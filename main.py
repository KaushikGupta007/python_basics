import math
import datetime
import os
import random
import sys

if __name__ == '__main__':

    # Q1
    print("Anything You find cool.")

    # Q2.1
    a, b = 5, 10
    print("Sum:", a + b)

    # Q2.2
    str1, str2 = "Hello", "World"
    print("Concatenated String:", str1 + " " + str2)

    # Q2.3
    num = 42
    print("Concatenated String and Number:", str1 + " " + str(num))

    # Q3.1
    num = -5
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

    # Q3.2
    num = 4
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

    # Q4.1
    for i in range(1, 11):
        print(i, end=" ")
    print("\n")

    # Q4.2
    i = 1
    while i <= 10:
        print(i, end=" ")
        i += 1
    print("\n")

    # Q4.3
    print("Sum from 1 to 100:", sum(range(1, 101)))

    # Q5.1
    numbers = [23, 1, 56, 12, 78]
    print("Largest:", max(numbers), "Smallest:", min(numbers))

    # Q5.2
    dictionary = {"name": "Alice", "age": 25, "city": "Wonderland"}
    key = "age"
    print("Value:", dictionary.get(key, "Key not found"))

    # Q5.3
    numbers = [5, 2, 9, 1]
    print("Ascending:", sorted(numbers))
    print("Descending:", sorted(numbers, reverse=True))

    # Q5.4
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    merged_dict = {**dict1, **dict2}
    print("Merged Dictionary:", merged_dict)

    # Q6.1
    count = 0
    string = "Hello World"
    vowels = "aeiouAEIOU"
    for char in string:
        if char in vowels:
            count += 1
    print("Vowel Count:", count)

    # Q6.2
    print("Reversed String:", string[::-1])

    # Q6.3
    string = "madam"
    if string == string[::-1]:
        print("Palindrome")
    else:
        print("Not a Palindrome")

    # Q7.1
    with open("test.txt", "w") as file:
        file.write("Hello File Handling!")
    with open("test.txt", "r") as file:
        print("File Content:", file.read())

    # Q7.2
    with open("test.txt", "a") as file:
        file.write("\nAppended Text.")
    with open("test.txt", "r") as file:
        print("Updated File Content:", file.read())

    # Q7.3
    with open("test.txt", "r") as file:
        print("Line Count:", len(file.readlines()))

    # Q8.1
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero!")

    # Q8.2
    try:
        num = int(input("Enter a number: "))
        print("Number:", num)
    except ValueError:
        print("Invalid input!")

    # Q8.3
    try:
        print("Trying something risky!")
    finally:
        print("This will always execute.")

    # Q9.1
    random_numbers = []
    for i in range(5):
        random_numbers.append(random.randint(1, 100))

    print("Random Numbers:", random_numbers)

    # Q9.2
    num = random.randint(1, 100)
    if num == 1:
        print(f"{num} is neither prime nor composite")
    else:
        for i in range(2, num):
            if num % i == 0:
                print(f'{num} is composite')
                break
        else:
            print(f'{num} is prime')

    # Q9.3
    print("Rolled Die:", random.randint(1, 6))

    # Q9.4
    numbers = [1, 2, 3, 4, 5]
    random.shuffle(numbers)
    print("Shuffled List:", numbers)

    # Q9.5
    print("Random Choice:", random.choice(numbers))

    # Q9.6
    length = 8
    password = ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=length))
    print("Random Password:", password)

    # Q9.7
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    print("Random Card:", random.choice(ranks), random.choice(suits))

    # Q10.1
    if len(sys.argv) > 2:
        num1, num2 = int(sys.argv[1]), int(sys.argv[2])
        print("Sum of Arguments:", num1 + num2)

    # Q10.2
    if len(sys.argv) > 1:
        print("String Length:", len(sys.argv[1]))

    # Q11.1
    num = 16
    print("Square Root:", math.sqrt(num))

    # Q11.2
    print("Current Date and Time:", datetime.datetime.now())

    # Q11.3
    print("Files in Directory:", os.listdir("."))
