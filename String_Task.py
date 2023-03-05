#  link para o desafio: https://codeforces.com/contest/118/problem/A
string = input().upper()
resp = []
for letter in string:
    if letter == "A" or letter == "O" or letter == "Y" or letter == "E" or letter == "U" or letter == "I":
        continue;
    else:
        resp.append(".")
        resp.append(letter)
    
        
resp2 = "".join(resp)
print(resp2.lower())
    