a={20,40,50,60,70}
type(a)
<class 'set'>
set()
set()
a={20,40,50,60,70}
a.add(0)
a
{0, 50, 20, 70, 40, 60}
b={20,40,50,60}
a.union(b)
{0, 70, 40, 50, 20, 60}
b={20.0,40.0,5000,600}
a.union(b)
{0, 70, 40, 5000, 50, 20, 600, 60}
a.update([10,50,60])
a
{0, 50, 20, 70, 40, 10, 60}
a.pop()
0
a.pop()
50
a.remove(70)
a
{20, 40, 10, 60}
a.remove(100)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.remove(100)
KeyError: 100
a.discard(20)
a
{40, 10, 60}
a.discard(100)
a
{40, 10, 60}
a.clear()
a
set()
a
{50, 20, 70, 40, 60}
b=a.copy()
b
{50, 20, 70, 40, 60}
a={10,20,50,60,70,80,60}
b={10,20,50}
b.issubset(a)
True
a.issuperset(b)
True
a={10,20,50,60}
b={50,60,80,90}
a.difference(b)
{10, 20}
a.intersection(b)
{50, 60}
