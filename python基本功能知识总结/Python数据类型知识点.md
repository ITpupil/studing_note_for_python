## **1.字符串**

- **字符串常用功能**

~~~python
name = 'derek'
print(name.capitalize())    #首字母大写  Derek
print(name.count("e"))      #统计字符串出现某个字符的个数  2
print(name.center(10,'*'))  #打印30个字符，不够的“*”补齐   **derek***
print(name.endswith('k'))   #判断字符串是否以"k"结尾   True

print('244'.isdigit())      #判断字符是否为整数      True
print('+'.join(['1','2','3']))   #把join后的内容加入到前面字符串中，以+为分割符   1+2+3
print('\n123'.strip())       #strip去掉换行符
print("1+2+3+4".split("+"))   #以+为分隔符生成新的列表，默认不写为空格    ['1', '2', '3', '4']

msg = 'my name is {name} and i am {age} old'
print(msg.format(name='derek',age=20))

my name is derek and i am 20 old
~~~

- **字符串的内置方法**

~~~python
# string.capitalize()                                  把字符串的第一个字符大写
# string.center(width)                                 返回内容是原字符串居中,并使用空格填充至长度为 width 的新字符串
# string.count(str, beg=0, end=len(string))            返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
# string.decode(encoding='UTF-8', errors='strict')     以 encoding 指定的编码格式解码 string，如果出错默认报一个 ValueError 的 异 常 ， 除 非 errors 指 定 的 是 'ignore' 或 者'replace'
# string.encode(encoding='UTF-8', errors='strict')     以 encoding 指定的编码格式编码 string，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
# string.endswith(obj, beg=0, end=len(string))         检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
# string.expandtabs(tabsize=8)                         把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8。
# string.find(str, beg=0, end=len(string))             检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
# string.index(str, beg=0, end=len(string))            跟find()方法一样，只不过如果str不在 string中会报一个异常.
# string.isalnum()                                     如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
# string.isalpha()                                     如果 string 至少有一个字符并且所有字符都是字母则返回 True,否则返回 False
# string.isdecimal()                                   如果 string 只包含十进制数字则返回 True 否则返回 False.
# string.isdigit()                                     如果 string 只包含数字则返回 True 否则返回 False.
# string.islower()                                     如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
# string.isnumeric()                                   如果 string 中只包含数字字符，则返回 True，否则返回 False
# string.isspace()                                     如果 string 中只包含空格，则返回 True，否则返回 False.
# string.istitle()                                     如果 string 是标题化的(见 title())则返回 True，否则返回 False
# string.isupper()                                     如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
# string.join(seq)                                     以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
# string.ljust(width)                                  返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
# string.lower()                                       转换 string 中所有大写字符为小写.
# string.lstrip()                                      截掉 string 左边的空格
# string.maketrans(intab, outtab])                     maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
# max(str)                                             返回字符串 str 中最大的字母。
# min(str)                                             返回字符串 str 中最小的字母。
# string.partition(str)                                有点像 find()和 split()的结合体,从 str 出现的第一个位置起,把 字 符 串 string 分 成 一 个 3 元 素 的 元 组 (string_pre_str,str,string_post_str),如果 string 中不包含str 则 string_pre_str == string.
# string.replace(str1, str2,  num=string.count(str1))  把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.
# string.rfind(str, beg=0,end=len(string) )            类似于 find()函数，不过是从右边开始查找.
# string.rindex( str, beg=0,end=len(string))           类似于 index()，不过是从右边开始.
# string.rjust(width)                                  返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
# string.rpartition(str)                               类似于 partition()函数,不过是从右边开始查找.
# string.rstrip()                                      删除 string 字符串末尾的空格.
# string.split(str="", num=string.count(str))          以 str 为分隔符切片 string，如果 num有指定值，则仅分隔 num 个子字符串
# string.splitlines(num=string.count('\n'))            按照行分隔，返回一个包含各行作为元素的列表，如果 num 指定则仅切片 num 个行.
# string.startswith(obj, beg=0,end=len(string))        检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查.
# string.strip([obj])                                  在 string 上执行 lstrip()和 rstrip()
# string.swapcase()                                    翻转 string 中的大小写
# string.title()                                       返回"标题化"的 string,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
# string.translate(str, del="")                        根据 str 给出的表(包含 256 个字符)转换 string 的字符,要过滤掉的字符放到 del 参数中
# string.upper()                                       转换 string 中的小写字母为大写
~~~

