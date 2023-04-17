a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a < b and a < c and a < d:
    print(a, 'the smallest number')
elif b < a and b < c and b < d:
    print(b, 'the smallest number')
elif c < a and c < b and c < d:
    print(c, 'the smallest number')
else:
    print(d, 'the smallest number')
