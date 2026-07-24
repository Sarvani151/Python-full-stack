#list comprehension
a=["codegnan","python","course"]
#print(a.upper())
'''b=str(a)
print(b.upper())'''
''' for i in a:
      print(i.upper(),end=" ")'''
'''b=[]
for i in a:
    b.append(i.upper())
print(b)'''
#syntax
#a=[expr for var in collection/range]
'''a=[i.upper() for i in a]
print(a)'''

'''a=["vij","hyd","vzg"]
a=[i.title() for i in a]
print(a)'''

'''a=[1,2,3,5,6,8,12,13]
a=[i**2 for i in a]
a=[i*i for i in a]
a=[pow(i,2) for i in a]
print(a)'''

#if-usage in list comprehension
'''a=[i for i in range(16) if i%2==0]
print(a)'''

'''a=[i for i in range(20) if i%2==0]
print(a)'''

'''a=[i for i in range(31)]
print(a)'''

'''fruits=["apple","banana","grapes","kiwi","mango","dragon","berry"]
a=[i for i in fruits if "a" in i]
print(a)'''


'''fruits=["apple","banana","grapes","kiwi","mango","dragon","berry"]
a=[i for i in fruits if "a"  not in i]
print(a)'''

#no elif usage in list comprehension
#if else usage in list comprehension
'''a=[i**2 if i%2==0 else i*5 for i in range(21)]
print(a)'''

a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[a[i]+b[i] for i in range(5)]
print(c)



