# Importando a biblioteca sys
# Permite acessar os argumentos passados na linha de comando
# Exemplo: python notes.py 1 2 3 4 5
import sys

# Criando uma lista de notas
notas = list(map(int,sys.argv[1:]))

# Calculando as novas notas
# Faz uma iteração da lista de notas e calcula as novas notas
novas = [(lambda ng: ((int(ng/5)+1)*5) if ng > 60 and ((int(ng/5)+1)*5) \
- ng < 3 else ng)(ng) for ng in notas]

# Imprimindo as novas notas
print(novas)