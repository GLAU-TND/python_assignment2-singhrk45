a = list(map(int, input().split(",")))
k = int(input())
m = []
total = 0
diff = 0
a.sort()
for i in range(0, len(a)):
    total += a[i]
    m.append(a[i])
    if total >= k:
        break
if total == k:
    print(m)
else:
    diff = total - k
if diff in a:
    m.remove(diff)
    m.sort()
    print(m)
elif diff not in a:
    print("None")
