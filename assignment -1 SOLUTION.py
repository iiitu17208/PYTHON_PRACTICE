'''
#1.))
a,b=int(input('Enter first number')),int(input('Enter second number'))  #basic input method
                    #OR(comment any one of them before testing
a,b=[eval(s) for s in input('Enter two number =').split(' ')]            #using comprehension technique and using eval() and unpacking technique of dict
print("SUM OF %d AND %d is %d"%(a,b,a+b))
'''


'''
#2.))
r=eval(input('Enter radius of the circle'))
print('Area of the given circle is %fS'%(3.14*(r**2)))
'''

'''
#3.))
l,w,h=tuple(eval(s) for s in input('Enter length width and hight respectively of cuboid').split(' '))
print('Volume of cuboid is %f units'%(l*w*h))
'''

'''
#4.))
p,r,t=[eval(x) for x in input('Enter principle amount , rate of interest , time(in yr) of simple interest').split(' ')]
print('simple interest for %f in %f year at %f rate is %f'%(p,t,r,((p*r*t)/100)))
'''

'''
#5.))
s=eval(input('Enter the Number'))
print('Square of the given number is %f'%(s**2))
'''

'''
#6.))
a,b,c=tuple(eval(x) for x in input('Enter the length of three side of triangles ').split(' '))
s=(a+b+c)/2 #semi perimeter
area=(s*(s-a)*(s-b)*(s-c))**(.5)
print('Area of the given triangle is %f'%area)
'''

            

    
    

    
