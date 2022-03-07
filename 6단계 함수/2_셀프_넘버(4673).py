a = list(range(1, 10000+1))
def d():
    b = [] 
    for i in range(1, 10000):
        if i < 10:                                                    #if문 안에 if문 한 번더 없어도 될 것 같음
            if i*2 in a:
                b.append(i*2)
        elif i < 100:
            if i + i//10 + i%10:                                             #원본 숫자 + 10의 자리 숫자 + 1의 자리 숫자
                b.append(i + i//10 + i%10)                   
        elif i < 1000:
            if i + i//100 + (i//10)%10 + i%10:                               #원본 숫자 + 100의 자리 숫자 + 10의 자리 숫자 + 1의 자리 숫자
                b.append(i + i//100 + (i//10)%10 + i%10)
        elif i < 10000:
            if i + i//1000 + (i//100)%10 + (i//10)%10 + i%10:                #원본 숫자 + 1000의 자리 숫자 + 100의 자리 숫자 + 10의 자리 숫자 + 1의 자리 숫
                b.append(i + i//1000 + (i//100)%10 + (i//10)%10 + i%10)
    return b

c = d()
c = set(c)
for x in a:
    if x not in c:
        print(x)
