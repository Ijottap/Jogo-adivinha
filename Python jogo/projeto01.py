import random

def jogo_de_adivinhacao():
    numero_secreto = random.randint(1,2)
    tentativas = 0
    print("Tente adivinhar um número entre 1 e 50.")

    while True:
        tentativa = int(input("Digite sua tentativa: "))
        tentativas += 1

        if tentativa < numero_secreto:
            print("Tente um número maior.")
        elif tentativa > numero_secreto:
            print("Tente um número menor.")
        else:
            print(f"Parabéns! Você acertou o número secreto em {tentativas} tentativas!")
            break
jogo_de_adivinhacao()


