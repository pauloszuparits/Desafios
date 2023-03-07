# link para o desafio: https://codeforces.com/contest/158/problem/B
aux = input()
n = input().split(" ")
soma = 0
for num in n:
    soma = soma + int(num)
if(soma%4 > 0):
    print(int(soma/4+1))
else:
    print(int(soma/4))