rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print(rows_by_fname)
print(rows_by_uid)

rows_by_lname_fname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lname_fname)

rows_lambda_fname = sorted(rows, key=lambda r : r['fname'])
rows_lambda_fname_lname = sorted(rows, key=lambda r : (r['fname'], r['lname']))

print(f"this is lambda multiple key -> {rows_lambda_fname_lname}")

print(max(rows, key=itemgetter('uid')))