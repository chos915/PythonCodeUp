# -*- coding : utf-8 -*-

n = int(input())

num = input().split()

temp = num[0]

for i in range(0, n-1):
    for j in range(i+1, n):
        if(int(num[i])>int(num[j])):
            temp=int(num[j])
            num[j]=int(num[i])
            num[i]=temp

print(num[0])