
"""
b = ("lanjin","fire")
a = (1,2,3,'',None,True,b)
print(a[-2])
print(a.index(None))
print(a.count(1))
print(a[-1][0])
print(a[-1].index("lanjin"))
print(a[0:1])
"""
c = ['ab',12,True,"哈哈","哈哈"]
name = input("请输入你的名字:")
c.append(name)
c.insert(0,name)
aa = [c.pop(1)]
print(c + aa)
c.remove("哈哈")
print(c)
