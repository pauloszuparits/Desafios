# link do desafio: https://codeforces.com/contest/131/problem/A
import sys
palavra = input()
if palavra.isupper():
    print(palavra.lower())
    sys.exit()
contador = 1
while contador < len(palavra):
    if palavra[contador].islower():
        print(palavra)
        sys.exit()
    contador = contador + 1
print(palavra.title())
