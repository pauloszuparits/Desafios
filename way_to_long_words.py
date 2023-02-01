# link https://codeforces.com/problemset/problem/71/A
qtdOp = int(input())
i = 0
arr = []

for i in range(qtdOp):
    word = input()
    tam = len(word)
    if tam > 10:
        word = list(word)
        firstLet = word[0]
        lastLet = word[tam -1]
        tam2 = tam - 2
        word2 = []
        word2.append(firstLet)
        word2.append(str(tam2))
        word2.append(lastLet)
        word3 = ''.join(word2)
        arr.append(word3)
    else:
        arr.append(word)
for w in arr:
    print(w)