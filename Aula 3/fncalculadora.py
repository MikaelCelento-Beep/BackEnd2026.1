
""" Passagem de parametro é quando enviamos informações para a função, de forma que ela possa executar sua tarefa """

#Criamos a função
def calculo(valor_um, operador, valor_dois):
    if operador == "+":
        resultado = valor_um + valor_dois
        return resultado
    elif operador == "-":
        resultado = valor_um + valor_dois
        return resultado
    elif operador == "*":
        resultado = valor_um * valor_dois
        return resultado
    elif operador == "/":

        #Evita o erro da divisão por zero

        if valor_dois == 0:

            mensagem = "Não é possível divisão por zero"
            return mensagem
            """ Não existe divisão por zero """
        else:
            resultado = valor_um / valor_dois
            return resultado
        
#Programação:

#Para a programação utilize a função padrão main


#Utilizar a função main (Principal)
def main():
    print(17*"=")
    print("Bem VIndo(a) a calculadora do Python")
    print(17*"=")

    numero_um = int(input("Informe o primeiro valor: "))
    op = input("Informe a operação [+] [-] [*] [/]: ")
    numero_dois = int(input("Informe o segundo valor: "))

    print(f"O resultado é: {calculo(numero_um, op, numero_dois)}")

main()
