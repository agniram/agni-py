n, m = [int(i) for i in input().split()]

a=[['*' for i in range(m)] for i in range(n)]

k=10

for i in range(m+n):
    if i<=n-1:
        for j in range(0, i+1):
            a[j][i-j]=k
            k+=1

    elif m-1>=i>n-1:
        for j in range(0, n):
            a[j][i-j]=k
            k+=1

    elif i>m-1:
          for j in range(i-m+1, n):
            a[j][i-j]=k
            k+=1

for row in a:
    print(' '.join([str(elem) for elem in row]))
