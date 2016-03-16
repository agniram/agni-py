
print('введите через пробел размер матрицы, n-количество строк; m-количество столбцов')
n, m = [int(i) for i in input().split()]
print(' ')


a=[[' *' for i in range(m)] for i in range(n)]

k=1
z=k
x=0
##################################################################
def first_iteration():
    global x,k,a
    if x==0:
        a[0][0]=k
        k+=1
        for j in range(x+1, m-x):
            if k==n*m+z:
                break
            a[x][j]=k
            k+=1
        spiral_2()
        x+=1
    return x,k,a
#################################
def spiral_1():
    global a,k
    if k<n*m+z:
        for j in range(x, m-x):
            if k==n*m+z:
                break
            a[x][j]=k
            k+=1
        return k,a

#################################
def spiral_2():
    global a,k
    if k<n*m+z:
        for i in range(x+1,n-x):
            if k==n*m+z:
                break
            a[i][ abs(m-x-1)]=k
            k+=1
        for j in range(m-x-2,x-1,-1):
            if k==n*m+z:
                break
            a[ abs(n-x-1)][j]=k
            k+=1

        for i in range(n-x-2,x,-1):
            if k==n*m+z:
                break
            a[i][x]=k
            k+=1

    return k,a
#################################


#################################
def other_iterations():
    global x,k,a,z
    while k<n*m+z:
        spiral_1()
        spiral_2()
        x+=1
    return x,k,a
#################################

def discharge():
    for i in range(n):
        for j in range(m):
            if a[i][j]<=9:
                a[i][j]='  ' + str(a[i][j])
            elif 9<a[i][j]<=99:
                a[i][j]=' '+ str(a[i][j])
            elif 99<a[i][j]<=999:
                a[i][j]=str(a[i][j])


#################################
def print_matrix():
    for row in a:
        print('( ' + '  '.join([str(elem) for elem in row]) + ' )')

#################################
def main():
    first_iteration()
    other_iterations()
    discharge()
    print_matrix()
#################################
main()
input('\n')
#################################