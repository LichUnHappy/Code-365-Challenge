# ftpserver

# import pyftpdlib
# print(pyftpdlib.__path__)

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler, ThrottledDTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.log import LogFormatter
import logging

# 记录日志，输出到屏幕和文件
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
fh = logging.FileHandler(filename='myftpserver111.log', encoding='utf-8')
fh.setLevel(logging.DEBUG)
ch.setFormatter(LogFormatter())
fh.setFormatter(LogFormatter())
# 输出到屏幕
logger.addHandler(ch)
# 输出到文件
logger.addHandler(fh)

# 实例化虚拟用户，以通过FTP验证
authorizer = DummyAuthorizer()
# 添加用户权限和路径，（用户名、密码、用户目录、权限），可以为不同的用户添加不同的目录和权限
authorizer.add_user("user", "666666", "/", perm="elradfmw")
# 添加匿名用户，只需要路径
authorizer.add_anonymous("/")

# 初始化FTP句柄
handle = FTPHandler
handle.authorizer = authorizer

# 添加被动端口范围
handle.passive_ports = range(2000, 2333)

# 下载上传速度设置
dtp_handler = ThrottledDTPHandler
# 300kb/s
dtp_handler.read_limit = 300 * 1024
# 300kb/s
dtp_handler.write_limit = 300 * 1024
handle.dtp_handler = dtp_handler

# 监听ip和port
server = FTPServer(("0.0.0.0", 21), handle)

# 最大连接数
server.max_cons = 150
server.max_cons_per_ip = 15

# 开始服务，打印日志信息
server.serve_forever()


