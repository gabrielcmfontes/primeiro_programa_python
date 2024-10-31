lista_numero = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]

lista_nomes = ['Gabriel', 'Raíssa', 'Maria Fernanda', 'Ana Luisa']

lista_anos = [2005, 2024]

soma_dos_impares = 0

#for numero in lista_numero[::-1]:
#   print(numero)
    
print('Informe um número para que eu imprima a tabuada\n')
tabuada_valor = input("Insira o número desejado: ")
tabuada_valor = int(tabuada_valor)

for numero in lista_numero:
    print(f" {tabuada_valor} x {numero} = {tabuada_valor*numero}")

soma_array = 0

for numero in lista_numero:
    soma_array += numero

print(soma_array)
