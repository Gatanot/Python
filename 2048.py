from random import randint
from os import system


def getAction():
    print("Enter:")
    print("\tA for left")
    print("\tD for right")
    print("\tW for up")
    print("\tS for down")
    action = input()
    return action


def checkMatrix(matrix):
    flag = False
    for i in range(0, 4):
        for j in range(0, 4):
            if matrix[i][j] == 0:
                flag = True
            elif matrix[i][j] == matrix[(i - 1) % 4][j]:
                if i == 0:
                    continue
                else:
                    flag = True
            elif matrix[i][j] == matrix[i][(j - 1) % 4]:
                if j == 0:
                    continue
                else:
                    flag = True
            elif matrix[i][j] == matrix[i][(j + 1) % 4]:
                if j == 3:
                    continue
                else:
                    flag = True
            elif matrix[i][j] == matrix[(i + 1) % 4][j]:
                if i == 3:
                    continue
                else:
                    flag = True
    return flag


def printMatrix(matrix, size):
    for i in range(0, size):
        for j in range(0, size):
            print(matrix[i][j], end="\t")
        print("\n", end="")


def updateMatrix(matrix, action):
    if action == "a" or action == "A":
        for row in range(0, 4):
            mark = -1
            for col in range(0, 4):
                if matrix[row][col] == 0:
                    continue
                else:
                    mark = mark + 1
                    if mark == col:
                        continue
                    else:
                        matrix[row][mark] = matrix[row][col]
                        matrix[row][col] = 0
            for col in range(0, 3):
                if matrix[row][col] == matrix[row][col + 1]:
                    matrix[row][col] = matrix[row][col] * 2
                    matrix[row][col + 1] = 0
            mark = -1
            for col in range(0, 4):
                if matrix[row][col] == 0:
                    continue
                else:
                    mark = mark + 1
                    if mark == col:
                        continue
                    else:
                        matrix[row][mark] = matrix[row][col]
                        matrix[row][col] = 0

    elif action == "d" or action == "D":
        for row in range(0, 4):
            mark = 4
            for col in range(0, 4):
                if matrix[row][3 - col] == 0:
                    continue
                else:
                    mark = mark - 1
                    if mark == 3 - col:
                        continue
                    else:
                        matrix[row][mark] = matrix[row][3 - col]
                        matrix[row][3 - col] = 0
            for col in range(0, 3):
                if matrix[row][3 - col] == matrix[row][2 - col]:
                    matrix[row][3 - col] = matrix[row][3 - col] * 2
                    matrix[row][2 - col] = 0
            mark = 4
            for col in range(0, 4):
                if matrix[row][3 - col] == 0:
                    continue
                else:
                    mark = mark - 1
                    if mark == 3 - col:
                        continue
                    else:
                        matrix[row][mark] = matrix[row][3 - col]
                        matrix[row][3 - col] = 0

    elif action == "w" or action == "W":
        for col in range(0, 4):
            mark = -1
            for row in range(0, 4):
                if matrix[row][col] == 0:
                    continue
                else:
                    mark = mark + 1
                    if mark == row:
                        continue
                    else:
                        matrix[mark][col] = matrix[row][col]
                        matrix[row][col] = 0
            for row in range(0, 3):
                if matrix[row][col] == matrix[row + 1][col]:
                    matrix[row][col] = matrix[row][col] * 2
                    matrix[row + 1][col] = 0
            mark = -1
            for row in range(0, 4):
                if matrix[row][col] == 0:
                    continue
                else:
                    mark = mark + 1
                    if mark == row:
                        continue
                    else:
                        matrix[mark][col] = matrix[row][col]
                        matrix[row][col] = 0

    elif action == "s" or action == "S":
        for col in range(0, 4):
            mark = 4
            for row in range(0, 4):
                if matrix[3 - row][col] == 0:
                    continue
                else:
                    mark = mark - 1
                    if mark == 3 - row:
                        continue
                    else:
                        matrix[mark][col] = matrix[3 - row][col]
                        matrix[3 - row][col] = 0
            for row in range(0, 3):
                if matrix[3 - row][col] == matrix[2 - row][col]:
                    matrix[3 - row][col] = matrix[3 - row][col] * 2
                    matrix[2 - row][col] = 0
            mark = 4
            for row in range(0, 4):
                if matrix[3 - row][col] == 0:
                    continue
                else:
                    mark = mark - 1
                    if mark == 3 - row:
                        continue
                    else:
                        matrix[mark][col] = matrix[3 - row][col]
                        matrix[3 - row][col] = 0
    else:
        print("You entered a wrong action")
    return matrix


def addMatrix(matrix):

    for i in range(0, 4):
        for j in range(0, 4):
            if matrix[i][j] == 0:
                tempNumber = randint(0, 7)
                if tempNumber % 7 == 0:
                    matrix[i][j] = 2

    return matrix


def main():
    size = 4
    matrix = []
    for i in range(0, size):
        tempList = []
        for j in range(0, size):
            tempNumber = randint(0, 6)
            if tempNumber % 3 == 0:
                tempList.append(2)
            else:
                tempList.append(0)
        matrix.append(tempList)
        steped = 0
    while True:
        if checkMatrix(matrix):
            printMatrix(matrix, size)
            print("Steped: ", end="")
            print(steped)
            steped = steped + 1
            action = getAction()
            tempMatrix = updateMatrix(matrix, action)
            if tempMatrix == matrix:
                tempMatrix = addMatrix(matrix)
            matrix = tempMatrix
            system("cls")
        else:
            system("cls")
            printMatrix(matrix, size)
            print("game over")
            return


def test():
    size = 4
    matrix = []
    for i in range(0, size):
        tempList = []
        for j in range(0, size):
            tempNumber = randint(0, 6)
            if tempNumber % 3 == 0:
                tempList.append(2)
            else:
                tempList.append(0)
        matrix.append(tempList)
    printMatrix(matrix, size)
    print()
    for i in range(0, 1):
        matrix = updateMatrix(matrix, "A")
        printMatrix(matrix, size)
        print()


main()
