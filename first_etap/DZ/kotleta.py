k = int(input())
m = int(input())
n = int(input())
if n<=k:
    print(m*2, 'минут - наименьшее время')
else:
    print(-1 * n // k * (-1) * m * 2, 'минут - наименьшее время')