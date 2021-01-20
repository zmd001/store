name1="沙糖橘子"
price1=3
quality1="A+"
num1=15
unit1="斤"

name2="苹果"
price2=2
quality2="B+"
num2=20
unit2="个"

name3="香蕉"
price3=10
quality3="B+"
num3=10
unit3="斤"

name4="菠萝"
price4=15
quality4="C+"
num4=2
unit4="个"

print("------------------欢迎来到水果商城------------------")
print("名称      价格        品质         数量          单位")
print("-------------------------------------------------")
print(name1,"  ",price1,"       ",quality1,"        ",num1,"          ",unit1)
print(name2,"     ",price2,"       ",quality2,"        ",num2,"          ",unit2)
print(name3,"     ",price3,"      ",quality3,"        ",num3,"          ",unit3)
print(name4,"     ",price4,"      ",quality4,"        ",num4,"           ",unit4)
print("-------------------------------------------------")
print("总金额：",price1*num1+price2*num2+price3*num3+price4*num4,"￥")