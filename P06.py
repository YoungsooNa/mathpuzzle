count = 0
for i in range(2, 10001, 2):
    n = i*3 + 1
    while(n != 1 and n != i):
        if n % 2 == 0 :
            n /= 2
        else :
            n = n*3 + 1

    if n == i:
        count+=1

print(count)