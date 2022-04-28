'''
    Função Anônima
'''

# def funcao(arg, arg2):
#     return arg * arg2

# var = funcao(2, 2)
# print(var)


################################################################

# USANDO função anônima 

# a = lambda x, y: x * y 
# print(a(2,2))

#################################################################

# ORDENANDO LISTA COM EXPRESSÃO LAMBDA

# lista = [
#     ['P1', 13],
#     ['P2', 6],
#     ['P3', 7],
#     ['P4', 50],
#     ['P5', 8],
# ]
#   0     1
# ['P1', 13]
#lista.sort(key=lambda item: item[1]) # para inverter a lista, reverse=True
#print(lista)

# ORDENANDO LISTA COM EXPRESSÃO LAMBDA SEM ALTERAR A LISTA ORIGINAL

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

print(sorted(lista, key=lambda i: i[1]))
print(lista)