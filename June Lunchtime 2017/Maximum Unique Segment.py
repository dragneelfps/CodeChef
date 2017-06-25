# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    d = [-1 for i in range(n)]
    c = [int(i) for i in input().split()]
    w = [int(i) for i in input().split()]
    start = 0
    sm = 0
    maxsum = 0
    k = 0
    while k < n:
        if d[c[k]] == -1 or d[c[k]] < start:
            d[c[k]] = k
            sm += w[k]
            k += 1
        else:
            sm = 0
            start = d[c[k]] + 1
            for j in range(start,k):
                sm += w[j]
        maxsum = sm if sm > maxsum else maxsum
    print(maxsum)
    
        
