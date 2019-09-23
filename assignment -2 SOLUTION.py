'''
#1.>>
a=eval(input('Enter a number ='))
if a%2 == 0:
    print('The number %f is a EVEN number'%a)
else:
    print('the number %f is a ODD number'%a)
'''

'''
#2.>>
s=eval(input('enter a number ='))
if s%5==0:
    print('the number %f is divisible by 5'%s)
else:
    print('the number %f is not divisible by 5'%s)
'''

'''
#3.>>
s=eval(input('enter a number ='))
if s<0:
    print ('%d is a negative number'%s)
elif s==0:
    print('%d is zero'%s)
else:
    print('%d is a positive number'%s)
'''

'''
#4.>>
a,b,c=tuple(eval(z) for z in input('enter three number').split(' '))
x=a if a>b else b
y=x if x>c else c
print('The greatest among these number is %f'%y)    
'''

'''
#5.>>
yr=int(input('Enter the year '))
if yr%4==0:
    print('the year %d is a LEAP YEAR'%yr)
else:
    print('The year %d  a NOT a leap year'%yr)
'''

'''
#6.>>
q=int(input('enter the month number ='))
d31=(1,3,5,7,8,10,12)
for z in d31:
    if q==z:
        print('this month has 31 days')
    elif q==2:
        print('this month has either 28 or 29 days')
        break
    else:
        print('this month has 30 days')
        break
'''

'''
#7.>>
print('after comparing the coefficient of your quadratic equation with ax^2 + bx +c ')
a,b,c=[eval(z) for z in (input(' enter the value of a , b, c respectively ').split(' '))]
D=(b**2 - 4*a*c)
if D<0:
    print('both root of the given equation is imaginary')
elif D==0:
    print('both root are real and equal')
else:
    print('both roots are real and distinct')
'''

'''
#8.>>
l=input('enter three words ').split(' ')
print('Entered words list is \n',l)
l.sort   #we can also use "sort_l=sorted( l )" function for that
print('dictionary order of these three words are as follows :-\n',)
for x in l:
    print(x)
'''

'''
#9.>>
rp,ap=input('enter a complex number').split('+')
i=int(rp)
j=ap[:-1:1]
k=int(j)
print(i,type(i),k,type(k))

if i>k:
    print('real part(%d) is greater than imaginary part(%d)'%(i,k))
else:
    print('imaginary part(%d) is greater than real part(%d)'%(k,i))
'''

'''
#10.>>
ml=[eval(x)for x in input('enter the marks of FIVE subject').split(' ')]
c=[]
sum1=0
for q in ml:
    if q<=100:
        c.append(q)
    else:
        pass
if len(c)!=5:
    print('INVALID NUMBERS OF MARKS ENTERED or ENTERED INCORRECT MARKS IN ANY SUBJECT')
if len(c)==5:
    for s in c:
        sum1+=s
    print('Total marks is %d'%sum1)
    if sum1<=299:
        print('you are fail')
    else:
        if sum1>400:
            dev=1
        elif 350<sum1<400:
            dev=2
        else:
            dev=3
        print('you are pass by %dst division and has %f percent marks '%(dev,sum1/5))
'''        
































