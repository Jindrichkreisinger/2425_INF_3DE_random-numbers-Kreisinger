import random

def roll_multiple_dice(n, k):
    # Tvůj kód zde
    results = []
    sum = 0
    for i in range(n):
        results.append(random.randint(1,6))
        sum += results[i]
    return sum
    

# Otestování funkce
print(roll_multiple_dice(3, 6))  # Simulace hodu 3 kostkami, každá má 6 hran
