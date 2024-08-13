# N X N 정사각형
# 1 x 1 크기의 정사각형으로 나누어짐
# 가장 왼쪽 위 좌표 : (1,1) , 가장 오른쪽 아래 좌표 : (N, N)
# 상하좌우 이동 가능
# 시작 좌표: 항상 (1,1)
# 계획서 : 한 줄에 띄어쓰기 기준, LRUD 중 하나의 문자가 반복적으로 적힘
# 정사각형 공간을 벗어나는 움직임은 무시

# 입력
# 첫째 줄 : 공간 크기 N (1<=N<=100)
# 둘째 줄 : 이동 계획서, 이동 횟수는 1이상 100이하
# 출력
# 첫째 줄 : 최종 도착 지점 좌표 X Y

# 1st solution
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def U(pnt):
    if((pnt.x-1) == 0):
        return
    pnt.x-=1

def L(pnt):
    if((pnt.y-1) == 0):
        return
    pnt.y -=1

def D(pnt):
    if((pnt.x+1) == (N+1)):
        return
    pnt.x+=1

def R(pnt):
    if((pnt.y+1) == (N+1)):
        return
    pnt.y+=1


N = int(input())
arr = [[0 for _ in range(N+2)] for _ in range(N+2)]
cur = point(1,1)

plan = input().split(" ")

for p in plan:
    if p == 'L':
        L(cur)
    elif p == 'R':
        R(cur)
    elif p == 'U':
        U(cur)
    elif p == 'D':
        D(cur)
    

print(cur.x, cur.y)



# 2nd solution
N2 = int(input())
plan2 = input().split(" ")
curX, curY = 1, 1
move = ['L', 'R', 'U', 'D'] 
#L,R,U,D를 각각 if(elif)문에 작성하는 방법 개선 - 한 번에 처리 + 함수 작성 불필요 : 각 move type에 맞게 좌표 이동 설정해주면 됨 

#좌표 변화 : 위의 move type에 맞춰서
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for p in plan2:
    for i in range(len(move)):
        if p == move[i]:
            tempX = curX + dx[i]
            tempY = curY + dy[i]

    if tempX < 1 or tempX > N2 or tempY <1 or tempY > N2:
        continue        

    curX = tempX
    curY = tempY

print(curX, curY)

