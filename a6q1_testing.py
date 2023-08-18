# Student Name: Pratham Shah                        Section Number: 01
# NSID: mvr659                                      Course Number: 41442
# Student Number: 11353450                          Instructor: Lauresa Stilling


from a6q1 import *
from unittest.mock import patch

# Test1
test = "input1.txt"
expected = ['*-*', '*-*', '*-*']
lst = []
with patch("builtins.input", side_effect=["n"]):
    Conway(test, 1)
with open("input1_1steps.txt", "r") as temp_file:
    for i in temp_file:
        lst.append(i.removesuffix('\n'))
if lst != expected:
    print("Testing Conway() with", test, "\n\tExpected:", expected, "\n\tGot:", lst)
else:
    print("Test1 Success...")

# Test2
test = "input2.txt"
expected = ['ZZ', 'ZZ']
lst = []
with patch("builtins.input", side_effect=["n"]):
    Conway(test, 2)
with open("input2_2steps.txt", "r") as temp_file:
    for i in temp_file:
        lst.append(i.removesuffix('\n'))
if lst != expected:
    print("Testing Conway() with", test, "\n\tExpected:", expected, "\n\tGot:", lst)
else:
    print("Test2 Success...")

# Test3
test = "input3.txt"
expected = ['-*-', '---', '-*-']
lst = []
with patch("builtins.input", side_effect=["n"]):
    Conway(test, 1)
with open("input3_1steps.txt", "r") as temp_file:
    for i in temp_file:
        lst.append(i.removesuffix('\n'))
if lst != expected:
    print("Testing Conway() with", test, "\n\tExpected:", expected, "\n\tGot:", lst)
else:
    print("Test3 Success...")

# Test4
test = "input4.txt"
expected = ['--', 'ZZ', 'ZZ', '--']
lst = []
with patch("builtins.input", side_effect=["n"]):
    Conway(test, 3)
with open("input4_3steps.txt", "r") as temp_file:
    for i in temp_file:
        lst.append(i.removesuffix('\n'))
if lst != expected:
    print("Testing Conway() with", test, "\n\tExpected:", expected, "\n\tGot:", lst)
else:
    print("Test4 Success...")

# Test5
test = "input5.txt"
expected = ['--ZZ', '--ZZ', '----', '----']
lst = []
with patch("builtins.input", side_effect=["n"]):
    Conway(test, 4)
with open("input5_4steps.txt", "r") as temp_file:
    for i in temp_file:
        lst.append(i.removesuffix('\n'))
if lst != expected:
    print("Testing Conway() with", test, "\n\tExpected:", expected, "\n\tGot:", lst)
else:
    print("Test5 Success...")

# Test6
test = "input6.txt"
expected = ['---', '-ZZ', '---']
lst = []
with patch("builtins.input", side_effect=["n"]):
    Conway(test)
with open("input6_3steps.txt", "r") as temp_file:
    for i in temp_file:
        lst.append(i.removesuffix('\n'))
if lst != expected:
    print("Testing Conway() with", test, "\n\tExpected:", expected, "\n\tGot:", lst)
else:
    print("Test6 Success...")

print("---Testing Complete---")

# Test7
test = "input7.txt"  # Empty File
expected = []
lst = []
with patch("builtins.input", side_effect=["n"]):
    Conway(test)
with open("input7_3steps.txt", "r") as temp_file:
    for i in temp_file:
        lst.append(i.removesuffix('\n'))
if lst != expected:
    print("Testing Conway() with", test, "\n\tExpected:", expected, "\n\tGot:", lst)
else:
    print("Test7 Success...")

print("---Testing Complete---")
