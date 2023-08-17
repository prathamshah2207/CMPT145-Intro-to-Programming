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
    global line, row_count, column_count, file_noExt, original_iterations, bool

    file_noExt = fileName.removesuffix('.txt')
    original_iterations = iterations
    row_count = 0
    l = []

    # Ask User for console outputs
    user_input = input("To see the results in the console press Y or press N otherwise: ")
    if user_input == 'y' or user_input == 'Y':
        bool = True
    else:
        bool = False

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
                if ary[currentRow + 1][currentElement + 1] == '*' and currentRow < row_count - 1 and currentElement < column_count - 1:
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
                if ary[currentRow - 1][currentElement + 1] == '*' and currentRow > 0 and currentElement < column_count - 1:
                    lives += 1
            except IndexError:
                pass

            List_of_lives.append(lives)
    life_array = np.array(List_of_lives).reshape(row_count, column_count)
    def zombie_neighbour():
        zombie_counter = []

        for currentRow in range(len(ary)):
            for currentElement in range(len(ary[currentRow])):
                zombies = 0

                # Top
                if ary[currentRow - 1][currentElement] == 'Z' and currentRow > 0:
                    zombies += 1

                # Top-Left
                try:
                    if ary[currentRow - 1][currentElement - 1] == 'Z' and currentRow > 0 and currentElement > 0:
                        zombies += 1
                except IndexError:
                    pass

                # Left
                if ary[currentRow][currentElement - 1] == 'Z' and currentElement > 0:
                    zombies += 1

                # Bottom-Left
                try:
                    if ary[currentRow + 1][currentElement - 1] == 'Z' and currentRow < row_count - 1 and currentElement > 0:
                        zombies += 1
                except IndexError:
                    pass

                # Bottom
                try:
                    if ary[currentRow + 1][currentElement] == 'Z' and currentRow < row_count - 1:
                        zombies += 1
                except IndexError:
                    pass

                # Bottom-Right
                try:
                    if ary[currentRow + 1][
                        currentElement + 1] == 'Z' and currentRow < row_count - 1 and currentElement < column_count - 1:
                        zombies += 1
                except IndexError:
                    pass

                # Right
                try:
                    if ary[currentRow][currentElement + 1] == 'Z' and currentElement < column_count - 1:
                        zombies += 1
                except IndexError:
                    pass

                # Top-Right
                try:
                    if ary[currentRow - 1][currentElement + 1] == 'Z' and currentRow > 0 and currentElement < column_count - 1:
                        zombies += 1
                except IndexError:
                    pass
                zombie_counter.append(zombies)
        zb_ary = np.array(zombie_counter).reshape(row_count, column_count)
        return zb_ary

    zombie_array = zombie_neighbour()

    # If iterations are over then we go to different function to make output file
    if iterations <= 0:
        file_maker(ary)
    else:
        iterations -= 1
        GameOfLife(ary, life_array, zombie_array, iterations)


def GameOfLife(arr1, arr_life, arr_zombie, iterations):
    '''
    This function makes a new file and adds living and dead cells as per the conditions provided.
    :param arr1: Original array from input
    :param arr_life: Array of count of living neighbour cells of each cell
    :return: output_array and output_list
    '''

    output_list = []
    # for i in range(len(arr1)):
    #     for j in range(len(arr1[i])):
    #         if arr_life[i][j] < 2 or arr_life[i][j] > 3:
    #             output_list.append('-')
    #         elif (arr_life[i][j] == 2 or arr_life[i][j] == 3) and arr1[i][j] == "*":
    #             output_list.append('*')
    #         elif arr_life[i][j] == 3:
    #             output_list.append('*')
    #         else:
    #             output_list.append('-')

    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            life_count = arr_life[i][j] + arr_zombie[i][j]
            if life_count < 2 or life_count > 3:
                output_list.append('-')
            elif arr1[i][j] == "*" and arr_zombie[i][j] > 0:
                output_list.append('Z')
            elif arr1[i][j] == "*":
                output_list.append('*')
            elif arr1[i][j] == "Z":
                output_list.append('Z')
            elif life_count == 3:
                output_list.append('Z')
            else:
                output_list.append('-')

    output_array = np.array(output_list).reshape(row_count, column_count)

    if bool == True:
        print("\nIteration -", original_iterations - iterations)
        for line in output_array:
            for element in line:
                print(element, end='')
            print()

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
