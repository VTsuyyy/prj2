import re
import ast
import time
from random import randint
import google.generativeai as genai

# genai.configure(api_key='AIzaSyC2J5S7cQuj3cEo0LT_Kkc05NrKLsy8fWA')
genai.configure(api_key='AIzaSyBMpXlgd5xgUAP7rZFtS58Ef9WRzJDPlU0')
# genai.configure(api_key='GOOGLE_API_KEY1')

model = genai.GenerativeModel(model_name='gemini-pro')

chat = model.start_chat(history=[])

# Matrix distance
A = [[0, 68, 35, 1, 70, 25, 79, 59, 63, 65, 6, 46, 82],
[28, 0, 92, 96, 43, 28, 37, 92, 5, 3, 54, 93, 83],
[22, 17, 0, 96, 48, 27, 72, 39, 70, 13, 68, 100, 36],
[95, 4, 12, 0, 34, 74, 65, 42, 12, 54, 69, 48, 45],
[63, 58, 38, 60, 0, 42, 30, 79, 17, 36, 91, 43, 89],
[7, 41, 43, 65, 49, 0, 6, 91, 30, 71, 51, 7, 2],
[94, 49, 30, 24, 85, 55, 0, 41, 67, 77, 32, 9, 45],
[40, 27, 24, 38, 39, 19, 83, 0, 42, 34, 16, 40, 59],
[5, 31, 78, 7, 74, 87, 22, 46, 0, 73, 71, 30, 78],
[74, 98, 13, 87, 91, 62, 37, 56, 68, 0, 75, 32, 53],
[51, 51, 42, 25, 67, 31, 8, 92, 8, 38, 0, 88, 54],
[84, 46, 10, 10, 59, 22, 89, 23, 47, 7, 31, 0, 69],
[1, 92, 63, 56, 11, 60, 25, 38, 49, 84, 96, 42, 0]]


def objectFunction(list: int):
    cost = 0
    for i in range(len(list)-1):
        cost += A[list[i]-1][list[i+1]-1]
    return cost

def sortList(x):
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if(objectFunction(x[i]) > objectFunction(x[j])):
                tmp = x[i]
                x[i] = x[j]
                x[j] = tmp

set1 = {0}
set2 = {0}
mod = 65494786
def isExist(list):
    k1, k2 = 156, 654
    for i in range(len(list)):
        k1 = (k1*10 + list[i]*15)%mod
        k2 = (k1*13 + list[i]*19)%mod
    if k1 not in set1 and k2 not in set2:
        set1.add(k1)
        set2.add(k2)
        return False
    else:
        print("exist" + str(list))
        return True

mutation = """\nStrongly remember this mutation function for a list of integers:
def mutation(list: int):
    a = randint(0, 11)
    b = randint(a+1, 12)
    list[a], list[b] = list[b], list[a]
"""
response = chat.send_message(mutation)
print(response)


x = [[1, 9, 3, 2, 5, 11, 13, 7, 6, 4, 8, 10, 12], 
[10, 11, 9, 13, 1, 12, 8, 3, 7, 4, 6, 5, 2],
[10, 13, 1, 3, 7, 11, 4, 12, 5, 2, 9, 8, 6],
[10, 12, 13, 11, 8, 5, 3, 2, 7, 1, 4, 9, 6],
[13, 7, 11, 4, 10, 1, 12, 3, 2, 5, 9, 8, 6],
[10, 11, 8, 5, 3, 9, 2, 7, 6, 13, 1, 4, 12],]
prompt = "Give me 20 random permutation of numbers from 1 to 13 in type list and breacketed it with <trace> </trace>."
response = model.generate_content(prompt)
# print(response.text)
pattern = r'<trace>(.*?)</trace>'
matches = re.findall(pattern, response.text)
# print(matches)
for x1 in matches:
    x1 = ast.literal_eval(x1)
    print(x1)
    if(isinstance(x1, list) == False):
        continue
    else:
        x.append(x1)


for i in range(50):
    timeBegin = round(time.time()*1000)
    sortList(x)
    x = x[:15]
    for i in x:
        print(str(objectFunction(i)) + ' ' + str(i))
    description = "I give you xlist, each element in xlist is a list of integers: " + str(x)
    description += "\nMutation each list in xlist by mutation function. Directly give me for each list after mutation, breacketed it with <trace> </trace>. Donot give me source code."
    prompt = description
    response = model.generate_content(description)
    # print(response.text)
    # print("___")
    pattern = r'<trace>(.*?)</trace>'
    matches = re.findall(pattern, response.text)
    # x.clear()
    for x1 in matches:
        # print(x1)
        x1 = ast.literal_eval(x1)
        if(isinstance(x1, list) == False):
            continue
        if(isExist(x1)):
            continue
        x.append(x1)
    print("---")
    timeEnd = round(time.time()*1000)
    if(timeEnd-timeBegin < 30000):
        time.sleep((timeBegin+30000-timeEnd)/1000)
    # print(timeBegin)
    # print(timeEnd)