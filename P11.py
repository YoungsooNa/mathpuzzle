a = 1
b = 1
c = 2
n = 0
def sumOfEach(string : str) :
    sum = 0;
    for c in string:
        sum += int(c)
    return sum
while True:
    c = a + b
    a = b
    b = c

    if c % sumOfEach(str(c)) == 0 :
        print(c)
        n+=1

    if n == 11:
        break
