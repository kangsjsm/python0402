def triple(a = 5):
    result = a * 3
    return result
print(triple(2))
print(triple())


# 다수 연산 값 리턴
def cal(a, b):
    return a + b, a - b, a / b, a * b, a % b
print(cal(2, 3))
print(type(cal(2, 3)))

'''
num1 = int(input('첫번째 숫자를 입력하새:'))
num2 = int(input('두번째 숫자를 입력해:'))
print(f'{num1} + {num2} = {num1 + num2}')
print(f'{num1} - {num2} = {num1 - num2}')
print(f'{num1} / {num2} = {num1 / num2}')
print(f'{num1} // {num2} = {num1 // num2}')
print(f'{num1} * {num2} = {num1 * num2}')
print(f'{num1} % {num2} = {num1 % num2}')

'''
