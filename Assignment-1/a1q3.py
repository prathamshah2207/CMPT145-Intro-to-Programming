'''
Name: Pratham Shah					Class: CMPT145
NSID: mvr659						Section Number: 01
student number: 11353450			Instructor: Lauresa Stilling
'''

import numpy as np
import math

l = []


def Conway(fileName):
    '''
    This function reads the input file and makes an array out of it. Then it calls another function and passes the array into it.
    :param fileName: Name of the file
    :return: None
    '''
    global x
    file = open(fileName, "r")

    for line in file:
        line = line.rstrip()
        for element in line:
            l.append(element)
    x = int(math.sqrt(len(l)))
    arr = np.array(l).reshape(x, x)

    file.close()
    NeighbourCheck(arr)


def list_to_array(l):
    '''
    This function converts input list into array
    :param l: List of input in form of living and dead cells
    :return: output_array and output_list
    '''
    global x
    x = int(math.sqrt(len(l)))
    arr = np.array(l).reshape(x, x)
    return NeighbourCheck(arr)


def NeighbourCheck(ary):
    '''
    This function counts the number of alive neighbours of each cell and makes an array of it. Then it passes both arrays to next function.
    :param ary: Original array from input
    :return: output_array and output_list
    '''
    List_of_lives = []
    for i in range(len(ary)):
        for j in range(len(ary[i])):
            lives = 0

            # Top
            if ary[i - 1][j] == '*' and i > 0:
                lives += 1
            # Left
            if ary[i][j - 1] == '*' and j > 0:
                lives += 1
            # Bottom
            try:
                if ary[i + 1][j] == '*' and i < x - 1:
                    lives += 1
            except IndexError:
                pass
            # Right
            try:
                if ary[i][j + 1] == '*' and j < x - 1:
                    lives += 1
            except IndexError:
                pass

            List_of_lives.append(lives)
    life_array = np.array(List_of_lives).reshape(x, x)
    return GameOfLife(ary, life_array)


def GameOfLife(arr1, arr_life):
    '''
    This function makes a new file and adds living and dead cells as per the conditions provided.
    :param arr1: Original array from input
    :param arr_life: Array of count of living neighbour cells of each cell
    :return: output_array and output_list
    '''
    new_file = f'{x}' + "x" + f'{x}' + '_updated.txt'
    f = open(new_file, "w")
    output_list = []
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            if arr_life[i][j] < 2 or arr_life[i][j] > 3:
                f.write("-")
                output_list.append('-')
            elif (arr_life[i][j] == 2 or arr_life[i][j] == 3) and arr1[i][j] == "*":
                f.write("*")
                output_list.append('*')
            elif arr_life[i][j] == 3:
                f.write("*")
                output_list.append('*')
            else:
                f.write("-")
                output_list.append('-')
        f.write("\n")
    f.close()
    output_array = np.array(output_list).reshape(x, x)
    return output_array, output_list


Conway("input1.txt")
