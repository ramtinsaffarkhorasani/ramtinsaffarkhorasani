import math

op=input('چه کار کنم اعداد رو')
if   op=='fac' or op=='%':
    a=float(input("عدد را وارد کن"))
else:    

    a = float(input('عدد را وارد کن'))
    b = float(input('عدد را وارد کن'))

if op=="+":
    result= a+b
elif   op=="-":
    result= a-b
elif op=="*":
    result= a*b
elif op== '/':
    if b==0:
        result='نمیشه با صفر'
    else:
        result=a/b  
elif op=='%':
    result =a/100 
elif op=='فاکتوریل':
    result=math.factorial(a)       

print(result)