Python 3.14.4 (v3.14.4:23116f998f6, Apr  7 2026, 09:45:22) [Clang 17.0.0 (clang-1700.6.4.2)] on darwin
Enter "help" below or click "Help" above for more information.
>>> #list
>>> a=[3,5.6,"python",9+7j,True,False]
>>> print(a)
[3, 5.6, 'python', (9+7j), True, False]
>>> type(a)
<class 'list'>
>>> b=9
>>> print(b)
9
>>> type(b)
<class 'int'>
>>> c=[9]
>>> print(c)
[9]
>>> #list methods
>>> a=["python","java","c"]
>>> a.append("c++")
>>> a
['python', 'java', 'c', 'c++']
>>> a.append(["ml,"ai"])
...           
SyntaxError: unterminated string literal (detected at line 1)
>>> a.append(["ml","ai"])
...           
>>> a
...           
['python', 'java', 'c', 'c++', ['ml', 'ai']]
>>> a.append("ml","ai")
...           
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a.append("ml","ai")
TypeError: list.append() takes exactly one argument (2 given)
>>> #extend()
...           
>>> a=["java","html","css"]
...           
>>> a.extend(["js","bs"])
...           
>>> a
...           
['java', 'html', 'css', 'js', 'bs']
>>> #insert
...           
>>> b=["apple","banana","grapes"]
...           
>>> b.insert(a,"mango")
...           
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    b.insert(a,"mango")
TypeError: 'list' object cannot be interpreted as an integer
>>> b.insert(1,"mango")
...           
>>> b
...           
['apple', 'mango', 'banana', 'grapes']
>>> #sort()
...           
>>> a=['kiwi','mango','apple','banana']
...           
>>> a.sort()
...           
>>> a
...           
['apple', 'banana', 'kiwi', 'mango']
b=[9,6,3,0,2,4,20]
          
b.sort()
          
b
          
[0, 2, 3, 4, 6, 9, 20]
#reverse
          
a=["c","html","java","css"]
          
a.reverse()
          
a
          
['css', 'java', 'html', 'c']
b=[9,10,12,14,15]
          
b.reverse()
          
b
          
[15, 14, 12, 10, 9]
a=["black","white","red","blue","pink"]
          
a.pop()
          
'pink'
a
          
['black', 'white', 'red', 'blue']
a.pop(2)
          
'red'
a
          
['black', 'white', 'blue']
a.pop("white")
          
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a.pop("white")
TypeError: 'str' object cannot be interpreted as an integer
#copy
          
a=["pooja","priya","sweety,"cuty"]
   
SyntaxError: unterminated string literal (detected at line 1)
a=["pooja","priya","sweety","cuty"]SyntaxError: unterminated string literal (detected at line 1)a=
   
SyntaxError: invalid syntax
a=["poojaa","sri","sai","saketh"]
   
a.copy()
   
['poojaa', 'sri', 'sai', 'saketh']
b=a.copy()
   
b
   
['poojaa', 'sri', 'sai', 'saketh']
a.clear()
   
a
   
[]
b.append("hi")
   
b
   
['poojaa', 'sri', 'sai', 'saketh', 'hi']
#len and count
   
a=["hi","hello","how"]
   
len(a)
   
3
b="hello"
   
len(b)
   
5
c=["hello"]
   
len(c)
   
1
a.count("hello")
   
1
