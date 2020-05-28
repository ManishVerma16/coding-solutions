from itertools import product

def iterProduct(a, b):
    result = list(product(a, b))
    string =  ' '.join(str(i) for i in result) 
    print(string)
        

a = list(map(int,input().split()))
b = list(map(int,input().split()))
iterProduct(a, b)