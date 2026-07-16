import random

numero_secreto = random.randint(1, 10)

for intento in range(3):
    guess = int(input("Adivina: "))

    if guess == numero_secreto:
        print(f"🎉 ¡Adivinaste en el intento {intento + 1}!")
        break
    elif guess < numero_secreto:
        print("⬆️ El número secreto es mayor")
    else:
        print("⬇️ El número secreto es menor")
else:
    # Este "else" del for se ejecuta solo si NO hubo break
    print(f"😢 Perdiste, el número era {numero_secreto}")
