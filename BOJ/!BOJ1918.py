# 중위표기식을 후위표기식으로 변경하기
# ex) A * (B + C) ---> ABC+*

# 문제해결방법
# 1. 피연산자가 들어오면 바로 출력한다
# 2. 연산자가 들어오면 자기보다 우선순위가 높거나 같은 것들을 빼고 자신을 스택에 담는다.
# 3. 여는 괄호를 만나면 무조건 스택에 담는다.
# 4. 닫는 괄호를 만나면 여는 괄호를 만날 때까지 스택에서 출력한다.

# A + B * C 일경우 --> ABC*+

# 예외적인 상황
# 1. 뒤쪽에 위치한 연산자보다 앞쪽에 위치한 연산자의 우선순위가 크거나 같은 경우
# -> 스택의 맨 위에 위치한 연산자의 우선 순위가 지금 연산자보다 
# -> 우선순위가 작아질때까지 pop 하며 결과로 출력한 뒤에 지금의 연산자를 push

import sys

stack = []  # 연산자      * ( + )

result = [] # 결과값

cmd = sys.stdin.readline().rstrip()

for i in cmd:
    if 'A' <= i <= 'Z':       # 피연산자를 결과값으로
        result.append(i)
    
    elif i == '(':
        stack.append(i)
    
    elif i == ')':
        while stack != '(': # stack 맨위나 아래가 
            result.append(stack.pop())
        stack.pop() # 여는 괄호 pop

    elif i == '+' or i == '-':
        if not stack:  # 비어있으면 push
            stack.append(i)
        else:
            while stack in ['*','/']:
                result.append(stack.pop())
            stack.append(i)

    elif i == '*' or i == '/':
        if not stack:
            stack.append(i)

        else:
            while stack in ['*','/']:
                result.append(stack.pop())
            stack.append(i)

for _ in range(len(stack)):
    result.append(stack.pop())

for j in result:
    print(j,end='')
