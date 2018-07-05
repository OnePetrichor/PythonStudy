# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 21:17:02 2018

@author: Yang
"""

#简单示例
friends=['yi','er','san','si','wu']
for friend in friends:
    if friend == 'er':
        print(friend.upper())
    else:
        print(friend.title())

#检查多个条件 and/or
age_0=18
age_1=23
if age_0<=20 and age_1>20:
    print('True:age_0<=20 and age_1>20')
else:
    print('False:age_0<=20 and age_1>20')

#检查特定值是否在列表中 in
friends=['yi','er','san','si','wu']
print('yi' in friends)
print('y' in friends)

#检查特征值是否不在列表中 not in
if 'yy' not in friends:
    print('yy不在friends列表中')
    
#if-elif-else语句
age=17
if age<=5:
    print('Welcome,you should pay nothing.')
elif age<18:
    print('Your admission cost is $5.')
else:
    print('Your admission cost in $10.')












