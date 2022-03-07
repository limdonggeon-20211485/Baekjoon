# 1.    
def solution(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i]*b[i])
    return sum(c)



# 2.
solution = lambda x, y: sum(a*b for a, b in zip(x, y))\



# 3.
def solution(a, b):
    return sum(map(lambda i: a[i]*b[i], range(len(a))))