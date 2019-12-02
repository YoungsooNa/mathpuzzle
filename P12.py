import decimal

N = 200
decimal.getcontext().prec= N

a = decimal.Decimal(4)**decimal.Decimal(0.5)
n = 2;
while True:
    check = {}
    string = str(decimal.Decimal(n)**decimal.Decimal(0.5))
    min = 0
    count = 0
    for i in string.split('.')[1]:
        count+=1
        if not(i in check.keys()):
            check[i] = 1

        if len(check.keys()) == 10:
            min = count
            break
    if len(check.keys()) == 10 and min <= 10:
        print(n)
        print(string)
        break
    n +=1