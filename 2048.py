import random
a=[[0]*4 for i in range(4)]
def pri(a):
    for i in a:
        for j in i:
            print(str(j).rjust(4,' '),end='')
        print()
a[random.randint(0,3)][random.randint(0,3)]=2
while 2048 not in [x for i in a for x in i]:
    while True:
        m=random.randint(0,3)
        n=random.randint(0,3)
        if a[m][n]==0:
            a[m][n]=2
            pri(a)
            break
    x=input()
    if x=='a':
        for i in range(len(a)):
            if a[i][0]==0:
                if a[i][1]==0:
                    if a[i][2]==0:
                        a[i][0]=a[i][3]
                        a[i][3]=0
                    else:
                        a[i][0]=a[i][2]
                        a[i][2]=0
                else:
                    a[i][0]=a[i][1]
                    a[i][1]=0
            if a[i][1]==0:
                if a[i][2]==0:
                    a[i][1]=a[i][3]
                    a[i][3]=0
                else:
                    a[i][1]=a[i][2]
                    a[i][2]=0
            if a[i][2]==0:
                a[i][2]=a[i][3]
                a[i][3]=0
            if a[i][0]==a[i][1]:
                a[i][0]+=a[i][1]
                if a[i][2]==a[i][3]:
                    a[i][1]=a[i][2]+a[i][3]
                    a[i][2]=0
                    a[i][3]=0
                else:
                    a[i][1]=a[i][2]
                    a[i][2]=a[i][3]
                    a[i][3]=0
            elif a[i][1]==a[i][2]:
                a[i][1]+=a[i][2]
                a[i][2]=a[i][3]
                a[i][3]=0
            elif a[i][2]==a[i][3]:
                a[i][2]+=a[i][3]
                a[i][3]=0
    elif x=='w':
        for i in range(len(a)):
            if a[0][i]==0:
                if a[1][i]==0:
                    if a[2][i]==0:
                        a[0][i]=a[3][i]
                        a[3][i]=0
                    else:
                        a[0][i]=a[2][i]
                        a[2][i]=0
                else:
                    a[0][i]=a[1][i]
                    a[1][i]=0
            if a[1][i]==0:
                if a[2][i]==0:
                    a[1][i]=a[3][i]
                    a[3][i]=0
                else:
                    a[1][i]=a[2][i]
                    a[2][i]=0
            if a[2][i]==0:
                a[2][i]=a[3][i]
                a[3][i]=0
            if a[0][i]==a[1][i]:
                a[0][i]+=a[1][i]
                if a[2][i]==a[3][i]:
                    a[1][i]=a[2][i]+a[3][i]
                    a[2][i]=0
                    a[3][i]=0
                else:
                    a[1][i]=a[2][i]
                    a[2][i]=a[3][i]
                    a[3][i]=0
            elif a[1][i]==a[2][i]:
                a[1][i]+=a[2][i]
                a[2][i]=a[3][i]
                a[3][i]=0
            elif a[2][i]==a[3][i]:
                a[2][i]+=a[3][i]
                a[3][i]=0
    elif x=='s':
        for i in range(len(a)):
            if a[3][i]==0:
                if a[2][i]==0:
                    if a[1][i]==0:
                        a[3][i]=a[0][i]
                        a[0][i]=0
                    else:
                        a[3][i]=a[1][i]
                        a[1][i]=0
                else:
                    a[3][i]=a[2][i]
                    a[2][i]=0
            if a[2][i]==0:
                if a[1][i]==0:
                    a[2][i]=a[0][i]
                    a[0][i]=0
                else:
                    a[2][i]=a[1][i]
                    a[1][i]=0
            if a[1][i]==0:
                a[1][i]=a[0][i]
                a[0][i]=0
            if a[3][i]==a[2][i]:
                a[3][i]+=a[2][i]
                if a[1][i]==a[0][i]:
                    a[2][i]=a[1][i]+a[0][i]
                    a[1][i]=0
                    a[0][i]=0
                else:
                    a[2][i]=a[1][i]
                    a[1][i]=a[0][i]
                    a[0][i]=0
            elif a[2][i]==a[1][i]:
                a[2][i]+=a[1][i]
                a[1][i]=a[0][i]
                a[0][i]=0
            elif a[1][i]==a[0][i]:
                a[1][i]+=a[0][i]
                a[0][i]=0
    elif x=='d':
        for i in range(len(a)):
            if a[i][3]==0:
                if a[i][2]==0:
                    if a[i][1]==0:
                        a[i][3]=a[i][0]
                        a[i][0]=0
                    else:
                        a[i][3]=a[i][1]
                        a[i][1]=0
                else:
                    a[i][3]=a[i][2]
                    a[i][2]=0
            if a[i][2]==0:
                if a[i][1]==0:
                    a[i][2]=a[i][0]
                    a[i][0]=0
                else:
                    a[i][2]=a[i][1]
                    a[i][1]=0
            if a[i][1]==0:
                a[i][1]=a[i][0]
                a[i][0]=0
            if a[i][3]==a[i][2]:
                a[i][3]+=a[i][2]
                if a[i][1]==a[i][0]:
                    a[i][2]=a[i][1]+a[i][0]
                    a[i][1]=0
                    a[i][0]=0
                else:
                    a[i][2]=a[i][1]
                    a[i][1]=a[i][0]
                    a[i][0]=0
            elif a[i][2]==a[i][1]:
                a[i][2]+=a[i][1]
                a[i][1]=a[i][0]
                a[i][0]=0
            elif a[i][1]==a[i][0]:
                a[i][1]+=a[i][0]
                a[i][0]=0
else:
    print("YOU WIN")
