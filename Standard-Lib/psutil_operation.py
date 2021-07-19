## short command of psutil

import psutil

## CPU info
# cpu占用时间
psutil.cpu_times()
# 每个cpu占用时间
psutil.cpu_times(percpu=True)
# cpu逻辑数量
psutil.cpu_count()
# cpu物理数量
psutil.cpu_count(logical=False)
# cpu占比
psutil.cpu_percent()
# 每个cpu占比
psutil.cpu_percent(percpu=True)

## Memory
psutil.virtual_memory()

## Disk
# 分区
psutil.disk_partitions()
# 磁盘使用情况
psutil.disk_usage('/')
# 磁盘io
psutil.disk_io_counters()

## Network
# 获取网络读写字节数
psutil.net_io_counters()
# 获取网络接口信息
psutil.net_if_addrs()
# 获取网络接口状态
psutil.net_if_stats()
# 获取当前网络连接信息
psutil.net_connections()

## Process
# 获取所有进程的pid
for pid in psutil.pids():
    print(pid, end=',')
# 查找特定程序的相关i信息
for proc in psutil.process_iter(attrs=['pid', 'name', 'username']):
    if proc.info['name'].startswith('fuck'):
        print(proc.info)
# 获取特定pid的cpu占用
psutil.Process(12345).cpu_times()
# 获取特定pid的memory占用
psutil.Process(12345).memory_info()
# 获取线程数
psutil.Process(12345).num_threads()
# 获取内存占比
psutil.Process(12345).memory_percent()

