def to_binary (num):
    a=""
    b="1"
    while num!=1:
        x=num%2
        num=num//2
        a+=str(x)
    for i in range(0-len(a),0):
        b+=a[i]
    return b
aa=to_binary(44)
print(aa)
