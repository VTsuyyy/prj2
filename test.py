import re
import ast
import time

response ="""
<trace>[7, 2, 10, 4, 6, 11, 8, 5, 12, 13, 9, 3, 1]</trace>
<trace>[13, 12, 11, 5, 8, 1, 2, 9, 4, 10, 7, 3, 6]</trace>
<trace>[5, 3, 11, 1, 13, 7, 8, 9, 10, 4, 6, 12, 2]</trace>
<trace>[4, 11, 6, 10, 1, 3, 12, 2, 13, 8, 7, 9, 5]</trace>
<trace>[13, 10, 1, 3, 9, 2, 6, 7, 5, 11, 8, 4, 12]</trace>
<trace>[12, 13, 3, 5, 9, 2, 7, 6, 4, 11, 10, 8, 1]</trace>
<trace>[1, 11, 8, 3, 7, 12, 6, 13, 5, 10, 2, 4, 9]</trace>
<trace>[8, 2, 1, 11, 13, 7, 12, 6, 4, 10, 5, 9, 3]</trace>
<trace>[7, 10, 1, 9, 8, 12, 6, 2, 4, 13, 11, 5, 3]</trace>
<trace>[12, 11, 9, 4, 10, 6, 2, 8, 3, 7, 13, 1, 5]</trace>
<trace>[11, 12, 3, 9, 4, 6, 7, 2, 13, 8, 5, 1, 10]</trace>
<trace>[1, 7, 12, 4, 6, 3, 5, 11, 8, 10, 9, 13, 2]</trace>
<trace>[9, 10, 3, 8, 2, 6, 7, 5, 12, 13, 11, 4, 1]</trace>
<trace>[7, 8, 5, 12, 1, 4, 11, 10, 9, 6, 13, 2, 3]</trace>
<trace>[2, 3, 4, 6, 8, 12, 11, 5, 1, 13, 9, 7, 10]</trace>
"""
pattern = r'<trace>(.*?)</trace>'
matches = re.findall(pattern, response)
for x1 in matches:
    x1 = ast.literal_eval(x1)
    print(x1)
    if(isinstance(x1, list) == False):
        continue
