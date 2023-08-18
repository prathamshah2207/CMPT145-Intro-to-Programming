# Student Name: Pratham Shah                        Section Number: 01
# NSID: mvr659                                      Course Number: 41442
# Student Number: 11353450                          Instructor: Lauresa Stilling


from a6q1 import *
from unittest.mock import patch

# Test1
test = "Input1.txt"
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
