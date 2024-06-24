from support import *
from instance import *

import ast
import google.generativeai as genai


genai.configure(api_key='AIzaSyC2J5S7cQuj3cEo0LT_Kkc05NrKLsy8fWA')

model = genai.GenerativeModel(model_name='gemini-pro')

chat = model.start_chat(history=[])

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


#----------------------------------------------------------------------------------------------------------------------------------
# description = 'You are given a list of points with coordinates: {' + list2str() + '}. Your task is to find a trace, with the shortest possible length, that trverses each point exactly once.\n'
# in_context = 'Below are some previous traces and their lengths. The traces are arranged in descending order based on their lengths, where lower values are better.\n'
#in_context += pool2examples(Pool)                  ! NOTICE that each generation, Pool change.
# task_instruction = 'Please follow the instruction step-by-step to generate new trace:\n'
# task_instruction += 'Step 1. Select one trace from the above traces.\n'
# # task_instruction += 'Step 2. Crossover the two traces chosen in Step 1 and generate a new trace.\n'
# task_instruction += 'Step 2. Generate a new trace by choose two point c1, c2 in trace and inverse the trace between c1, c2.\n'
# task_instruction += ('Step 3. Keep the generated trace generated in Step 2, repeat Step 1, 2, until you have ' + str(N) + ' generated traces.\n')
# task_instruction += 'Directly give me all the chosen trace at Step 1, bracketed them with <selection> and </selection>, and all the generated traces at Step 2, bracketed them with <res> and </res>. Not any explanation needed.'

# description = 'You are given a list X = [1, 5, 3, 6, 2, 4, 7]. Your task is to generate a new list'
# in_context = 'Below are some previous traces and their lengths. The traces are arranged in descending order based on their lengths, where lower values are better.\n'
# task_instruction = 'Please follow the instruction step-by-step to generate new trace:\n'
# task_instruction += 'Step 1. Select one trace from the above traces.\n'
# task_instruction += 'Step 2. Crossover the two traces chosen in Step 1 and generate a new trace.\n'
# task_instruction += 'Step 2. Generate a new trace by choose two point c1, c2 in trace and inverse the trace between c1, c2.\n'
# task_instruction += ('Step 3. Keep the generated trace generated in Step 2, repeat Step 1, 2, until you have ' + str(N) + ' generated traces.\n')
# task_instruction += 'Directly give me all the chosen trace at Step 1, bracketed them with <selection> and </selection>, and all the generated traces at Step 2, bracketed them with <res> and </res>. Not any explanation needed.'

listOff = [[1, 5, 13, 9, 3, 12, 8, 10, 6, 2, 4, 11, 7]]
description = 'You are given list '
# for i in range(len(listOff)):
for i in range(1):
    description += 'x' + str(i) + ' = ' + str(listOff[i])
# description += """ and a matrix
# A = [[0, 68, 35, 1, 70, 25, 79, 59, 63, 65, 6, 46, 82],
# [28, 0, 92, 96, 43, 28, 37, 92, 5, 3, 54, 93, 83],
# [22, 17, 0, 96, 48, 27, 72, 39, 70, 13, 68, 100, 36],
# [95, 4, 12, 0, 34, 74, 65, 42, 12, 54, 69, 48, 45],
# [63, 58, 38, 60, 0, 42, 30, 79, 17, 36, 91, 43, 89],
# [7, 41, 43, 65, 49, 0, 6, 91, 30, 71, 51, 7, 2],
# [94, 49, 30, 24, 85, 55, 0, 41, 67, 77, 32, 9, 45],
# [40, 27, 24, 38, 39, 19, 83, 0, 42, 34, 16, 40, 59],
# [5, 31, 78, 7, 74, 87, 22, 46, 0, 73, 71, 30, 78],
# [74, 98, 13, 87, 91, 62, 37, 56, 68, 0, 75, 32, 53],
# [51, 51, 42, 25, 67, 31, 8, 92, 8, 38, 0, 88, 54],
# [84, 46, 10, 10, 59, 22, 89, 23, 47, 7, 31, 0, 69],
# [1, 92, 63, 56, 11, 60, 25, 38, 49, 84, 96, 42, 0]]
# """
# description += """. And below are the list objective function:
# def obj(list: int):
#     tmp = 0
#     for i in range(len(off)-1):
#         tmp += A[off[i]-1][off[i+1]-1]
#     return tmp
# The new list is valid if it has objective function value smaller than the origin list """
description += 'Your task is to generate 5 new list by function below:'
in_context = """
def cc(x: int):
    a = random.randint(1, 13)
    b = random.randint(1, 13)
    if(a > b):
        tmp = a
        a = b
        b = tmp
    while(a < b):
        tmp = x[b]
        x[b] = x[a]
        x[a] = tmp
        a += 1
        b -= 1
"""
task_instruction = 'Directly give me the origin list, bracketed them with <selection> and </selection> and give me the new list after call the function, bracketed them with <res> and </res>. Not any explanation needed.'

prompt = description + in_context + task_instruction
val = 2000*[0]
def obj(off: int):
    tmp = 0
    for i in range(len(off)-1):
        tmp += A[off[i]-1][off[i+1]-1]
    return tmp
def sortList():
    for i in range(len(listOff)):
        val[i] = obj(listOff[i])
    for i in range(len(listOff)):
        tmp = i
        tmp1 = val[i]
        for j in range(i, len(listOff)):
            if(val[tmp] > val[j]):
                tmp = j
        val[i] = val[tmp]
        val[tmp] = tmp1

gener = 1
G = 7
val[0] = obj(listOff[0])
while gener < G :
    gener += 1
    response = chat.send_message(prompt)
    print(response.text + '\n')
    newGen = cutGenTrace(response.text)
    print('\n' + str(listOff[0]) + ' ' + str(val[0]))
    # listOff.clear()
    for s in newGen:
        listOff.append(ast.literal_eval(s))
    sortList()
    for i in range(len(listOff)):
        print(str(listOff[i]) + ' ' + str(val[i]))
# print(listOff)
# P_sharp = transform(listOff[:N])

