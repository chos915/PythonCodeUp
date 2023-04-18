# -*- coding : utf-8 -*-

c = int(input())
print(chr(c)) # c에 저장되어 있는 정수 값을 유니코드 문자(character)로 바꿔 출력한다.

'''
입력은 기본적으로 모두 문자열로 입력되는 것이라고 할 수 있다.
따라서, 입력 값이 문자/문자열/정수/실수인지에 따라서 먼저 정확하게 변환시킨 다음에 사용하거나 계산하는 것이 좋다.

예를 들어 123이 입력 되었다고 한다면, 이건 정수일까? 문자열일까? 조금만 생각해보면, 입력된 것만 보고는 그 값이 어떤 데이터인지 알 수 없다는 것을 쉽게 이해할 수 있다.
따라서, 그 입력 값을 어떻게 해석하고 변환할 지에 대해서 명확하게 작성해 주어야 하는 것이다.

chr[]는 정수값->문자, ord()는 문자->정수값 형태로 바꿔주는 서로 반대 방향으로 바꾸어 주는 기능을 한다.
'''