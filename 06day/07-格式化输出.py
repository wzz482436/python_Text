name = input("请输入名字:")
age = input("请输入年龄")
sex = input("请输入性别")
height = float(input("请输入身高"))
#print(name,age,sex)

'''
print(name)
print(age)
print(sex)
把自己的个人信息输入进来要整数 要有浮点数的 要有字符的 格式化输出到屏幕上
'''
#格式化输出
#%s 占位字符串
#%f 占位浮点数 保留两位小数%.02f
#%d 占位整数
print("我的名字是%s,我的年龄是%s,我的性别是%s,我的身高是%.02f"%(name,age,sex,height))


