import textwrap
s=input()
k=int(input())
b=textwrap.fill(s,k)
a=[]
for i in b.split('\n'):
    a.append(i)
print(a)
