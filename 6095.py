# -*- coding : utf-8 -*-


values = []
n = int(input())
i = int(0)

while i!=n:
    x,y = input().split()
    values.append((int(x), int(y))) # x, y값을 정수형으로 변환하여 저장
    i+=1


for i in range(1, 20):
    for j in range(1, 20):
        if (i, j) in values: # (i, j)가 입력받은 값들의 좌표에 있으면 1을 출력
            print(1, end=' ')
        else:
            print(0, end=' ')
    print() # 행이 바뀔 때에만 줄바꿈을 출력

 