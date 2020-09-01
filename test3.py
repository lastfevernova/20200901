ID = input("输入一个账号：")
password = input("请输入一个密码：")
if  len(ID) > 5 and len(ID) < 8:
     if ID  == '张三12345' and password == '123456':
        print("登录成功")
     else:
        print("登陆失败")
else:
    print("登陆失败")

