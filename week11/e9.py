import random

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

random.shuffle(alfabeto)

letra_escolhida = random.choice(alfabeto)

print("Lista embaralhada com índices:")
for i, letra in enumerate(alfabeto):
    print(f"{i}: {letra}")

palpite = int(input(f"\nEm qual posição está a letra '{letra_escolhida}'? "))

if alfabeto[palpite] == letra_escolhida:
    print("Você acertou.")
else:
    print(f"Você errou.")
