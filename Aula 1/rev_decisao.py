"""

    Crie uma aplicação que de 100 vidas a um jogador,
    e verifique se: o jogador tiver 0 vidas informe game over
                o jogador tiver 100 vidas informe o jogador está vivo.
"""

""" Variavel """
vida = 0

if vida == 0:
    print("Game Over")
elif vida == 50:
    print("Você só tem 50% de vida")
else:
    print("Jogador Vivo")