#dictionary methods
di={1:23,
    2:45,
    4:56,
    5:68,
    7:89,
    9:90
    }
print(di.copy())
print(di.keys())
print(di.values())
print(di.get(2))
print(di.items())
di.popitem()
print(di.items())
di.pop(1)
print(di.items())
di.update({"car":"mstang"})
print(di)
i=di.setdefault(1,900)
print(i)
print(di)
di.clear()
print(di)


# string
s="abhishek IS a Hunter"
s=s.capitalize()
print(s)
s=s.casefold()
print(s)
c=s.center(200)
print(c)
c=s.count("a")
print(c)
c=s.encode()
print(c)
print(s.endswith("hunter"))
c=s.expandtabs(20)
print(c)
print(s.find("s"))
print(s.index("i"))
print(s.isalnum())
print(s.isalpha())
print(s.isascii())
print(s.isdecimal())
print(s.isdigit())
print(s.isidentifier())
print(s.islower())
print(s.isnumeric())
print(s.isspace())
print(s)
print(s.isprintable())
print(s.istitle())
print(s.isupper())
li=["monday "," tuesday "," wednesday" ]
c=s.join(li)
print(c)
c=s.ljust(20)
print(c,"it is good")
c=s.lstrip()
print(c)
c=s.replace("is","bad")
print(c)
print(s.rfind("ek"))
print(s.partition(" "))
print(s.rindex("ek"))
print(s.rjust(2))
print(s.rpartition("ek"))
print(s.rsplit())
print(s.rstrip())
print(s.split("is"))
print(s.strip("ek"))
c=s.swapcase()
print(c)
c=s.swapcase()
c=s.title()
print(c)
print(s.upper())
c=s.zfill(200)
print(c)

my={12: 45}
print(s.translate(my))# dictionay is translate
li=[" he is  "," woolen "," \nclothes "]

c=s.join(li)
print(c)
s="abhishek is hunter is very dangerous \nhe died the loins and tiger\n he also get died"
c=s.splitlines()
print(c)

# sets
c={1,2,3,4}
c.add(5)
print(c)
c.discard(3)
print(c)
c.pop()
print(c)
c.remove(4)
print(c)
c=c.intersection({2,3,4})
print(c)
c=c.union({4,5,6,7,8,9})
print(c)
c=c.difference({2,3,4})
print(c)
c=c.issuperset({2,3,1,0,9})
print(c)


















