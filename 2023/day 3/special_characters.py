import re

input = open(r"C:\Users\jaken\anaconda3\my_sandbox\advent of code\2023\day 3\input.txt", "r").read()
input = input.split("\n")

chars = []
for row in input:
    s = row.replace(".", "")
    result = ''.join([i for i in s if not i.isdigit()])
    print(result)

    chars.append(result)

