# Cada tipo de dado tem sua classe
# Por ser uma classe, eles tem métodos e propriedades

a = 5
print(type(a))
print(a.to_bytes(8,byteorder='big'))

b = 7.5
print(type(b))
print(b.hex())

c = True
print(type(c))
print(c.real)

d = "minha terra tem palmeiras..."
print(type(d))
print(d.capitalize())