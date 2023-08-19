'''
Name: Pratham Shah					Class: CMPT145
NSID: mvr659						Section Number: 01
student number: 11353450			Instructor: Lauresa Stilling
'''

from a1q3 import list_to_array
import numpy as np
import math

# Test1
test = list("*-*****-*")
expected = list('-*-***-*-')
arr, lst = list_to_array(test)
if lst != expected:
    print("Testing list_to_array() with", test, "\nExpected:",
          np.array(expected).reshape(int(math.sqrt(len(expected))), int(math.sqrt(len(expected)))), "\ngot:", arr)
else:
    print("Test1 Success...")

# Test2
test = list("")
expected = list('')
arr, lst = list_to_array(test)
if lst != expected:
    print("Testing list_to_array() with", test, "\nExpected:",
          np.array(expected).reshape(int(math.sqrt(len(expected))), int(math.sqrt(len(expected)))), "\ngot:", arr)
else:
    print("Test2 Success...")

# Test3
test = list("*-*-")
expected = list('----')
arr, lst = list_to_array(test)
if lst != expected:
    print("Testing list_to_array() with", test, "\nExpected:",
          np.array(expected).reshape(int(math.sqrt(len(expected))), int(math.sqrt(len(expected)))), "\ngot:", arr)
else:
    print("Test3 Success...")

# Test4
test = list("****************")
expected = list('*****--**--*****')
arr, lst = list_to_array(test)
if lst != expected:
    print("Testing list_to_array() with", test, "\nExpected:",
          np.array(expected).reshape(int(math.sqrt(len(expected))), int(math.sqrt(len(expected)))), "\ngot:", arr)
else:
    print("Test4 Success...")

# Test5
test = list("*")
expected = list('-')
arr, lst = list_to_array(test)
if lst != expected:
    print("Testing list_to_array() with", test, "\nExpected:",
          np.array(expected).reshape(int(math.sqrt(len(expected))), int(math.sqrt(len(expected)))), "\ngot:", arr)
else:
    print("Test5 Success...")

# Test6
test = list("*---*-*-*---*---*-*-*---*")
expected = list('-------*---*-*---*-------')
arr, lst = list_to_array(test)
if lst != expected:
    print("Testing list_to_array() with", test, "\nExpected:",
          np.array(expected).reshape(int(math.sqrt(len(expected))), int(math.sqrt(len(expected)))), "\ngot:", arr)
else:
    print("Test6 Success...")

# Test7
test = list("------***--*-*--***------")
expected = list('------***--*-*--***------')
arr, lst = list_to_array(test)
if lst != expected:
    print("Testing list_to_array() with", test, "\nExpected:",
          np.array(expected).reshape(int(math.sqrt(len(expected))), int(math.sqrt(len(expected)))), "\ngot:", arr)
else:
    print("Test7 Success...")
