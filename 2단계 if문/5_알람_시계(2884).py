H ,M = map(int, input().split())

if 45 <= M <=59:
    print(H, M-45)
elif 0<= M < 45 and 0 < H <= 23:
    print(H-1, 60-(45-M))
elif  0<= M < 45 and H == 0:
    print(23, 60-(45-M))
else:
    pass
