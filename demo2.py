a = {"name":"langjin","age":"23"}
print(a["name"])
print(a["age"])
print(a.get("age1"))

a["address"] = "chongqin"#当key不存在时，新增
a["name"]="aa"#当key存在，修改
a.update(name = "wanger") #update的写法，key在这里是一个变量
a.pop("name")#取走
#通用的删除
del a["age"]
print(a)
a["money"] = "1000"
print(a)
print(list(a.keys("adress","money")))