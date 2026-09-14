a=[10,'hello',20.2,False]
type(a)
<class 'list'>
a.append(10)
a
[10, 'hello', 20.2, False, 10]
a.append('hello')
a
[10, 'hello', 20.2, False, 10, 'hello']
a.extend('hello')
a
[10, 'hello', 20.2, False, 10, 'hello', 'h', 'e', 'l', 'l', 'o']
a.extend([10,20,30])
a
[10, 'hello', 20.2, False, 10, 'hello', 'h', 'e', 'l', 'l', 'o', 10, 20, 30]
a.append([10,20,30])
a
[10, 'hello', 20.2, False, 10, 'hello', 'h', 'e', 'l', 'l', 'o', 10, 20, 30, [10, 20, 30]]
a=[10, 'hello', 20.2, False, 10, 'hello']
a.insert(10,2)
a
[10, 'hello', 20.2, False, 10, 'hello', 2]
a=[10,'hello',20.2,False,10,'hello',2]
a.insert(1,'bye')
a
[10, 'bye', 'hello', 20.2, False, 10, 'hello', 2]
a.remove(2)
a
[10, 'bye', 'hello', 20.2, False, 10, 'hello']
a.pop()
'hello'
a.pop(2)
'hello'
a
[10, 'bye', 20.2, False, 10]
b=a.copy()
b
[10, 'bye', 20.2, False, 10]
b.clear()
b
[]
a.index(20.2)
2
a[1].index('y')
1
a=['i love pyhton','python','hello']
   
a[1].index('o',4)
   
4
a[0].index('o',4)
   
11
a.count('o')
   
0
a=['i love pyhton','python','hello']
   
a[0].count('o')
   
2
A=[10,40,70,980,50]
   
a.sort()
   
a
   
['hello', 'i love pyhton', 'python']
A.sort()
   
a
   
['hello', 'i love pyhton', 'python']
A=[10,40,70,980,50]
   
A.sort()
   
a
   
['hello', 'i love pyhton', 'python']
A
   
[10, 40, 50, 70, 980]
A=[10,40,70,980,50]
   
A.sort(reverse=True)
   
a
   
['hello', 'i love pyhton', 'python']
A
   
[980, 70, 50, 40, 10]
A.reverse()
   
A
   
[10, 40, 50, 70, 980]
