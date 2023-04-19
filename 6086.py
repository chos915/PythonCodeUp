# -*- coding : utf-8 -*-


N = int(input())

sum = int(0)

for i in range(1,N+1):
    sum += i
    if(sum >= N):
        print(sum)
        break