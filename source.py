a=1;b=1;c=a+b;t=0
for i in range(100):
    if t==0: #for print 0
        print(t,end=" ")
        t=5 #for end the printing 0
    print(a,"",b,"",c,"",end="")
    a=b+c
    b=a+c
    c=b+a
