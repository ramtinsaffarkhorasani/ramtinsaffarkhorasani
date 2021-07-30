#name= (input("enter your name:")
#family = (input("enter your family:"))
n=input('enter your name:')
f=input('enter your name:')

nomre1=int(input('enter score one'))
nomre2=int(input('enter score two'))
nomre3=int(input('enter score three'))

majmoe=nomre1+nomre2+nomre3
miangin=majmoe/3

if miangin >= 17 :
    print(n,f,'average=',miangin,"your condition is grat")
elif miangin < 17 and miangin >=12:
    print (n,f,'average=',miangin,"your condition is normal") 
elif miangin <12:
    print(n,f,'average=',miangin,"your condition is fail")