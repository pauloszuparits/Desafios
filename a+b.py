# link para o problema : https://codeforces.com/problemset/problem/1772/A
qtdOp = int(input())
i = 0
arr = []
for i in range(qtdOp):
    op = input()
    arr.append(eval(op))
for num in arr:
    print(num)