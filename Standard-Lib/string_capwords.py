import string

s = 'The quick brown fox jump over the lazy dog.'

print(s)
# Capitalize each word splitted by space
print(string.capwords(s))
# Capitalize the 1st word 
print(s.capitalize())
# Split, cap and join
space = ' '
list = []
for ele in s.split():
    list.append(ele.capitalize())
print(space.join(list))
