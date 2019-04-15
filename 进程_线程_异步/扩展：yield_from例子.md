```python
final_result = {}

def sales_sum(product):
    total = 0
    nums = []
    while True:
        x = yield
        print(product+'销量：',x)
        if not x:
            break
        total += x
        nums.append(x)
    return total,nums

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
    for key,data_set in data_sets.items():
        print('start key:',key)
        m =middle(key)
        m.send(None)
        for value in data_set:
            m.send(value)
        m.send(None)
    print('final_result:',final_result)

main()
```
---
**运行结果如下：**

start key: 面膜
面膜销量： 1200
面膜销量： 1500
面膜销量： 3000
面膜销量： None
面膜销量统计完成
start key: 手机
手机销量： 28
手机销量： 21
手机销量： 65
手机销量： 37
手机销量： 87
手机销量： 66
手机销量： None
手机销量统计完成
start key: 内衣
内衣销量： 2312
内衣销量： 32
内衣销量： 324
内衣销量： 35
内衣销量： None
内衣销量统计完成
final_result: {'面膜': (5700, [1200, 1500, 3000]), '手机': (304, [28, 21, 65, 37, 87, 66]), '内衣': (2703, [2312, 32, 324, 35])}
[Finished in 0.2s]

---

**分析过程：**

TODO