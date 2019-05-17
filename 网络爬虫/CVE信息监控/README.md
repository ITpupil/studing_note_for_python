# CVE 信息监控

参考：https://xz.aliyun.com/t/1902#toc-0

## 0x01  程序说明

- 一、入口程序：`cve.py`
  - 获取CVE信息的URL列表：`getCVES()`
  - 解析 CVE 信息，返回关键信息以便存储： `getCVEDetail(url)`
  - `main()` ：全流程执行脚本
  - `main2()`：全流程执行脚本 + 显示进度条
  - `main_only_query_data()`：用于已经完成数据采集后 再次发送邮件
- 二、数据存取程序：`cveMysqlPress.py`
  - `__init__`：初始化数据库连接，返回操作对象
  - `create_table(self,sql=SQL_TABLE_CREATED)`：创建数据库表
  - `insert_data(self,data)`：插入数据（插入前检查重复的CVE-ID `check_duplicate()`）
  - `query_data(self,updatetime=UPDATETIME)`：按照时间（YYYY-MM-DD）查询数据
- 三、邮件发送程序：`sendEmail.py`
  - `__init__`：初始化邮件发送服务
  - `outBase64(self,base64_string)`：解析base64字符串
  - `pressData(self)`：组装CVE信息的html表格
  - `send()`：发送邮件
- 四、配置文件：`config.py`
  - 数据库信息配置
  - 邮件客户端配置
  - 邮件信息组装配置

## 0x02   踩坑总结

- 一、base64编码时报错，base64处理的对象为bytes对象，转化时出现编码问题
  - `str(base64.b64encode(data.encode('utf-8')),'utf-8')`：编码时转变为str
  - `str(base64.b64decode(data),'utf-8')`：解码时转变为str
- 二、QQ邮箱是授权码，有的邮件服务器（如：某公司邮箱）没有设置，可以直接使用密码
- 三、组装HTML，使用CSS会报错key error?(忘记了)，可以在标签中进行配置style属性