q = int(input())
for i in range(q):
    w,e,r,t= input().split()
    w,e,r,t= int(w),int(e),int(r),int(t),
    p = w+e
    x = r+t
    if p == x:
        print('penalty')
    elif p>x:
        print('perspolis')
    else:
        print('esteghlal')