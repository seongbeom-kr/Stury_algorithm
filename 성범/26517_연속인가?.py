k = int(input())
a,b,c,d = map(int, input().split())

def fx(a,b,k):
    return a*k+b

if(fx(a,b,k)==fx(c,d,k)):
    print("Yes",fx(a,b,k))
else:
    print('No')