def largest_prime_factor(n : int) -> int:
    maior_fator = 1
    
    while n % 2 == 0:
        maior_fator = 2
        n //= 2
    
    fator = 3
    while fator * fator <= n:
        while n % fator == 0:
            maior_fator = fator
            n //= fator
        fator += 2
    
    if n > 2:
        maior_fator = n
    
    return maior_fator
    

print(largest_prime_factor(13195))
