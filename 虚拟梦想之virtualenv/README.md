## 虚拟梦想之virtualenv

`virtualenv`在python dev中起到一个生产虚拟环境的作用。

​	这里为什么称之为虚拟梦想？主要原因是他的虚拟和我心中的虚拟不太一致，不是我想要的虚拟理解差异如下：

| 想象之中的                     | virtualenv实现的                                 |
| ------------------------------ | ------------------------------------------------ |
| 虚拟环境，可随意指定python版本 | 虚拟环境只是克隆了主机python版本                 |
|                                | 提供了一个纯净的dev空间                          |
|                                | 这个空间可以安装不同的软件包，如jina2.0 /jina3.0 |



## 指令总结

1. 安装virtualenv


- python3.6.3版本自带了pip，为了减少安装步骤，使用pip安装；

- cmd，打开windows命令行；安装完成后，输入pip list,查看当前的所有安装的包；

```python
pip install virtualenv
pip install virtualenvwrapper  # 这是对virtualenv的封装版本，一定要在virtualenv后安装 
```
2. 创建虚拟环境
   选择一个用来存放虚拟环境的文件，如E:/python3，`cd E:python3`  # 进入该文件<br>

   ​	`virtualenv envname`   # 创建一个名字为envname的虚拟环境<br>
   ​	`virtualenv --no-site-packages venv` #不带任何第三方包的“干净”的Python运行环境<br>

   ​	`virtualenv -p python2 envname`  # 如果安装了多个python版本，如py2和py3，需要指定使用哪个创建虚拟环境<br>

**注意**：

​	如果不识别`virtualenv`命令，可能是python安装路径没添加到系统环境变量或没安装`virtualenv`或没有重新打开一个 cmd 窗口；

3. 启动虚拟环境
```python
cd envname # 进入虚拟环境文件
cd Scripts # 进入相关的启动文件夹

activate  # 启动虚拟环境
deactivate # 退出虚拟环境

#或者使用source 
source venv/bin/activate #会修改相关环境变量，让命令python和pip均指向当前的virtualenv环境
```