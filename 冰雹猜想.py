def main():
    number = int(input())
    while number != 1:
        if number % 2 == 1:
            number = number * 3
            number = number + 1
        else:
            number = int(number / 2)
        print(number)
    print("true")


main()
