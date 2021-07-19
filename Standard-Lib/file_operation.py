# -*- coding: utf-8 -*-

f = open("wb.txt", "w", encoding="utf-8")
f.write("测试w写入，如果文件存在，则清空内容后写入; 如果文件不存在，则创建\n")
f.close()

f = open("wb.txt", "a", encoding="utf-8")
f.write("测试a写入，如果文件存在，则追加; 如果文件不存在，则创建\n")
f.close()

f = open("wb.txt", "r", encoding="utf-8")
data = f.read()
print(type(data))
print(data)
f.close()

f = open("wb.txt", "rb")
data = f.read()
print(type(data))
print(data)
f.close()
