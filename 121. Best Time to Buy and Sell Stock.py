price=list(map(int,input().split()))
pre,ans=price[0],0
for i in range(1,len(price)):
    pre=min(pre,price[i])
    ans=max(price[i]-pre,ans)
print(ans)