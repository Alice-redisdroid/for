numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in range(len(numbers)):
    n = numbers[i]
    is_prime = True

    for divider in range(2, n):
            if (n % divider) == 0:
                is_prime = False
    if is_prime and n != 1:
        primes.append(n)
    elif n != 1:
        not_primes.append(n)

print(primes)
print(not_primes)