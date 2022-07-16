'''Universidade cruzeiro do sul
   Bruno Gonçalves de souza
   09/05/2022
   07 – Escreva um programa que exiba a tabuada do
   número digitado, onde o usuário possa escolher o inicio
   e o fim da tabuada.'''

tabuada = int(input("Digite a tabuada desejada: "))

start = int(input("Digite o inicio desejado: "))
end = int(input("Digite o fim desejado: "))
step = 1

while (start <= end):
    print(f"{tabuada} x {start} = {tabuada * start}")
    start = start + step

