# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 10:26:09 2018

@author: Yang
"""

#字典是一系列键值对
#与键相关联的值可以是数字、字符串、列表乃至字典以及任意Python对象
alien_0={'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
print('Success hit, you just earned '+str(alien_0['points'])+' points!')

#添加/修改键值对
alien_0['x_position']=25
alien_0['y_position']=24
print(alien_0)
alien_0['x_position']=4
print(alien_0)

#删除键值对
del alien_0['points']
print(alien_0)

#遍历字典,使用字典的items()方法返回一个键值对列表
user_0={
        'username':'知非',
        'first name':'jiajun',
        'last name':'yang',
        }
for key,value in user_0.items():
    print('\nKey:' + key)
    print('Value:' + value.title())

#遍历字典中所有的键 keys()
for key in user_0.keys():
    print(key)
#遍历字典时默认遍历字典的键，因此上面的语句等效为
for key in user_0:
    print(key)
    
#遍历字典中所有的值 values()
for value in user_0.values():
    print(value.title())

#嵌套
#将字典存储在列表中，或将列表作为值存在字典中，称为嵌套
#字典列表
aliens=[]
for alien_number in range(0,30):
    new_alien={
            'color':'red',
            'speed':'slow',
            'points':5
                }
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
#在字典中存储列表
favorite_languages={
        'san zhang':['python','php'],
        'si li':['c'],
        'wu wang':['c++','java']
        }
for name,language in favorite_languages.items():
    if len(language) == 1:
        print(name.title()+"'s favarite language is:"+language[0])
    else:
        print(name.title()+"'s favarite language are:")
        for language in language:
            print('\t'+language.title())       
#在字典中存储字典
users={
       'yjiajun':{
               'first':'jiajun',
               'last':'yang'
               },
       'zsan':{
               'first':'san',
               'last':'zhang'
               }
       }



