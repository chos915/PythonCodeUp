# -*- coding : utf-8 -*-

n = int(input())


for i in range(1, n+1):
    if(i < 10):
        # 일의 자리
        l = int(i % 10)
    
        if(l != 0 and l % 3 == 0):
            print('X', end =' ')
        else:
            print(i, end = ' ')
    
    if(i >= 10):
        # 십의자리
        m = int(i / 10)

        # 일의 자리
        l = int(i % 10)
    
        if(m % 3 == 0):
            print('X', end =' ')
        elif(l != 0 and l % 3 == 0):
            print('X', end = ' ')
        else:
            print(i, end = ' ')

    
