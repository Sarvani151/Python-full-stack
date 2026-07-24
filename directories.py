#print(dir())
#print(dir("__builtins__"))
a="codegnan"
#print(a)
#print(list(a))
#print(tuple(a))
#print(set(a))
#print(dict(a))
'''b=dict.fromkeys(a)
print(b)'''
'''c=dict.fromkeys(a,"pooja")
print(c)
c["d"]="sam"
print(c)'''
#eval
'''while True:
    a=int(input())
    b=int(input())
    print(a+b)'''

'''while True:
    a=float(input())
    b=float(input())
    print(a+b)'''
'''while True:
    a=input()
    b=input()
    print(a+b)'''
'''while True:
    a=eval(input())
    b=eval(input())
    print(a+b)'''

#zip
'''a=[10,20,30,40,50]
names=["teja","dinesh","vamsi","sankalp","surya"]
print(a+names)'''

'''b=zip(a,names)
print(b)

c=list(zip(a,names))
print(c)

c=tuple(zip(a,names))
print(c)'''

'''c=set(zip(a,names))
print(c)'''
'''c=list(zip(a,names))
print(c)'''

names=["mythri","darshini","sarvani","srivarna","tejaswini"]
'''for i in range(len(names)):
    print(i,names[i])'''

'''b=dict(enumerate(names))
print(b)'''

'''b=dict(enumerate(names,100))
print(b)'''

#ASCII
#print(chr(65))
#print(chr(90))

'''print(ord("a"))
print(ord("z"))'''

'''for i in range(65,91):
    print(chr(i),end=" ")'''

'''for i in range(97,123):
    print(chr(i),end=" ")'''

'''a=input("enter the name:")
for i in a:
    print(i,"_",ord(i))'''
#max(),min(),sum()
'''print(max(2,5,8,9,10,20,30))'''
'''print(min(2,5,8,9,10,20,30))'''
a=2,3,4,5,6,7,8,9
print(sum(a))
      









