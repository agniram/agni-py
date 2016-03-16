n=10
m=5
x=0
z=0
a=             [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1],
                [1, 0, 0, 1, 0],
                [0, 1, 0, 1, 0],
                [1, 1, 1, 1, 1],
                [0, 1, 1, 0, 1],
                [1, 1, 1, 1, 1]]
####################################
for row in a:
        print('  '.join([str(elem) for elem in row]))
print(' ')
####################################
def offset_unit():
    global a
    for i in range(x,-1,-1):
        for j in range(m):
            if i==0:
                a[i][j]=0
            else:
                a[i][j]=a[i-1][j]
####################################
for i in range(n-1,-1,-1):
    z=0
    for j in range (m):
        if a[i][j]==0:
            break
        elif a[i][j]==1:
            z+=1
            if z==m:
                x=i
                offset_unit()
####################################
for row in a:
        print('  '.join([str(elem) for elem in row]))
####################################
input('\n')