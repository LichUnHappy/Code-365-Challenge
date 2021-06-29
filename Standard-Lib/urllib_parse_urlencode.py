from urllib.parse import urlencode

query_args = {
    'q': 'query string',
    'foo': 'bar',
}

encoded_args = urlencode(query_args)
print('Encoded:', encoded_args)

query_args = {
    'foo': ['foo1', 'foo2'],
}

print('Single :', urlencode(query_args))
print('Single :', urlencode(query_args, doseq=True))
