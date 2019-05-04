## 连接示例

```python
import paramiko,time

# 定义一个类，表示一台远端linux主机
class Linux(object):
    # 通过IP, 用户名，密码，超时时间初始化一个远程Linux主机
    def __init__(self, ip, username, password, timeout=30):
        self.ip = ip
        self.username = username
        self.password = password
        self.timeout = timeout
        # transport和channelel
        self.t = ''
        self.channel = ''
        # 链接失败的重试次数
        self.try_times = 3
 
     # 调用该方法连接远程主机
    def connect(self):
        while True:
            # 连接过程中可能会抛出异常，比如网络不通、链接超时
            try:
                self.t = paramiko.Transport(sock=(self.ip, 22))
                self.t.connect(username=self.username, password=self.password)
                self.channel = self.t.open_session()
                self.channel.settimeout(self.timeout)
                self.channel.get_pty()
                self.channel.invoke_shell()
                # 如果没有抛出异常说明连接成功，直接返回
                print( u'连接%s成功' % self.ip)
                # 接收到的网络数据解码为str
                print( self.channel.recv(65535).decode('utf-8'))
                return
            # 这里不对可能的异常如socket.error, socket.timeout细化，直接一网打尽
            except Exception:
                if self.try_times != 0:
                    print( u'连接%s失败，进行重试' %self.ip)
                    self.try_times -= 1
                else:
                    print( u'重试3次失败，结束程序')
                    exit(1)
 
     # 断开连接
    def close(self):
        self.channel.close()
        self.t.close()
 
    # 发送要执行的命令
    def send(self, cmd):
        cmd += '\r'
        result = ''
        # 发送要执行的命令
        self.channel.send(cmd)
        # 回显很长的命令可能执行较久，通过循环分批次取回回显,执行成功返回true,失败返回false
        while True:
            time.sleep(0.5)
            ret = self.channel.recv(65535)
            #print(11111111111111111111,ret,222222222222222222)
            ret = ret.decode('utf8','ignore')
            result += ret
            return result
 
# 连接正常的情况
if __name__ == '__main__':
    host = Linux(ip, user, passwd) #传入Ip，用户名，密码
    host.connect()

    host.send(cmd1);time.sleep(0.5)
    host.send(cmd2);time.sleep(1)
    result=host.send(cmd3)
    print( "返回的结果--")
    print( result)
    
    host.close()

```

