import random
secret = random.randint(1,10)
temp = input("请输入一个数字：")
guess = int(temp)
while guess != secret:
    temp = input("错了请重新输入：")
    guess = int(temp)
    if guess == secret:
        print("猜中")
    elif guess > secret:
        print("大了大了")
    else:
        print("小了小了")
print("游戏结束")

#a ='let\'s go'
#print(a)
