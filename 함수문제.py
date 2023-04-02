#221 슬라이싱 (reverse, sort는 리스트)
def print_reverse(string):
    print(string[ : : -1])
print_reverse('python')

a = [1, 2, 3, 4, 5]
a.reverse()
print(a)

b = [1, 2, 3, 4, 5]
c = reversed(b)
print(list(b))






#222
def print_score([a, b, c]):
    return (a + b + c)/3
print(print_score(1, 2, 3))

'''
#223
def print_even([
'''
