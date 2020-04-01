t = int(input())
while t > 0:
    n, k = map(int, input().split())
    arrayA = list(map(int, input().split()))
    seconds = [0]
    for i in arrayA:
        if i <= k:
            seconds.append(k-i)
    print(max(seconds))
    t -= 1