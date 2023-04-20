# -*- coding : utf-8 -*-

# 부른 번호의 횟수
n = int(input())

# 공백을 두고 분리하여 저장
num = input().split()

count = int(0)

for i in range(1, 24):
    count = int(0)
    for j in range(0, n):
        if(int(num[j])==i):
            count += 1
    print(count, end=' ')
            

    
    
    

