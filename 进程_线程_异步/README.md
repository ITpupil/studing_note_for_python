# 进程、线程、异步学习

​	今天学到Python中进程线程的处理，突发奇想`python中多进程和多线程谁快呢？`

和粉丝交流，他觉得是进程，而我觉得是线程，具体理由忘了。

​	于是在网上查找资料，现将自己的理解总结下。

- 谁快，本质上是这些方式谁更加充分的利用的CPU
- 一个CPU，某一个时间点，只处理一个进程
- CPU是多任务的，即CPU的处理速度很快，可以操作多个程序
- 进程占用CPU时，一般情况下CPU还有很富裕资源，要想充分利用怎么办——多线程
- 异步是一个线程没有释放，CPU开启其他的线程让程序继续执行，而不是按照顺序等待线程资源释放



## 目录结构

- [多线程](多线程.md)
- [异步](异步.md)
- [扩展：协程](扩展：协程.md)
- [扩展：yield_from例子](扩展：yield_from例子.md)



## 多线程 Threading
- 引用 `import threading`
- 获取当前线程 `threading.current_thread()`
- 获取当前线程的名字 `threading.current_thread().name`
- 创建一个线程：`t = threading.Thread(target=loop, name='自定义名字')`，name参数可不写
- 调用一个线程：`t.start()`
- 线程同步：`t.join()`
- 主线程名字是`MainThread` 子线程name默认thread-1...

------

- 调用锁 Lock() ：`lock = threading.Lock()`
- 获取锁或者加锁：`lock.acquire()`
- 释放锁或者解锁：`lock.release()`
- 线程加锁后一定要解锁：`try...finally...`

------

- 由于GIL的原因，多线程无法利用多核进行并发，可采用多进程的方式

## 多进程 



## 异步