""" Crie uma lista que guarde as armas do jogo """

""" Lista(Array) """
inventario = ["espada", "poção", "escudo"]

print("inventario 01")
for i in inventario:
    print(i)

print("")

inventario.append("Lança")

print("inventario 02")
for i in inventario:
    print(i)

""" Tupla é imutavel """

valor_ataque = (10, 20)

valor_ataque.append(30)