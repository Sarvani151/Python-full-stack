Python 3.14.4 (v3.14.4:23116f998f6, Apr  7 2026, 09:45:22) [Clang 17.0.0 (clang-1700.6.4.2)] on darwin
Enter "help" below or click "Help" above for more information.
>>> #slicing
>>> a="time si very precious"
>>> a[9:13]
'ery '
>>> a[8:13]
'very '
>>> a[0:4]
'time'
>>> a[14:22]
'recious'
>>> a[13:22]
'precious'
>>> a="work until you succed"
>>> a[15:21]
'succed'
>>> a[5:10]
'until'
>>> a[0:4]
'work'
>>> a[11:14]
'you'
>>> #negative slicing
>>> a="vizag is city of destinty
SyntaxError: unterminated string literal (detected at line 1)
>>> a="vizag is city of destiny"
>>> a[-15:-11]
'city'
>>> a[-7:-1]
'destin'
>>> a[-7:-0]
''
>>> a[-7:0]
''
>>> a[-24:-19]
'vizag'
>>> a[-7:-1]
'destin'
>>> a="hi hello how are you
SyntaxError: unterminated string literal (detected at line 1)
>>> a="hi hello how are you"
>>> a[-18:-13]
' hell'
>>> a[-18:-12]
' hello'
>>> a[-4:-1]
' yo'
>>> a[-4: ]
' you'
>>> a="data science"
>>> a[ ::]
'data science'
>>> a[:: 1]
'data science'
>>> a[::2]
'dt cec'
>>> a="machine learning"
>>> a[::7]
'm n'
>>> a[::2]
'mcielann'
>>> a[3:1]
''
>>> a[8:]
'learning'
>>> a[9:]
'earning'
a[::4]
'miln'
a[::10]
'ma'
a[:8]
'machine '
a="cloud computing"
a[1:9:2]
'lu o'
