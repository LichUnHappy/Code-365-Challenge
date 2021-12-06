# 解压可迭代对象赋值给多个变量

# 可变长元组的序列
# records = [
#     ('foo', 1, 2),
#     ('bar', 'hello'),
#     ('foo', 3, 4),
# ]

# def do_foo(x, y):
#     print('foo', x, y)

# def do_bar(s):
#     print('bar', s)

# for tag, *args in records:
#     if tag == 'foo':
#         do_foo(*args)
#     elif tag == 'bar':
#         do_bar(*args)

# 字符串操作
# line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
# uname, *fields, homedir, sh = line.split(':')
# print(uname)
# print(homedir)
# print(sh)

# placeholder
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)