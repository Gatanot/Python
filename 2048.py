from random import randint
from os import system
from time import sleep


def getIn():
    return True


def getAction():
    print("Enter:")
    print("\tA for left")
    print("\tD for right")
    print("\tW for up")
    print("\tS for down")
    action = input()
    return action


def checkMatrix(matrix):
    for i in range(0, 4):
        for j in range(0, 4):
            if matrix[i][j] == 0:
                return True
            elif matrix[i][j] == matrix[(i - 1) % 4][j]:
                return True
            elif matrix[i][j] == matrix[i][(j - 1) % 4]:
                return True
            elif matrix[i][j] == matrix[i][(j + 1) % 4]:
                return True
            elif matrix[i][j] == matrix[(i + 1) % 4][j]:
                return True
            else:
                return False


def printMatrix(matrix, size):
    for i in range(0, size):
        for j in range(0, size):
            print(matrix[i][j], end="\t")
        print("\n", end="")


def updateMatrix(matrix, action):
    if action == "a" or action == "A":
        for i in range(0, 4):
            for j in range(0, 4):
                getIn()
    elif action == "a" or action == "A":
        for i in range(0, 4):
            for j in range(0, 4):
                getIn()
    elif action == "a" or action == "A":
        for i in range(0, 4):
            for j in range(0, 4):
                getIn()
    elif action == "a" or action == "A":
        for i in range(0, 4):
            for j in range(0, 4):
                getIn()
    else:
        print("You entered a wrong action")
    return matrix


def main():
    size = int(input("enter x times x\n"))
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
    while checkMatrix(matrix):
        action=getAction()
        while(matrix==updateMatrix(matrix,action)):
            action=getAction()
        system("cls")
        printMatrix(matrix, size)


main()
