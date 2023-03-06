# link para o desafio: https://codeforces.com/problemset/problem/1030/A
import sys
people = input()
asw = input()
aswSplit = asw.split(" ")
for n in aswSplit:
    if n == "1":
        print("HARD")
        sys.exit()
print("EASY")