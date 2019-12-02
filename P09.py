"""
A string consist of word 20 m and 10 w
Find a order of string that
Even if split the one point of string can't make number of m and n equals at least in one part.


points = 30 > 2n > 0
w_1 = k < 10 and k < points
m_1 = points - w_1
w_2 = 10 - w_1
m_2 = 20 - m_1

"""
count = 0;
for point in range(2, 30, 2):
    for w_1 in range(1, 10):
        if w_1 > point :
            break

        m_1 = point - w_1

        if m_1 != w_1 :
            count+=1
        else :
            m_2 = 20 - m_1
            w_2 = 10 - w_1

            if m_2 != w_2:
                count+=1

print(count)

