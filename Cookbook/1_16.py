# 列表推导
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])
print([n for n in mylist if n < 0])

# 生成器表达式
pos = (n for n in mylist if n > 0)
print(pos)

for x in pos:
    print(x)

# 内建的filter() 函数
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

print(filter(is_int, values))

tmp = filter(is_int, values)
for x in tmp:
    print(x)

ivals = list(filter(is_int, values))
print(ivals)

# 过滤操作的一个变种就是将不符合条件的值用新的值代替，而不是丢弃它们。
clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress
more5 = [n>5 for n in counts]
print(more5)

tmp = compress(addresses, more5)
print(tmp)
print(list(tmp))