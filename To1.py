N, K = map(int, input().split())



res = 0

while True:
    
    # target : 다음 K로 나누어떨어지는 N의 값
    target = (N//K) * K  # N이 K로 나누어 떨어지지 않더라도 몫에 K값을 곱하면 현재 N과 가장 가까운 K로 나누어떨어지는 값을 찾을 수 있음
    res += (N-target) # 1 빼주는 연산 횟수 바로 계산
    N = target

    if N < K:
        break

    N //= K
    res+=1

res += (N-1)
print(res)



# while N!=1:
#     if N%K == 0:
#         res +=1
#         N //=K
#     else:
#         res +=1
#         N -= 1

# print(res)



# N = 9 -> 8 -> 2 -> 1 

#