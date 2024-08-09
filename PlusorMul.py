numStr = input()

res = 0
for s in numStr:
    num = int(s)
    if res <= 1 or num <=1:
        res += num
    else:
        res *= num

print(res)