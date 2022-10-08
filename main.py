from math import gcd
from random import randint

def eratosthenes(a, n):
    res = []
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(2*i, len(sieve), i):
                sieve[j] = 0
    for i in sieve:
        if a <= i and i != 0:
            res.append(i)
    return res


def eiler(n):
    a = []
    for i in range(n):
        if gcd(i, n) == 1:
            a.append(i)
    return len(a)

def choice():
    print("\n[1] - задати значення m")
    print("[2] - a mod m")
    print("[3] - a^b mod m")
    print("[4] - ax ≡ b mod m")
    print("[5] - випадкове просте число [A; B]\n")
    key = int(input())
    return key


def first():
    print("\nВведіть значення m:")
    m = int(input())
    return m


def second(m):
    print("\nВведіть значення а:")
    a = int(input())
    return a % m


def third(a, b, m):
    binary = reversed(str(bin(b))[2:])
    c = 1
    c_more_one = False
    for i in binary:
        if i == "1":
            a = a * c % m
        if c_more_one:
            c = c * c % m
        else:
            c = a*a % m
        c_more_one = True
    return a


def fourth(m):
    print("\nВведіть значення а:")
    a = int(input())
    print("Введіть значення b:")
    b = int(input())
    if gcd(a, m) != 1:
        return None
    return b * third(a, eiler(m)-1, m) % m


def fifth(a, b):
    prime_nums = eratosthenes(a, b)
    return prime_nums[randint(0, len(prime_nums)-1)]


m = 1
while True:
    key = choice()
    if key == 1:
        m = first()
    elif key == 2:
        print(f"a mod m = {second(m)}")
    elif key == 3:
        print("\nВведіть значення а:")
        a = int(input())
        print("Введіть значення b:")
        b = int(input())
        print(f"a^b mod m = {third(a, b, m)}")
    elif key == 4:
        result = fourth(m)
        if not result:
            print("Необхідно ввести взаємнопрості a та m (НСД(а, m) = 1)")
        else:
            print(f"x = {result}")
    elif key == 5:
        print("\nВведіть значення а:")
        a = int(input())
        print("Введіть значення b:")
        b = int(input())
        print(f"Випадкове просте число [{a}; {b}] - {fifth(a,b)}")
