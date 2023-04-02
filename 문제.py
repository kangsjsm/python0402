'''
print(f'1276000 // 24 = {1276000 // 24}원')


a = 'EVERLAND'
b = a[4 : 6]
c = a[1 : 3]
d = a[-2 : ] 
e = a[2 : 4]
print(b + c + d + e)


의자 = 6
테이블 = 2
print(f'내 방에는 의자 {의자}개가 있다') 
print(f'내 방에는 테이블 {테이블}개가 있다')


a = ['e', 'b', 'd', 'a', 'c']
a.sort(reverse = True) 
print(a)


a = []
a.extend([1, 2, 3, 4])
print(a)
a.remove(1)
a.remove(2)
a.remove(3)
print(a)


id = 'ilovepython'
pw = 'mypass1234'
s = input('아이디를 입력하시오: ')
a = input('패스워드를 입력하시오: ')
if s == id :
    if a == pw :
        print('환영합니다.')
    else:
        print('비밀번호가 틀렸습니다.')
else:
    print('아이디가 틀렸습니다.')



sum = 0
answer = 'yes'
while answer == 'yes':
    number = int(input('숫자를 입력하시오: '))
    sum = sum + number
    answer = input('계속?(yes / no):')
print(f'합계는 {sum}')

    
'''
population = ['Seoul', 9765, 'Busan', 3441, 'Incheon', 2954]
print(f'서울 인구: {population[1]}')
print(f'인천 인구: {population[5]}')
print(f'도시 리스트: {population[ :  : 2]}')
c = population[ 1] + population[3] + population[5]
print(f'인구의 합: {c}')

