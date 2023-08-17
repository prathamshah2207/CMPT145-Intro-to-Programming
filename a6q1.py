# Student Name: Pratham Shah                        Section Number: 01
# NSID: mvr659                                      Course Number: 41442
# Student Number: 11353450                          Instructor: Lauresa Stilling

import numpy as np
import math

l = []

def Conway(fileName):
    '''
    This function reads the input file and makes an array out of it. Then it calls another function and passes the array into it.
    :param fileName: Name of the file
    :return: None
    '''
    global line, row_count, column_count, file_noExt
    file_noExt = fileName.removesuffix('.txt')
    row_count = 0

    file = open(fileName, "r")

    for line in file:
        line = line.rstrip()
        row_count += 1
        for element in line:
            l.append(element)

    column_count = len(line)
    arr = np.array(l).reshape(row_count, column_count)

    file.close()
    NeighbourCheck(arr)


def NeighbourCheck(ary):
    '''
    This function counts the number of alive neighbours of each cell and makes an array of it. Then it passes both arrays to next function.
    :param ary: Original array from input
    :return: output_array and output_list
    '''
    List_of_lives = []
    for currentRow in range(len(ary)):
        for currentElement in range(len(ary[currentRow])):
            lives = 0

            # Top
            if ary[currentRow - 1][currentElement] == '*' and currentRow > 0:
                lives += 1
            # Left
            if ary[currentRow][currentElement - 1] == '*' and currentElement > 0:
                lives += 1
            # Bottom
            try:
                if ary[currentRow + 1][currentElement] == '*' and currentRow < row_count - 1:
                    lives += 1
            except IndexError:
                pass
            # Right
            try:
                if ary[currentRow][currentElement + 1] == '*' and currentElement < column_count - 1:
                    lives += 1
            except IndexError:
                pass

            List_of_lives.append(lives)
    life_array = np.array(List_of_lives).reshape(row_count, column_count)
    return GameOfLife(ary, life_array)


def GameOfLife(arr1, arr_life):
    '''
    This function makes a new file and adds living and dead cells as per the conditions provided.
    :param arr1: Original array from input
    :param arr_life: Array of count of living neighbour cells of each cell
    :return: output_array and output_list
    '''
    new_file = f'{file_noExt}' + "_1steps.txt"
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
    output_array = np.array(output_list).reshape(row_count, column_count)
    return output_array, output_list

Conway("input1.txt")