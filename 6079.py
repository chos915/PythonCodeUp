# -*- coding : utf-8 -*-

'''
처음 짠 코드
n = int(input())
sum = int(0)

for i in sum:
    sum += i
    i += 1
    if(sum > n):
        break

print(sum)
'''

n = int(input())
sum = int(0)

for i in range(0, 1001):
    i += 1
    sum += i
    if(sum >= n):
        print(i)   
        break
