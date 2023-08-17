# Student Name: Pratham Shah                        Section Number: 01
# NSID: mvr659                                      Course Number: 41442
# Student Number: 11353450                          Instructor: Lauresa Stilling

import numpy as np


def Conway(fileName, iterations=3):
    '''
    This function reads the input file and makes an array out of it. Then it calls another function and passes the array into it.
    :param fileName: Name of the file
    :return: None
    '''
    global line, row_count, column_count, file_noExt, original_iterations

    file_noExt = fileName.removesuffix('.txt')
    original_iterations = iterations
    row_count = 0
    l = []

    file = open(fileName, "r")

    for line in file:
        line = line.rstrip()
        row_count += 1
        for element in line:
            l.append(element)

    column_count = len(line)
    arr = np.array(l).reshape(row_count, column_count)

    file.close()

    NeighbourCheck(arr, iterations)


def NeighbourCheck(ary, iterations):
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

            # Top-Left
            try:
                if ary[currentRow - 1][currentElement - 1] == '*' and currentRow > 0 and currentElement > 0:
                    lives += 1
            except IndexError:
                pass

            # Left
            if ary[currentRow][currentElement - 1] == '*' and currentElement > 0:
                lives += 1

            # Bottom-Left
            try:
                if ary[currentRow + 1][currentElement - 1] == '*' and currentRow < row_count - 1 and currentElement > 0:
                    lives += 1
            except IndexError:
                pass

            # Bottom
            try:
                if ary[currentRow + 1][currentElement] == '*' and currentRow < row_count - 1:
                    lives += 1
            except IndexError:
                pass

            # Bottom-Right
            try:
                if ary[currentRow + 1][
                    currentElement + 1] == '*' and currentRow < row_count - 1 and currentElement < column_count - 1:
                    lives += 1
            except IndexError:
                pass

            # Right
            try:
                if ary[currentRow][currentElement + 1] == '*' and currentElement < column_count - 1:
                    lives += 1
            except IndexError:
                pass

            # Top-Right
            try:
                if ary[currentRow - 1][
                    currentElement + 1] == '*' and currentRow > 0 and currentElement < column_count - 1:
                    lives += 1
            except IndexError:
                pass

            List_of_lives.append(lives)
    life_array = np.array(List_of_lives).reshape(row_count, column_count)

    # If iterations are over then we go to different function to make output file
    if iterations <= 0:
        file_maker(ary)
    else:
        iterations -= 1
        GameOfLife(ary, life_array, iterations)


def GameOfLife(arr1, arr_life, iterations):
    '''
    This function makes a new file and adds living and dead cells as per the conditions provided.
    :param arr1: Original array from input
    :param arr_life: Array of count of living neighbour cells of each cell
    :return: output_array and output_list
    '''

    output_list = []
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            if arr_life[i][j] < 2 or arr_life[i][j] > 3:
                output_list.append('-')
            elif (arr_life[i][j] == 2 or arr_life[i][j] == 3) and arr1[i][j] == "*":
                output_list.append('*')
            elif arr_life[i][j] == 3:
                output_list.append('*')
            else:
                output_list.append('-')

    output_array = np.array(output_list).reshape(row_count, column_count)
    NeighbourCheck(output_array, iterations)


def file_maker(final_array):
    new_file = f'{file_noExt}' + "_" + f'{original_iterations}' + "steps.txt"
    f = open(new_file, "w")
    for line in final_array:
        for element in line:
            element = str(element)
            f.write(element)
        f.write('\n')
    f.close()
    print("Program Success...")
