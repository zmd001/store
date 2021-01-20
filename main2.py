name1="衬衫"
price1=45
num1=2
size1="xl"
color1="黑色"
unit="件"

name2="毛衣"
price2=80
num2=3
size2="l"
color2="黄色"
unit="件"

name3="棉服"
price3=150
num3=2
size3="xxl"
color3="白色"
unit="件"

name4="半袖"
price4=15
num4=4
size4="xxxl"
color4="灰色"
unit="件"

print("-------------------欢迎来到衣服商城-------------------")
print("名称     价格     数量      尺码      颜色      单位")
print("---------------------------------------------------")
print(name1,"   ",price1,"     ",num1,"     ",size1,"      ",color1,"    ",unit)
print(name2,"   ",price2,"     ",num2,"     ",size2,"       ",color2,"    ",unit)
print(name3,"   ",price3,"    ",num3,"     ",size3,"     ",color3,"    ",unit)
print(name4,"   ",price4,"     ",num4,"     ",size4,"    ",color4,"    ",unit)
print("---------------------------------------------------")
print("总金额：",price1*num1+price2*num2+price3*num3+price4*num4,"￥")