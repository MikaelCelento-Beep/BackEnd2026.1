""" Estudo de Caso: Loja de Games """


#Declarar as listas
jogos = ["Minecraft", "GTA V", "FIFA", "Tekken8", "Street Fighter V"]
valores = [80, 120, 90, 110, 85]

total = 0

for i in range(len(jogos)):
    print(i, "-", jogos[i], "- R$", valores[i])

#Usúario seleciona
for i in jogos:
    escolha = int(input("Escolha o jogo: [0] [1] [2] [3] [4]"))
    total += valores[escolha]

    seguir = input("Deseja escolher outro jogo? [s] [n]").lower()

    if seguir in ["s", "sim"]:
        continue
    else:
        break
if total >= 200:
    desconto = total * 0.10
    total -= desconto
    print("desconto aplicado!")

print(f"Total Final: R${total:.2f}")