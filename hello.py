import re
import ast
from random import randint
import google.generativeai as genai


genai.configure(api_key='AIzaSyC2J5S7cQuj3cEo0LT_Kkc05NrKLsy8fWA')
# genai.configure(api_key='AIzaSyBMpXlgd5xgUAP7rZFtS58Ef9WRzJDPlU0')

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

# objectect function
# def object(list: int):
#     temporary = 0
#     for i in range(len(list)-1):
#         temporary += A[list[i]][list[i+1]]
    # return temporary

# list solution
x = [[1, 2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2, 1]]

# Give length matrix to LLM
matrix = "Strongly remember this 2D matrix A: " + str(A) 
# matrix += "This matrix mean distance from point i to point j is A[i][j]."
objectFunc = """Strongly remember to evaluate cost of a list, you should get the matrix A and sum all distances int that list. example: cost of [2, 4, 3, 1, 5] is A[2][4] + A[4][3] + A[3][1] + A[1][5]."""
# objectFunc = """ And strongly remember to evaluate cost of list, you and use cost function below:
# def cost_function(list: int):
#     cost = 0
#     for i in range(len(list)-1):
#         cost += A[list[i]][list[i+1]]
#     return cost
# """
response = chat.send_message(matrix + objectFunc)

mutation = """\nStrongly remember this mutation function for a list:
def mutation(list: int):
    a = random.randint(0, 6)
    b = random.randint(0, 6)
    tmp = list[b]
    list[b] = list[a]
    list[a] = tmp
"""
# response = chat.send_message(mutation)



# for i in range(5):
#     # task_instruction
#     print("xl: " + str(x))
#     description = "Get the list A from past. I give you xlist, each element in xlist is a list of integers: " + str(x)
#     description += "\nMutation each list in xlist by mutation function and evaluate cost of it. Directly give me for each list after mutation, breacketed it with <trace> </trace> and cost of it. Donot give me source code."
#     prompt = description
#     response = chat.send_message(description)
#     print(response.text)
#     print("___")
#     pattern = r'<trace>(.*?)</trace>'
#     matches = re.findall(pattern, response.text)
#     x.clear()
#     for x1 in matches:
#         print(x1)
#         x1 = ast.literal_eval(x1)
#         if(isinstance(x1, list) == False):
#             continue
#         x.append(x1)
#     print("---")


for i in range(5):
    a = randint(0, 11)
    b = randint(0, 11)
    prompt = "When you want the value of " + f"A[{a}][{b}], you can see it is row {a+1} and column {b+1}, it is equal {A[a][b]}"
    print(prompt)
    # prompt += ", don't give me matrix A."
    response = chat.send_message(prompt)
    print(response.text)
    # prompt = f"give me A[{a}][{b}]"
    # print(f"true:  {A[a][b]}")
    # prompt += ", don't give me matrix A."
    # response = chat.send_message(prompt)
    # print(response.text)

print("\n\n\n")

for i in range(5):
    a = randint(0, 11)
    b = randint(0, 11)
    prompt = f"give me A[{a}][{b}]"
    print(f"true: A[{a}][{b}] = {A[a][b]}")
    # prompt += ", don't give me matrix A."
    response = chat.send_message(prompt)
    print(response.text)
