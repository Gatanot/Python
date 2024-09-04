import random
import os
from time import sleep


def printMatrix(matrix, size):
    for i in range(0, size):
        for j in range(0, size):
            print(matrix[i][j], end=" ")
        print("\n", end="")


def checkNumber(matrix, row, col, size):
    Number = (
        matrix[row - 1][col - 1]
        + matrix[row - 1][col]
        + matrix[row - 1][col + 1]
        + matrix[row][col - 1]
        + matrix[row][col + 1]
        + matrix[row + 1][col - 1]
        + matrix[row + 1][col]
        + matrix[row + 1][col + 1]
    )

    return Number


def developMatrix(matrix, size):
    developedMatrix = []
    for i in range(0, size + 2):
        tempList = []
        if i == 0:
            for j in range(0, size + 2):
                if j == 0:
                    tempList.append(matrix[size - 1][size - 1])
                elif j == size + 1:
                    tempList.append(matrix[size - 1][0])
                else:
                    tempList.append(matrix[size - 1][j - 1])
        elif i == size + 1:
            for j in range(0, size + 2):
                if j == 0:
                    tempList.append(matrix[0][size - 1])
                elif j == size + 1:
                    tempList.append(matrix[0][0])
                else:
                    tempList.append(matrix[0][j - 1])
        else:
            for j in range(0, size + 2):
                if j == 0:
                    tempList.append(matrix[i - 1][size - 1])
                elif j == size + 1:
                    tempList.append(matrix[i - 1][0])
                else:
                    tempList.append(matrix[i - 1][j - 1])
        developedMatrix.append(tempList)
    return developedMatrix


def processMatrix(matrix, size):
    tempMatrix = developMatrix(matrix, size)
    for i in range(0, size):
        for j in range(0, size):
            tempNumber = checkNumber(tempMatrix, i + 1, j + 1, size)
            if tempMatrix:
                if tempNumber <= 1 or tempNumber >= 4:
                    matrix[i][j] = 0
            else:
                if tempNumber == 3:
                    matrix[i][j] = 1
    return matrix


def main():
    size = int(input("enter x times x\n"))
    matrix = []
    for i in range(0, size):
        tempList = []
        for j in range(0, size):
            tempList.append(random.randint(0, 1))
        matrix.append(tempList)

    printMatrix(matrix, size)
    while True:
        matrix = processMatrix(matrix, size)
        printMatrix(matrix, size)
        sleep(1)
        os.system("cls")


def test():
    size = int(input("enter x times x\n"))
    matrix = []
    for i in range(0, 4):
        tempList = []
        for j in range(0, 4):
            tempList.append(random.randint(0, 1))
        matrix.append(tempList)

    printMatrix(matrix, size)
    matrix = processMatrix(matrix, size)
    print(matrix)

main()