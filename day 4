#Smart List Filter & Rebuilder

k=int(input("Enter Number of elements in list: "))
data=[0]*k
for i in range(k):
    a=input("enter element: ")
    num=True
    if a=="":
        num=False
    else:
        for j in a:
            if(j>'9' or j<'0'):
                num=False
                break
    if num==True:
        data[i]=int(a)
    else:
        data[i]=a

digit=[]
string=[]
#Personalization data
registration_no="AP24110011832"

numbers_count=0
string_count=0
for i in data:
    if(i*0 ==0):
        digit=digit+[i]
        numbers_count+=1
    else:
        if(i!=""):
            string=string+[i]
            string_count+=1

# Personalization logic(Option-A)
if( int(registration_no[-1]) % 2==0):
    n=numbers_count
    for i in range(n//2):
        temp=digit[i]
        digit[i]=digit[n-i-1]
        digit[n-1-i]=temp
else:
    n=string_count
    for i in range(n//2):
        temp=string[i]
        string[i]=string[n-i-1]
        string[n-1-i]=temp

print("Numbers List: ",digit)
print("String List: ",string)
print("Total Numbers: ",numbers_count)
print("Total strings: ",string_count)


