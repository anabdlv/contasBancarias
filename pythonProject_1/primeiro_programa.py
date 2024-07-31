'''
s = ("Hello world")
num = 10
print(s)
print(num)

###

numero = eval(input('Entre com um número inteiro: '))
numero += 2
print(numero)

###

nome = input('Entre com seu nome: ')
print(nome)

###

peso = eval(input('Infome seu peso: '))
altura = eval(input('Infome sua altura: '))

imc = peso/(altura**2)

print('IMC: ', imc)

###

hora = 10
minutos = 26
segundos = 18

print(str(hora) + ':' + str(minutos) + ':' + str(segundos))

###

hora = 10
minutos = 26
segundos = 18

print('{}:{}:{}'.format(hora, minutos, segundos))

###

hora = 10
minutos = 26
segundos = 18

print(f'{hora}:{minutos}:{segundos}')

###

print('{:4},{:5}'.format(10,100))

###

str = 'Hello World'
print(str[0:4])
print(str[2:8])

###

str = 'Hello World'
print(str[::-1])
print(str[8:2:-1])

###

num = eval(input('Informe um número: '))
resto = num % 2
if(resto==0):
    print('O número é par')
else:
    print('O número é ímpar')

###

nota = eval(input('Informe sua nota: '))

if(nota>=7):
    situacao = 'O aluno está aprovado'
elif(nota>=5):
    situacao = 'O aluno está em recuperação'
else:
    situacao = 'O aluno está reprovado'

print(situacao)

###

preco_unitario = 10
desconto10 = 0.1
desconto20 = 0.2
quantidade = eval(input('Informe a quantidade de itens: '))

if(quantidade<=10):
    valor_final = preco_unitario*quantidade
elif(quantidade<=20):
    valor_final = preco_unitario*quantidade*(1-desconto10)
else:
    valor_final = preco_unitario*quantidade*(1-desconto20)

print(f'O valor final da compra é {valor_final}')

###

lista = [10, 2, 5, 7, 6, 3]
n=len(lista)
soma=0
for i in range(n):
    if(lista[i]%2==0):
        soma=soma+lista[i]
print(f'O somatório dos elementos pares da lista é {soma}')

lista = [10, 2, 5, 7, 6, 3]
soma=0

for num in lista:
    if(num%2==0):
        soma=soma+num
print(f'O somatório dos elementos pares da lista é {soma}')

###

while True:
    palavra = input('Entre com uma palavra: \n')
    if palavra == 'sair':
        break
print('Você digitou sair e agora está fora do laço')

###

def encontrar_minimo(lista):
    minimo = lista[0]
    for elem in lista:
        if(elem < minimo):
            minimo = elem

    return minimo

lista_teste = [12, 378, 45, 98, 22]
menor = encontrar_minimo(lista_teste)
print("O menor elemento da lista é: {}".format(menor))

###

def ePar(n):
    r = (n%2==0)
    return r
def somaPares(lista):
    soma = 0
    for elem in lista:
        if (ePar(elem)):
            soma = soma + elem
    return soma

lista_teste = [10, 1, 12, 3]
somatorio = somaPares(lista_teste)
print(f'A soma dos números pares é {somatorio}')

###

def fatorialIterativo(num):
    f = 1
    for i in range(1,num+1):
        f=f*i
    return f

def fatorialRescursivo(num):
    if((num==0) or (num==1)):
        return 1
    return num*fatorialRescursivo(num-1)

numero = 5

print(f'O fatorial de {numero} é: {fatorialIterativo(numero)}')
print(f'O fatorial de {numero} é: {fatorialRescursivo(numero)}')

###

def numeroPrimo(n):
    if(n<2):
        return False
    i=n//2
    while(i>1):
        if(n%i==0):
            return False
        i -= 1
    return True

def imprimirResultado(numero, resultado):
    mensagem= f'O número {numero} NÃO é primo'
    if(resultado):
        mensagem = f'O número {numero} é primo'
    return mensagem

numero = 8
resultado = numeroPrimo(numero)
msg = imprimirResultado(numero,resultado)
print(msg)'''

###






