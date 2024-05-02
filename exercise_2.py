def is_prime(number):

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

number = int(input("Enter a number from 2 to 1000: "))
result = is_prime(number)
print(result)