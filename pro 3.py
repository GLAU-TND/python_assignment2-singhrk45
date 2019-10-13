def minRemove(a, n):
    list1 = [0 for i in range(n)]
    lh = 0
    for i in range(n):
        list1[i] = 1
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j] and (i - j) <= (a[i] - a[j]):
                list1[i] = max(list1[i], list1[j] + 1)
        lh = max(lh, list1[i])
    return n - lh


a = list(map(int, input().split(",")))
n = len(a)
res = int(minRemove(a, n))
if res == 1:
    print(True)
elif res == 0:
    print("Already Non-Decreasing in Nature.")
else:
    print(False)
