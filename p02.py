import time

def symetric(string : str, string2) :
    if string == string2[::-1]:
        return True
    return False

"""
4자리 수이므로 0x0x0x0
들어갈 수 있는 곳은 3곳 연산자는 4개 + 없는 경우 1 이므로 총 5^3 125가지 경우의 수를 모두 계산하는 것이
간단하다. 좀 더 고려해보면 최적화가 가능하겠지만 일단 단순하게 풀어보자
for문 3개로 하는건 너무 더러울거 같다. 000 001 002 003 ~ 443 의 형태의 경우가 있다. (444는 연산자가 하나도 없으므로 빼야 된다)
k = 0 부터 123까지 증가시키고 int(k/25)%5 int(k/5)%5 k % 5 로 인덱스를 할당하면 될 것 같다.
eval 에서 예외처리로 넘기는 것은 ... 좀 그렇긴 해보인다.
"""
op = ['+', '-', '*', '/', '']

start_time = time.time()
for i in range(1001, 10000, 2):
    for k in range(0, 5**3-1):
        num_s = str(i)
        exp = num_s[0] + op[int(k/25)%5] + num_s[1] + op[int(k/5)%5] + num_s[2] + op[k%5] + num_s[3]
        try :
            exp_s = str(eval(exp))
        except :
            continue
        if(symetric(num_s, exp_s)) :
            print(str(i) + ' -> ' + exp +' = ' + exp_s)

end_time = time.time()

print(end_time - start_time)