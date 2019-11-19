#somt

a = 10
"""
길이 n의 한 막대를 1 단위로 자른다고 하자, 단 하나의 막대는 한 번에 한 사람만이 자를 수 있습니다.
잘린 막대가 3개가 되면 동시에 3명이 자를 수 있습니다.
최대 m명이 있을 때 막대를 자르는 최소 횟수를 구해 보세요 ( 모든 막대의 길이가 1이 되게 하는 횟수)

일단 무조건 반으로 자르는게 좋아보인다. = 최대한 많은 인원을 투입할 수 있게 각 막대가 생존하는 시간을 맞춰줘야 
문제는 막대의 개수가 투입 인원보다 많을 경우 나머지 막대는 쉬어야 된다.
막대의 크기가 1이 되면 건들 필요 없다.
한명이 자르는데 한 clock에 m 번 작업할 수 있다고 해도 똑같을거 같다.
"""

n = 100
m = 5

b_tree = []
b_tree.append(n)
clock = 0
while(True):
    job = []
    for i in range(len(b_tree)):
        if b_tree[i] > 1 :
            job.append(i)
    if (len(job) == 0) :
        break;
    new_tree = []
    for i in range(min(len(job), m)):
        todo = b_tree[job[i]]
        if todo % 2 == 0:
            new_tree.append(todo/2)
            new_tree.append(todo/2)
        else :
            new_tree.append((todo-1)/2)
            new_tree.append((todo+1)/2)

    if len(job) > m :
        for i in range(0, len(job) - m) :
            new_tree.append(b_tree[job[i+m]])

    b_tree = new_tree
    print(b_tree)
    clock += 1


print(clock)