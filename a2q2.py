###############################################################################
# CMPT 145 Course material
# Original Author: Lauresa Stilling
# Date Created:   31 May 2023
# Last Edited:    31 May 2023
#
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this
# file to a public or private website, or providing this file to a person
# not registered in CMPT 145, constitutes Academic Misconduct, according
# to the University of Saskatchewan Policy on Academic Misconduct.
#
# Synopsis:
#    Testing; relevant to Chapter 5, 6, 7
###############################################################################

# TODO: Fill in your information below
# Student Name: Pratham Shah                        Section Number: 01
# NSID: mvr659                                      Course Number: 41442
# Student Number: 11353450                          Instructor: Lauresa Stilling

################### DO NOT ALTER CODE BELOW ###################################
def gcd(val1: int, val2: int) -> int:
    """
    Purpose: Find the greatest common divisor (gcd) of the two values passed in.
    Pre-conditions:
        :param val1: int - integer value being compared to find gcd.
            Must be less than 1000, else returns -1
        :param val2: int - integer value being compared to find gcd
            Must be less than 1000, else returns -1
    Post Conditions:
        None
    Return:
        int - The greatest common positive divisor of the two numbers passed in.
            -1 returned on failure.
    """
    return -1


def replace(input_str: str, target: str, replacement: str) -> str:
    """
    Purpose: Replace all instances of target string with replacement string within input string.
        Starting at the first occurrence of target string.
    Pre-condition
        :param input_str:str - input string to change target strings to replacement strings
        :param target: str - string that one wishes to change
        :param replacement: str - string that will replace target strings in the input string
    Post Condition:
        None
    Return:
        str - new string where target strings have been changed to replacement string
    """
    new_str = ""
    inp_len = len(input_str)
    targ_len = len(target)
    if inp_len < targ_len:
        new_str = input_str
    else:
        i = 0
        while i < inp_len:
            if input_str[i:i+targ_len] == target:
                new_str += replacement
                i += targ_len
            else:
                new_str += input_str[i]
                i += 1
    return new_str


def grade_letter(score:int) -> str:
    """
    Purpose: Get the grade letter related to the score passed in.

    Pre-condition
        :param score:int - the number being calculated to a letter grade.
            Should be within the range of 0-100
    Post Condition:
        None
    Return:
        str - string associated with the score passed in
            if score is outside valid range returns the string "Invalid"
    """
    letter = ""
    if score < 0 or score > 100:
        letter = "Invalid"
    elif score >= 90:
        letter = "A"
    elif score >= 80:
        letter = "B"
    elif score >= 70:
        letter = "C"
    elif score >= 60:
        letter = "D"
    else:
        letter = "F"
    return letter

def sort_students_into_grades(student_list: list) -> dict:
    """
    Purpose: Goes through a list of dictionaries adding student names to the appropriate dictionary grade letter
        If the student's grade is not one of "A", "B", "C", "D", or "F", it is added to list "Invalid".
    Pre-condition:
        :param student_list: list of dictionaries,
            each dictionary represents a student and contains two keys: 'name' and 'grade'
    Post Condition:
        None
    Return:
        dict with lists as values; each key has a list value of names of students with that grade letter.
            Contains the keys "A","B","C","D","F","Invalid"
    """
    return {}
################### DO NOT ALTER CODE ABOVE ###################################


# TODO: Create tests for functions above

#Tests for first function

test = [50, 0]
expected = 50
result = gcd(test[0], test[1])
if result != expected:
    print("Testing gcd() with", test[0], "and", test[1], "Expected:", expected, "got:", result)

test = [365, 1000]
expected = -1
result = gcd(test[0], test[1])
if result != expected:
    print("Testing gcd() with", test[0], "and", test[1], "Expected:", expected, "got:", result)

test = [-150, 200]
expected = 50
result = gcd(test[0], test[1])
if result != expected:
    print("Testing gcd() with", test[0], "and", test[1], "Expected:", expected, "got:", result)


#Tests for second function

test = ["Hello, hello, HELLO!", "hello", "Hi"]
expected = "Hello, Hi, HELLO!"
result = replace(test[0], test[1], test[2])
if result != expected:
    print("Testing replace() with ", test, "Expected:", expected, "got:", result)

test = ["I am happy.", "happy", "extremely joyful and content"]
expected = "I am extremely joyful and content."
result = replace(test[0], test[1], test[2])
if result != expected:
    print("Testing replace() with ", test, "Expected:", expected, "got:", result)

test = ["ababab", "aba", "x"]
expected = "xxb"
result = replace(test[0], test[1], test[2])
if result != expected:
    print("Testing replace() with ", test, "Expected:", expected, "got:", result)


#Tests for third function

test = -10
expected = "Invalid"
result = grade_letter(test)
if result != expected:
    print("Testing grade_letter() with ", test, "Expected:", expected, "got:", result)

test = 00
expected = "F"
result = grade_letter(test)
if result != expected:
    print("Testing grade_letter() with ", test, "Expected:", expected, "got:", result)

test = 70
expected = "C"
result = grade_letter(test)
if result != expected:
    print("Testing grade_letter() with ", test, "Expected:", expected, "got:", result)


#Tests for forth function

test = []
expected = {
    "A": [],
    "B": [],
    "C": [],
    "D": [],
    "F": [],
    "Invalid": []
}
result = sort_students_into_grades(test)
if result != expected:
    print("Testing sort_students_into_grades() with", test, "   Expected:", expected, " Got: ", result)

