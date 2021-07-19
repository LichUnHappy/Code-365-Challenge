import os

# Naive
# with open('a.txt') as read_f, open('.a.txt.swap', 'w') as write_f:
    # data = read_f.read()
    # data = data.replace('str1', 'str2')

    # write_f.write(data)

# iter 写法
with open('a.txt') as read_f, open('.a.txt.swap'. 'w') as write_f:
    # 对可迭代对象逐行操作，防止内存溢出
    for line in read_f: 
        line = line.replace('str1', 'str2')

os.remove('a.txt')
os.rename('.a.txt.swap', 'a.txt')