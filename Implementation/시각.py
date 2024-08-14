#00시 00분 00초 ~ N시 59분 59초 
#3이 하나라도 포함된 시각의 수

#hour부터[0-23] : 3, 13, 23 -> 3개
#3,13,23을 제외한 시간(21개)에 한해 minute[0-59] : 3,13,23,[30-39],43,53 -> 15개
#3,13,23을 제외한 시간 중에서 위의 15개 min들 제외 초로만 카운트 되는 경우[0-59] : 3,13,23,[30-39],43,53 -> 15개

#sol 1
N = int(input())

hourContains3 = [3,13,23]
numOfMinSecContains3 = 15

hourWithout3 = 0
hourWith3 = 0
for i in range(N+1):
    if i in hourContains3:
        hourWith3+=1
    else:
        hourWithout3+=1

numHour3 = hourWith3 * 3600
numMin3 = hourWithout3*numOfMinSecContains3*60
numSec3 = hourWithout3*(60-numOfMinSecContains3)*numOfMinSecContains3

print(numHour3+numMin3+numSec3)


#sol 2 : 완전 탐색
N1 = int(input())

result = 0

for h in range(N1+1):
    for m in range(60):
        for s in range(60):
            if '3' in (str(h)+str(m)+str(s)):
                result+=1

print(result)