test = [
    {"name": "abhi", "grade": "A"},
    {"name": "benstock", "grade": "A"},
    {"name": "Charlie", "grade": "B"},
    {"name": "milli", "grade": "B"},
    {"name": "morning star", "grade": "C"}
]
expected = {
    "A": ["abhi", "benstock"],
    "B": ["Charlie", "milli"],
    "C": ["morning star"],
    "D": [],
    "F": [],
    "Invalid": []
}
result = sort_students_into_grades(test)
if result != expected:
    print("Testing sort_students_into_grades() with", test, "   Expected:", expected, " Got: ", result)

test = [
    {"name": "abhi", "grade": "A"},
    {"name": "jack ryan", "grade": "B"},
    {"name": "Charlie", "grade": "Z"},
    {"name": "milli", "grade": "D"},
    {"name": "morning star", "grade": "F"}
]
expected = {
    "A": ["abhi"],
    "B": ["jack ryan"],
    "C": [],
    "D": ["milli"],
    "F": ["morning star"],
    "Invalid": ["Charlie"]
}
result = sort_students_into_grades(test)
if result != expected:
    print("Testing sort_students_into_grades() with", test, "   Expected:", expected, "Got:",result)

# TODO Create test driver for whitebox tested functions

def white_box_test_driver():
    # Test gcd function
    print("Testing gcd function:")
    print(gcd(10, 15))  # Expected output: 5
    print(gcd(28, 14))  # Expected output: 14
    print(gcd(1000, 500))  # Expected output: -1 (out of range)

    # Test replace function
    print("\nTesting replace function:")
    print(replace("Hello, world!", "o", "x"))  # Expected output: Hellx, wxrld!
    print(replace("banana", "na", "apple"))  # Expected output: baappleapple
    print(replace("Hello, world!", "xyz", "123"))  # Expected output: Hello, world!

    # Test grade_letter function
    print("\nTesting grade_letter function:")
    print(grade_letter(85))  # Expected output: B
    print(grade_letter(92))  # Expected output: A
    print(grade_letter(45))  # Expected output: F
    print(grade_letter(110))  # Expected output: Invalid (out of range)

    # Test sort_students_into_grades function
    print("\nTesting sort_students_into_grades function:")
    students = [
        {"name": "Alice", "grade": 85},
        {"name": "Bob", "grade": 92},
        {"name": "Charlie", "grade": 77},
        {"name": "David", "grade": 65},
        {"name": "Eve", "grade": 45},
        {"name": "Frank", "grade": 110},
        {"name": "Grace", "grade": 78},
        {"name": "Henry", "grade": 92},
    ]
    result = sort_students_into_grades(students)
    print(result)
    # Expected output: {'A': ['Bob', 'Henry'], 'B': ['Alice'], 'C': ['Charlie', 'Grace'], 'D': ['David'], 'F': ['Eve'], 'Invalid': ['Frank']}


# TODO: Create test driver for blackbox tested functions


def black_box_test_driver():
    # Test gcd function
    print("Testing gcd function:")
    gcd_test_cases = [
        {"input": (18, 9), "expected_output": 9},
        {"input": (0, 7), "expected_output": 7},
        {"input": (1000, 500), "expected_output": -1},
        {"input": (-12, 8), "expected_output": 4},
    ]
    for test_case in gcd_test_cases:
        input_val1, input_val2 = test_case["input"]
        expected_output = test_case["expected_output"]
        output = gcd(input_val1, input_val2)
        print(f"Input: {input_val1}, {input_val2} | Output: {output} | Expected: {expected_output} | Pass: {output == expected_output}")

    # Test replace function
    print("\nTesting replace function:")
    replace_test_cases = [
        {"input": ("Hello, world!", "world", "earth"), "expected_output": "Hello, earth!"},
        {"input": ("", "abc", "xyz"), "expected_output": ""},
        {"input": ("Test test", "test", ""), "expected_output": "Test "},
    ]
    for test_case in replace_test_cases:
        input_str, target, replacement = test_case["input"]
        expected_output = test_case["expected_output"]
        output = replace(input_str, target, replacement)
        print(f"Input: '{input_str}', '{target}', '{replacement}' | Output: '{output}' | Expected: '{expected_output}' | Pass: {output == expected_output}")

    # Test grade_letter function
    print("\nTesting grade_letter function:")
    grade_letter_test_cases = [
        {"input": 110, "expected_output": "Invalid"},
        {"input": 100, "expected_output": "A"},
        {"input": 73, "expected_output": "C"},
    ]
    for test_case in grade_letter_test_cases:
        input_score = test_case["input"]
        expected_output = test_case["expected_output"]
        output = grade_letter(input_score)
        print(f"Input: {input_score} | Output: {output} | Expected: {expected_output} | Pass: {output == expected_output}")

    # Test sort_students_into_grades function
    print("\nTesting sort_students_into_grades function:")
    students = [
        {"name": "David", "grade": "D"},
        {"name": "Eve", "grade": "F"},
        {"name": "Frank", "grade": "Invalid"},
        {"name": "Grace", "grade": "B"},
        {"name": "Henry", "grade": "A"},
    ]
    expected_output = {
        "A": ["Henry"],
        "B": ["Grace"],
        "C": [],
        "D": ["David"],
        "F": ["Eve"],
        "Invalid": ["Frank"],
    }
    output = sort_students_into_grades(students)
    print(f"Output: {output} | Expected: {expected_output} | Pass: {output == expected_output}")


# TODO: Create test driver to test all functions
