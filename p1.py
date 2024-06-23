def multiples_3_5(number : int) -> int:
    sum = 0
    for i in range(3, number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum
print(multiples_3_5(49))
