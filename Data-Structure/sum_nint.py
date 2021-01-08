def sum_n_int(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
        print(i)
    return sum

print(sum_n_int(10))