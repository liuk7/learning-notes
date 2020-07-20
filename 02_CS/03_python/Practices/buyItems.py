N,M=3200,60
f=[0]*N
#分组背包，每组有四种情况，a.主件 b.主件+附件1 c.主件+附件2 d.主件+附件1+附件2
v=[[0 for i in range(4)] for j in range(M)] #体积
w=[[0 for i in range(4)] for j in range(M)] #价值
n,m=map(int,input().split())
n=n//10#价格为10的整数倍，节省时间
for i in range(1,m+1):
    x,y,z=map(int,input().split())
    x=x//10
    if z==0:
        for t in range(4):
            v[i][t], w[i][t] = v[i][t]+x, w[i][t]+x* y
    elif v[z][1]==v[z][0]:#如果a==b，添加附件1(如果a=b=c=d说明没有附件)
        v[z][1],w[z][1] = v[z][1] + x, w[z][1] + x* y
        v[z][3],w[z][3] = v[z][3] + x, w[z][3] + x* y
    else:#添加附件2
        v[z][2], w[z][2] = v[z][2] + x, w[z][2] + x* y
        v[z][3], w[z][3] = v[z][3] + x, w[z][3] + x* y
for i in range(1,m+1):
    for j in range(n,-1,-1):
        for k in range(4):
            if j>=v[i][k]:
                f[j]=max(f[j],f[j-v[i][k]]+w[i][k])
print(10*f[n])