**2.列表**



```python
#创建
fruit = ['apple','pear','grape','orange']   

#切片
print(fruit[1])      #pear
print(fruit[1:3])    #['pear', 'grape']
print(fruit[-1])     #orange
print(fruit[:2])     #['apple', 'pear']

# 追加
fruit.append('peach')
print(fruit)         #['apple', 'pear', 'grape', 'orange', 'peach']

# 删除
fruit.remove('peach')   #删除指定的
print(fruit)         #['apple', 'pear', 'grape', 'orange']

fruit.pop()          #删除列表最后一个元素
print(fruit)         #['apple', 'pear', 'grape']

del fruit[2]         #删除指定的索引
print(fruit)         #['apple', 'pear']

# 插入
fruit.insert(1,'grape')   #把‘grape’加入到索引为1的位置
print(fruit)         #['apple', 'grape', 'pear']

# 修改
fruit[2] = 'orange'  #直接修改
print(fruit)         #['apple', 'grape', 'orange']

# 扩展
fruit1 = ['apple','orange']
fruit2 = ['pear','grape']
fruit1.extend(fruit2)
print(fruit1)         #['apple', 'orange', 'pear', 'grape']

# 统计
print(fruit1.count('apple'))    #1

# 排序
fruit1.sort()
print(fruit1)     #['apple', 'grape', 'orange', 'pear']

fruit1.reverse()
print(fruit1)     #['pear', 'orange', 'grape', 'apple']

# 获取下标
print(fruit1.index('apple'))    #3

# 同时获取下标和值
for index,item in enumerate(fruit1):
   print(index,item)
   
# 结果    
0 pear
1 orange
2 grape
3 apple
```



**3.元组**



```python
# 创建元组
fruit = ('apple','orange','grape')

# 常用功能
print(fruit.count('apple'))   #1
print(fruit.index('orange'))  #1
```



**4.字典**



```python
# 创建
fruit = {1:'apple',2:'orange',3:'grape'}
print(fruit)

# 增加
fruit[4] = 'pear'
print(fruit)      #{1: 'apple', 2: 'orange', 3: 'grape', 4: 'pear'}

# 修改
fruit[4] = 'peach'
print(fruit)      #{1: 'apple', 2: 'orange', 3: 'grape', 4: 'pear'}

# 删除
fruit.pop(4)       #删除指定的key
print(fruit)       #{1: 'apple', 2: 'orange', 3: 'grape'}

# 查找value
print(fruit.get(1))     #apple
```



```python
fruit = {1:'apple',2:'orange',3:'grape'}

# 循环 迭代字典
for k,v in fruit.items():
   print(k,v)

1 apple
2 orange
3 grape

#查找
for k in fruit.keys():
   print(k)

1
2
3

for v in fruit.values():
   print(v)
   
apple
orange
grape

# 查找是否存在键 可以不适用keys()直接使字典
if key in fruit:pass

# 字典排序
>>> d = {"c": 3, "a": 1, "f":6, "b": 0}
# 按照value排序
>>> sorted(d.items(), key=operator.itemgetter(1))
[('b', 0), ('a', 1), ('c', 3), ('f', 6)]
# 按照key排序
>>> sorted(d.items(), key=operator.itemgetter(0))
[('a', 1), ('b', 0), ('c', 3), ('f', 6)]
```



**5.集合**



```python
# 创建
fruit = set(['apple','orange','pear'])
print(fruit)         #{'orange', 'pear', 'apple'}

# 添加
fruit.add('grape')   #add只能添加一个
print(fruit)         #{'apple', 'orange', 'pear', 'grape'}

fruit.update(['peach','banana'])    #update添加多个
print(fruit)
{'banana', 'pear', 'apple', 'peach', 'grape', 'orange'}

# 删除
fruit.remove('banana')    #删除指定的
print(fruit)

fruit.pop()    #随机删除
print(fruit)
```



```python
num1 = set([11,22,33,44])
num2 = set([33,44,55,66])

# 并集
print(num1.union(num2))     #{66, 11, 22, 33, 44, 55}

# 差集
print(num1.difference(num2))    #{11, 22}

# 交集
print(num1.intersection(num2))   #{33, 44}
```

