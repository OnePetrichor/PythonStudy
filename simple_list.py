# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 15:13:07 2018

@author: Yang
"""

#列表
games=['lol','cs go','dnf']
#直接输出列表，将打印列表的内部表示，包括方括号
print(games)

#访问列表元素
games=['lol','cs go','dnf']
print(games[0])
print(games[1].title())
#当索引为-1时将输出列表的最后一个元素
print(games[-1])
#同理，当索引为-2时将输出列表的倒数第二个元素
print(games[-2].upper())

#修改、添加、删除列表元素
games=['lol','cs go','dnf']
games[0]='lollol'
print(games)
#使用append()方法往列表末尾添加元素
games.append('fortnite')
print(games)
#使用insert()方法往列表任意位置添加元素
games.insert(0,'first_game')
print(games)
#使用del语句删除列表元素
del games[0]
print(games)
#使用pop()方法删除列表末尾元素，并用于使用
poped_game=games.pop()
print(poped_game)
print(games)
#使用pop(int)方法删除列表中任意位置元素
first_game=games.pop(0)
print(first_game)
print(games)
#根据值来删除元素
games=['lol','cs go','dnf']
games.remove('cs go')
print(games)
#Tips:remove()方法只删除第一个指定的值，若要删除的值在列表中出现多次，需使用循环

#组织列表
#使用sort()方法对列表进行永久排序
#Tips:sort()方法将直接修改原列表，且该方法没有返回值
numbers=[2,1,3,5,4,8,7,6]
numbers.sort()
print(numbers)
numbers=[2,1,3,5,4,8,7,6]
numbers.sort(reverse=True)
print(numbers)
#使用sorted()对列表进行临时排序
numbers=[2,1,3,5,4,8,7,6]
print(sorted(numbers))
print(numbers)
#使用reverse()方法对列表进行反序排列,永久性地,且没有返回值
numbers=[2,1,3,5,4,8,7,6]
numbers.reverse()
print(numbers)
#使用len()方法获取列表的长度
print("The length of the gamelist is "+str(len(numbers)))

#操作列表
#使用for循环遍历整个列表
students=['San Zhang','Si Li','Wu Wang','Liu Zhao']
for student in students:
    print(student)

#列表解析
#列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素
squares=[value**2 for value in range(1,11)]
print(squares)

#切片
players=['Zhang San','Si Li','Wu Wang','Liu Zhao']
print(players[0:2])
#未指定前索引时自动从列表的第一个元素开始
print(players[:2])
#未指定末索引时自动以列表的最后一个元素作为结束
print(players[2:])
#下面的语法输出列表末尾的2个元素
print(players[-2:])
#遍历切片，跟遍历列表类似
for player in players[0:3]:
    print(player)
    
#复制列表
#使用整个列表的切片进行列表复制
othersPlayers=players[:]
#若使用下面这种方式，则相当于两个变量均指向同一个列表，而不是复制一个新的
othersPlayers=players

#元组
#不可变的列表被称为元组
dimensions=(200,50)
print(dimensions[0])
#修改元组变量
#随便不能修改元组的元素，但是可以给存储元组的变量赋值
dimensions=(100,20)
print(dimensions)





