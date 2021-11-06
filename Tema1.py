lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(lista)
lista_s = lista.copy()
lista_s.sort()
print("Lista inițială ordonată ascendent: ", lista_s)
print("Lista inițială ordonată descendent: ", lista_s[::-1])
print("Lista ce conține numerele pare din lista ordonată: ", lista_s[1:11:2])
print("Lista ce conține numerele impare din lista ordonată: ", lista_s[0:11:2])
print("Lista ce conține numerele ce sunt multipli ai numărului 3: ", lista_s[2:11:3])