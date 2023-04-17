# -*- coding : utf-8 -*-

a = input()
a_int = int(a)
sum = 0 

for i in range(1,a_int+1):
    if(i % 2 == 0):
        sum += i     
    
print(sum)
