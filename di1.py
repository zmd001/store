# import pymysql
# # 通过pymysql获取连接
# con = pymysql.connect(host="localhost",user="root",password="123456",database="company")
# # 获取游标
# cursor = con.cursor() # 获取一个游标
# # 准备一条sql语句
# sql = "insert into t_dept values(%s,%s,%s)"
# param= ["160","财务部","北京"]
# # 执行sql语句
# num = cursor.execute(sql,param)
# print("影响了",num,"行数据")
# # 提交实际数据
# con.commit()  # 将缓存的数据真正的提交给数据库
# # 关闭资源
# cursor.close()
# con.close()


# import pymysql
# con = pymysql.connect(host="localhost",user="root",password="123456",database="company")
# cursor = con.cursor()
# sql = "delete from t_dept where dname = %s"
# param= ["财务部"]
# num = cursor.execute(sql,param)
# print("影响了",num,"行数据")
# con.commit()
# cursor.close()
# con.close()


# import pymysql
# con = pymysql.connect(host="localhost",user="root",password="123456",database="company")
# cursor = con.cursor()
# sql = "update t_dept set dname = %s where deptno = '90' "
# param= ["张三"]
# num = cursor.execute(sql,param)
# print("影响了",num,"行数据")
# con.commit()
# cursor.close()
# con.close()


import pymysql
con = pymysql.connect(host="localhost",user="root",password="123456",database="company")
cursor = con.cursor()
sql = "select * from t_employees where ename = %s"
param= ["黄忠"]
num = cursor.execute(sql,param)
data = cursor.fetchall()
print("影响了",num,"行数据")
for i in data:
    print(i)
con.commit()
cursor.close()
con.close()
