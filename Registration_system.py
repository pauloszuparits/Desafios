# link para o desafio: https://codeforces.com/problemset/problem/4/C
aux = int(input())
lista = []
listaAux = []
cont = 0
for i in range(aux):
    user = input()
    user2 = user
    if user in listaAux:
        cont = listaAux.count(user)
        user2 = user + str(cont)
        lista.append(user2)
    else:
        lista.append("OK")
    listaAux.append(user)
for name in lista:
    print(name)