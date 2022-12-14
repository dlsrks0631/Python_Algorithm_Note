'''
A,B 두 사람이 볼링을 치고 있습니다. 두 사람은 서로 무게가 다른 볼링공을 고르려고 한다.
볼링공은 총 N개가 있으며 각 볼링공마다 무게가 적혀 있고, 공의 번호는 1번부터 순서대로 부여된다.
같은 무게의 공이 여러 개 있을 수 있지만, 서로 다른 공으로 간주한다. 볼링공의 무게는 1부터 M까지의 자연수 형태로 존재

< 아이디어 >
1. 파이썬에 내장된 조합 라이브러리를 이용해 2개를 뽑을 수 있는 조합을 구한 뒤
   서로 무게가 다르면 결과값을 하나씩 추가하는 걸로 문제를 풀었다.

2. 무게마다 볼링공이 몇 개가 있는지 계산한 뒤 A가 특정한 무게의 볼링공을 선택했을 때,
   이어서 B가 볼링공을 선택하는 경우를 차례대로 계산하여 문제를 풀었다.

'''
##### 1번 방법 #####

import itertools

n,m = map(int,input().split())
data = list(map(int,input().split()))

result = 0

for x in itertools.combinations(data,2):
    if x[0] != x[1]:
        result += 1

print(result)

##### 2번 방법 #####

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0

# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1,m+1):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱하기

print(result)