import random
import time
num = random.randint(1,100)
counter = 0
a = 0
z = 300
while True:
    counter == a
    if a >=3:
        print("系统锁定5秒")
        f = 1
        while f <= 5:
            print(".",end="")
            time.sleep(1)
            f = f + 1
            a = 0
    a = a + 1
    counter = counter + 1
    n = input("请输入你想输入的数：")
    n = int(n)
    if n > num:
        z = z - 10
        print("大了,您还有：",z)
        if z <= 0:
            print("您输了！")
            break
    elif n < num:
        z = z - 10
        print("小了,您还有：",z)
        if z <= 0:
            print("您输了！")
            break
    else:
        z = z + 100
        print("恭喜您猜对了!您本次猜了：",counter,"次","您还有：",z)
        break
