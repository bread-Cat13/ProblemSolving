# 8 by 8 
# 행 : 1~8
# 열 : a~h


colType = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, -2, -1, 1, 2]



string = input()

curY = colType.index(string[0]) + 1 
#위에 colType을 쓰지 않는 경우 : 아스키코드 사용
#curY = int(ord(input[0])) - int(ord('a')) + 1 
curX = int(string[1]) 


result = 0

for i in range(len(dx)):
    x = curX + dx[i]
    y = curY + dy[i]
    if x<1 or y<1 or x>8 or y>8:
        continue
    result+=1

print(result)