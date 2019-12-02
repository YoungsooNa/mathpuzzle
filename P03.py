import time

"""
간단하게 구현하라고 하였으므로 그냥 간단하게 구해보겠다.
"""

# 0 is back 1 is front
cards = [0] * 100

for i in range(2, 101):
    for k in range(i, 101, i):
        cards[k-1] = 1 if cards[k-1] == 0 else 0

for i in range(0, 100):
    if cards[i] == 0:
        print(i+1)

"""
더 간단한 해법
짝수 번 뒤집는 카드를 찾으면 되는데 이는
약수가 1을 제외하고 짝수개 있는 수를 찾으면 된다
근데 제곱수가 약수가 홀수개인건 어떻게 아는거지?
"""