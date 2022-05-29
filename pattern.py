'''sp=8
n=int(input())
for i in range(1,n):
   print(" "*sp+" *"*i,end=" ")
   sp-=1
   print()

n=int(input())
for i in range(1,n+1,1):
    for s in range(1,n-i+1,1):
        print(' ',end='')
    for p1 in range(1,i+1,1):
        print('*',end='')
    for p2 in range(i-1,0,-1):
        print('*',end='')

    print()
    '''