import random

def generate_sequence(n):
    # Tvůj kód zde
    for x in range(n):
        print(random.randint(1, 100))



# Otestování funkce
generate_sequence(10)  # Vygeneruje 10 náhodných čísel
