# -*- coding: utf-8 -*-
"""Listas 04.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x5HZsWvbOk549D5qB9f6kUaKAhv3BNLz

# Adicionar e Remover itens de uma lista

Adicionar:<br>
lista.append(item)

Remover:<br>
item_removido = lista.pop(indice)<br>
lista.remove(item)

Digamos que você está construindo o controle de produtos da Apple.<br>
E a Apple lançou o IPhone 11 e irá tirar dos seus estoques o IPhone X
"""

produtos = ['apple tv', 'mac', 'iphone x', 'IPad', 'apple watch', 'mac book', 'airpods']

"""## Existem 2 formas de tratar o erro:

1. Criar um if para evitar que ele aconteça

2. Esperar que ele possa acontecer e tratar caso o erro aconteça com:

try:
    tentar fazer
except:
    caso dê errado
"""

