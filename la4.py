def EncoderQR():
    
    b=["10000000","01000000","00100000","00010000","00001000"]
    name=input("Enter the name:")
    if len(name)>5:
        return
    a=[ord(i) for i in name]
    a=[format(i,'08b') for i in a]
    ab=[]
    for s in range(0,len(a)):
        ab.append(b[s]+a[s])
    
    st=""
    for w in ab:
        st=st+w
    print(st)
    
