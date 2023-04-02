# 1~10까지의 합계를 함수로 작성!

def get_sum(start, end):
    sum = 0
    for i in range(start, end + 1):
        sum = sum + i
    return sum
print(get_sum(1, 10))

