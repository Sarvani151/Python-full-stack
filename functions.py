#functions
'''a=10
b=20
print("the sum is:",a+b)
print("the diff is:",a-b)
print("the product is:",a*b)'''
'''a=100
b=200
print("the sum is:",a+b)
print("the diff is:",a-b)
print("the product is :",a*b)'''
'''a=1000
b=2000
print("the sum is:",a+b)
print("the diff is:",a-b)
print("the product is :",a*b)'''


'''def calculate(a,b):
    print("the sum is:",a+b)
    print("the diff is:",a-b)
    print("the product is :",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''

'''def calculate(a,b):
    print("the power is:",a**b)
    print("the div is:",a%b)
    print("the floor div is",a//b)
calculate(10,20)
calculate(3,4)
calculate(5,8)'''
'''while True:
    def add():
        a=int(input("a value"))
        b=int(input("b value"))
        print(a+b)
    add()'''
#using functions
'''def add()
        a=int(input("a value"))
        b=int(input("b value"))
        print(a+b)
        add()
add()'''
'''def fullname():
    fname=input("first name")
    lname=input("last name")
    print((fname+" "+lname).title())
fullname()'''
#print v/s return
'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(2,3)'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d ,e
print(cal(2,3))'''
#splitbill
def bill():
    total_bill=2000
    per_person=total_bill//5
    print(per_person)
bill()

    
