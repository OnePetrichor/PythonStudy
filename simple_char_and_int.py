# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 15:11:23 2018

@author: Yang
"""
#字符串可以用单引号或双引号
message="This is a message"
print(message)
message="This is a new message"
print(message)
print(message.title())
print(message.upper())
print(message.lower())

#合并字符串
first_name="jiajun"
last_name="yang"
full_name=last_name.title()+" "+first_name.title()
print("Hello,"+full_name+"!")

#制表符和换行符
print("\tPython")
print("\tPython\n\tC++\n\tPHP")

#删除空白
#rstrip()用于去掉字符串末尾的空白
#lstrip()用于去掉字符串开头的空白
#strip()用于去掉字符串开头和末尾的空白
#Tips:要永久删除字符串的空白需将删除操作的结果存回到变量中
test_char=" python "
print(test_char.strip())

#数字
#注意乘方运算用 ** 
print(2+3)
print(2-3)
print(2*3)
print(2**3)
print((2+3)*3)
#存在一些问题
print(0.1+0.2)
#python2 中两个整数相除只只保留整数部分，而非四舍五入

#str()函数转换类型
age=23
message="Happy "+str(age)+"rd Birthday!"
print(message)








