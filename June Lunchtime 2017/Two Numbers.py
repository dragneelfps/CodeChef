t=int(input())
for i in range(t):
    a,b,n = [int(i) for i in input().split()]
    if n%2 == 0:
        print(a//b if a > b else b // a)
    else:
        c = a*2
        d = b
        print(c//d if c > d else d // c) 
