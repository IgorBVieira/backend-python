# Variáveis

print('Variáveis')
a = 10 # Global
nome = 'Joaquim' # Local
print(a)
print(nome)
print('--------------------------------------')

# Loops

print('**For Loop**')
listContador = []
for contador in range(10): # A função range gera uma lista de 0 a 9 do tipo int
    listContador.append(contador)
print(listContador)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

notas = [5.3, 7.5, 9.8, 10]
for nota in notas:
    print(f'suas notas são {nota}') # f-string | interpolação de strings
print('--------------------------------------')

print('**While Loop**')
print("Informe as notas. Ao terminar informe *")
media = 0.0
contagem = 0
s = input()
while s != "*":
	contagem += 1
	media += float(s) # Variável lida é sempre string!
	s = input()
print(f"A média é {media / contagem}")
print('--------------------------------------')

# Funções

print('**Funções**')
def hello(name):
    print(f'Hello, {name}!')
    
hello('Joaquim')
print('--------------------------------------')
