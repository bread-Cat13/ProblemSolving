N, K = map(int, input().split())
coin_lst =[]
for i in range(N):
    coin_lst.append(int(input()))

coin_lst.reverse()

count= 0

for v in coin_lst:
    if v > K:
        continue
    elif K==0:
        break
    count+=(K//v)
    K%=v


print(count)