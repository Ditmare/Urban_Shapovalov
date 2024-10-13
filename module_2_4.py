numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
i = 0
for i in numbers:
    is_prime = True
    if i < 2:
        continue
    for j in range(2, i - 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
print('Простые числа ', primes)
print('Составные числа', not_primes)
