import time
def symetric(string : str) :
    if string == string[::-1]:
        return True
    return False

start_time = time.time()
for n in range(11, 1000, 2):
    dec_s = str(n)
    bin_s = bin(n).split('b')[1]
    oct_s = oct(n).split('o')[1]

    if(symetric(dec_s) and symetric(bin_s) and symetric(oct_s)):
        print(n)
        break

end_time = time.time()

print(end_time - start_time)