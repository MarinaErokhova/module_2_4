numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes =[] #только простые числа.
not_primes = [] #не простые числа.
for i in range(len(numbers)):
    if numbers[i] == 0 or numbers[i] == 1:
        continue
    count = 0
    for j in range(2, numbers[i] + 1):
        if numbers[i] % j == 0:
            count += 1
    if count > 1:
        not_primes.append(numbers[i])
    else:
        primes.append(numbers[i])
print(primes)
print(not_primes)