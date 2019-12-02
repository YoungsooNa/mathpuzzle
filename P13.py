import itertools
"""

READ + WRITE + TALK = SKILL

R != 0
E
A
D
W != 0
I
T != 0
L
K
S != 0

READ + WRITE = SKI0L - TA0K

"""
not_zero = ['R', 'W', 'T', 'S']
pool = ['A', 'D', 'E', 'R', 'W', 'I', 'T', 'L', 'K', 'S']
WORDS = ["READ", "WRITE", "SKILL", "TALK"]

count = 0
for case in list(map(''.join, itertools.permutations(pool))):
    if case[0] in not_zero:
        continue
    n = 0
    value = {}
    for c in case:
        value[c] = n
        n+=1

    values = []

    for index, word in enumerate(WORDS):
        n = 0
        values.append(0)
        for c in reversed(word):
            values[index] += value[c] * (10**n)
            n += 1

    if values[0] + values[1] == values[2] - values[3] :
        print(values)
        count += 1

print(count)

