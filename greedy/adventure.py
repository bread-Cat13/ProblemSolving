#공포도가 n인 사람은 n명 이상의 그룹에 포함해야 됨. 


'''
입력 예시: 
N
n n n n n .. n (N개)
'''


N = int(input())
fear_lst = list(map(int, input().split()))

fear_lst.sort()

numOfGroup = 0
group = 0
for fear in fear_lst:
    group +=1
    if fear <= group:
        numOfGroup+=1
        group = 0
        
print(numOfGroup)
