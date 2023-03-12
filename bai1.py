def transferWithNegative(n):
    k = []

    while (n>0 ):
        a = int(n%2) # Tinh phan du
        k.append(a) # Day phan du vao danh sach
        n = (n-a)/2 # Tinh phan thuong cho phep tinh tiep theo

    while (len(k)<16) :
        k.append(0)

   
    kq = ""

    k.reverse() # Dao nguoc danh sach
    
    for i in range(16):
        if(k[i]==0) :
            k[i]=1
        else:
            k[i]=0
    
    123
    # Chuyen doi list sang string
    for i in k:
        kq += str(i)
    return kq

def transferWithPositive(n):
    k = []

    while (n>0):
        a = int(n%2)# Tinh phan du
        k.append(a) # Day phan du vao danh sach
        n = (n-a)/2 # Tinh phan thuong cho phep tinh tiep theo

    while (len(k)<16) :
        k.append(0)
    
    kq = ""

    k.reverse() # Dao nguoc danh sach
    # Chuyen doi list sang string
    for i in k:
        kq += str(i)
    return kq

#------------------------------------------------------------------------------------------------------------------

def fractionToBinary(x2) : # Chuyển phần phân về nhị phân
    k=['']
    while ((round(x2,15)-int(x2)!=0)&(len(k)<=149)):
        a=int(x2*2)
        if (round(x2*2,15)-1>=0):
            x2=round(x2*2,15)-int(x2*2)
        else:
            x2=round(x2*2,15)
        k.append(a)
    x=""
    for i in k:
        x+=str(i)
    return x
def biased(n) : # chuyển số exponent về nhị phân dạng Biased K
    x=n+127
    return transferWithPositive(x)

def singlePrecision(n): # chuyển về dạng single Precision
    k=['']
    if (n>0): k.append('0')  # kiểm tra bit dấu là âm hay dương
    if (n<0): k.append('1')
    n=abs(n) 
    x1=int(n)
    x2=round(n-x1,15)

    k1=int(transferWithPositive(x1)) # chuyển phần thực về nhị phân
    k1=str(k1)
    
    k2=fractionToBinary(x2)

    position=-1
    exponent=0
    if (k1!='0') :
        for i in range(0,len(k1)):
            if (k1[i]=='1'):
                position=i
                break
        exponent=len(k1)-position-1
    else:
        for j in range(0,len(k2)):
            if(k2[j]=='1'):
                position=j
                break
        exponent=-position-1

   
    exponentStr=int(biased(exponent))
    exponentStr=str(exponentStr).zfill(8) # 8 bit exponent


    k.append(exponentStr)
    if (exponent>0) :
        for i in range(1,len(k1)):
            k.append(k1[i])
        for i in k2:
            k.append(i)
    elif(exponent<0):
        for i in range(position,len(k2)):
            k.append(k2[i])
    while (len(k)>=25):
        k.pop(24)
    while (len(k)<=25):
        k.append('0')
    x=""
    for i in k:
        x+=str(i)
    return x


# Chuong trinh chinh
n = int(input("1. Input integer (16 bits ): "))
while (n>32767 or n<-32768) :
    print("The integer has just entered more than 16 bits  ")
    n = int(input("1. Input integer (16 bits ): "))
if(n>=0):
   print("2. Integer", n,"is two's complement representation (16 bits): ", transferWithPositive(n))
if (n<0):
    num=int(transferWithNegative(n*-1),2)+1
    print("2. Integer", n,"is two's complement representation (16 bits): ", transferWithPositive(num))


t=float(input("3. Input single precision: "))
if (t!=0) :
    print("4. Single precision" ,t,"is : ",singlePrecision(t))      
else:
    print("4. Single precision", t, "can't representation")  