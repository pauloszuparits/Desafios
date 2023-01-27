# link para o problema : https://codeforces.com/problemset/problem/1772/A

qtdOp = int(input())
if(qtdOp >= 0 and qtdOp <= 100):
    i = 0
    arr = []
    for i in range(qtdOp):
        op = input()
        if op >= 9 and op <= 0:
            arr.append(eval(op))
    for num in arr:
        print(num)

