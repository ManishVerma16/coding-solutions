n = int(input())
array = list(map(int, input().split()))
array.sort()
if n % 2 == 0:
    mid = array[int(n/2)]
else:
    mid = array[int(n/2)+1]
array.reverse()
print(array[0],mid,array[n-1])