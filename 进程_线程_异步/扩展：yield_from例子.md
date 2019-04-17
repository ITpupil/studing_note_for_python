```python
final_result = {}# 结果容器

def sales_sum(product):#对每个key求和
    total = 0
    nums = []
    while True:
        x = yield
        print(product+'销量：',x)
        if not x:
            break
        total += x
        nums.append(x)
    return total,nums #return 返回多个值得时候是个tuple对象

def middle(key):
    while True:
        final_result[key] = yield from sales_sum(key)
        print(key+'销量统计完成')

def main():
    data_sets={
        '面膜':[1200,1500,3000],
        '手机':[28,21,65,37,87,66],
        '内衣':[2312,32,324,35],
    }
    for key,data_set in data_sets.items():#迭代元数据
        print('start key:',key)
        m =middle(key)
        m.send(None)# 建立main 和 委托生成器 和子生成器的通道
        for value in data_set:
            m.send(value)# 和子生成器进行通信
        m.send(None)# 断开通道
    print('final_result:',final_result)

main()
```
---
**运行结果如下：**<br>

start key: 面膜<br>
面膜销量： 1200<br>
面膜销量： 1500<br>
面膜销量： 3000<br>
面膜销量： None<br>
面膜销量统计完成<br>
start key: 手机<br>
手机销量： 28<br>
手机销量： 21<br>
手机销量： 65<br>
手机销量： 37<br>
手机销量： 87<br>
手机销量： 66<br>
手机销量： None<br>
手机销量统计完成<br>
start key: 内衣<br>
内衣销量： 2312<br>
内衣销量： 32<br>
内衣销量： 324<br>
内衣销量： 35<br>
内衣销量： None<br>
内衣销量统计完成<br>
final_result: {'面膜': (5700, [1200, 1500, 3000]), '手机': (304, [28, 21, 65, 37, 87, 66]), '内衣': (2703, [2312, 32, 324, 35])}<br>
[Finished in 0.2s]<br>

---

**分析过程：**

TODO

