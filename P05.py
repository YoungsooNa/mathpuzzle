"""
동전 종류 10, 50, 100, 500
1000원 넣었을 때 나오는 동전의 조합이 몇가지인지 구하기
재귀함수로 구하는게 가장 간단할 거 같다.
"""

coin = [500, 100, 50, 10]

def coin_combination(n, coin_list, use_list, level):
    way = 0
    copy_list = use_list.copy()

    while(True) :
        copy_list[level] += 1
        sum = 0;
        for i in range(len(coin_list)):
            sum += coin_list[i] * copy_list[i]

        if sum == n:
            print(copy_list)
            return way+1
        elif sum > n:
            break
        else:
            if level < 3:
                way += coin_combination(n, coin_list, copy_list, level+1)

    return way

print(coin_combination(1000, coin, [0,0,0,0], 0))