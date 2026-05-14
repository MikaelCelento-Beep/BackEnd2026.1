def media(n1, n2):
    return (n1 + n2) / 2

resultado = media(7,8)

print(resultado)

def multiplicar(num1, num2):
    return (num1 * num2)

resultado2 = multiplicar(2,5)

print(resultado2)

def descontos_10(preco,porcentagem):
    #Calcula quanto é 10% do valor da compra
    desconto = preco * 0.10
    return (preco - desconto)

valor = int(input("Informe o valor da sua compra: "))
print("Aplicando cupom de desconto...")

valor_desconto = descontos_10(valor)

print(f"Desconto aplicado! Valor a pagar R${valor_desconto:.2f}")