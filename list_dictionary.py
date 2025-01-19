import random


def is_prime(n):
    if n <= 1:
        return False
    for j in range(2, n):
        if n % j == 0:
            return False
    return True


if __name__ == '__main__':

    # Q1
    L = [10, 20, 30, 40, 50, 60, 70, 80]

    # Q1 i
    L.extend([200, 300])
    print(L)

    # Q1 ii
    L.remove(10)
    L.remove(30)
    print(L)

    # Q1 iii
    L.sort()
    print(L)

    # Q1 iv
    L.sort(reverse=True)
    print(L)

    # Q2
    scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)

    # Q2 i
    highest_score = max(scores)
    highest_index = scores.index(highest_score)
    print(highest_score, highest_index)

    # Q2 ii
    lowest_score = min(scores)
    lowest_count = scores.count(lowest_score)
    print(lowest_score, lowest_count)

    # Q2 iii
    reversed_list = list(scores[::-1])
    print(reversed_list)

    # Q2 iv
    score_to_check = 76
    if score_to_check in scores:
        print(scores.index(score_to_check))
    else:
        print("Not present")

    # Q3
    numbers = []
    for i in range(100):
        numbers.append(random.randint(100, 900))

    # Q3 i
    odd_numbers = [num for num in numbers if num % 2 != 0]
    print(len(odd_numbers), odd_numbers)

    # Q3 ii
    even_numbers = [num for num in numbers if num % 2 == 0]
    print(len(even_numbers), even_numbers)

    # Q3 iii
    prime_numbers = [num for num in numbers if is_prime(num)]
    print(len(prime_numbers), prime_numbers)

    # Q4
    A = {34, 56, 78, 90}
    B = {78, 45, 90, 23}

    # Q4 i
    print(A | B)

    # Q4 ii
    print(A & B)

    # Q4 iii
    print(A ^ B)

    # Q4 iv
    print(A.issubset(B), B.issuperset(A))

    # Q4 v
    X = int(input("Enter a score to remove from A: "))
    if X in A:
        A.remove(X)
        print(A)
    else:
        print("Not present")

    # Q5
    dictionary = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
    dictionary["location"] = dictionary.pop("city")
    print(dictionary)
