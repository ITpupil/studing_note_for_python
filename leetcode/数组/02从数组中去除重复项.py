a=[0,0,1,1,1,2,3,3,4]
# 假设要将a若存在重复的项去掉，只留下没有发生重复的项 ，即结果：a=[4]

def solution(array):
    from collections import Counter #Counter会统计元素出现的次数并转化为字典
    res = Counter(array)
    new_array=[]
    for i in res:#这里i默认为res的key 【也就是数组中的元素】 而不用使用keys()方法
        if res[i]==1:
            new_array.append(i)
    return new_array

print(solution(a))