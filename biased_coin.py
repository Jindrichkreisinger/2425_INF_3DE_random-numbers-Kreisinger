import random

def flip_biased_coin(p):
    # Tvůj kód zde
    return random.choice(["heads","tails"])

# Otestování funkce
print(flip_biased_coin(0.7))  # Simulace hodu s 70% šancí na výhru
