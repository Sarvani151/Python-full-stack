#MARKKS ANALYSIS REPORT
'''students=int(input("enter the no.of students"))
marks=[]
for i in range(1,students+1):
    mark=int(input(f"enter the student {i} marks"))
    marks.append(mark)
for i in marks:
    print(i)
print(".......marks analysis report.........")
print("total students",students)
print("heighest marks",max(marks))
print("lowest marks",min(marks))
print("total marks",sum(marks))
print("average",sum(marks)/students)'''

#annonymous functions
'''def f(x):
    print(2*x+5)
f(5)'''

'''def f():
    x=int(input())
    print(2*x+5)
f()'''

#syntax
#a=lambda arg:expr
'''a=lambda x:2*x+5
print(a(5))'''

'''a=int(input())
b=lambda x:2*x+5
print(b(a))'''

'''a=lambda x,y:x*y
print(a(3,4))'''

'''a=int(input())
b=int(input())
c=lambda a,b:a*b
print(c(a,b))'''

#a="codegnan"
'''b=lambda a:a.upper()
print(b(a))'''
'''a=lambda a:a.upper()
print(a("codegnan"))'''

'''b="python course"
c=lambda a:a.title()
print(c(b))'''

'''fname=input("first name")
lname=input("last name")
fullname=lambda fname,lname:(fname+" "+lname).title()
print(fullname(fname,lname))'''

'''fname,lname=[x for x in input("enter the name")
                   .split(",")]
fullname=lambda fname,lname:(fname+" "+lname).title()
print(fullname(fname,lname))'''

#filter()
'''a=[10,20,23,25,67,45,80,90,85,100]
b=list(filter(lambda x:x%2==0,a))
print(b)'''

#[],().{}
'''a=[]
print(type(a))'''
'''b=()
print(type(b))'''
'''c={}
print(type(c))'''
'''d=set()
print(type(d))'''
a=[[],(),set(),{}," ",None,3,5.6,"pooja",4+9j,True,False]
b=list(filter(None,a))
print(b)

