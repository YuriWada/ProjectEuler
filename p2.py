def fibonacci(n : int) -> int:
    a, b = 0, 1
    soma_pares = 0
    
    for _ in range(n):
        if a % 2 == 0:
            soma_pares += a
        a, b = b, a + b
    
    return soma_pares
    
print(fibonacci(10))
