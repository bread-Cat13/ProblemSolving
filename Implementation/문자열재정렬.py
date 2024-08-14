#입력 : 알파벳 대문자 + 숫자(0~9)
#출력 : 알파벳 오름차순 + 숫자 더한 값

#숫자가 없을 때를 고려해야 함!

#sol 1
input_data = input()
result =""

alpha_lst = []
num = 0

for data in input_data:
    if data >= 'A' and data <='Z': # data.isalpha()
        alpha_lst.append(data)
    else:
        num+=int(data)

alpha_lst.sort()

for c in alpha_lst: 
    result+=c

if num!=0:
    result+=str(num)

print(result)

#sol 2
input_d = input()
result2 =""

lst = []
value = 0

for data in input_d:
    if data.isalpha(): 
        lst.append(data)
    else:
        value+=int(data)

lst.sort()

result2 = "".join(lst)
result2 = result2+str(value) if value!=0 else result2

print(result2)