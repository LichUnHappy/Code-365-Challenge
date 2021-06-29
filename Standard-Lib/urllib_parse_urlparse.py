from urllib.parse import urlparse

url = "http://net.loc/path/s;param?query=arg#frag"
parsed = urlparse(url)
print(parsed)

url = "http://user:pwd@NetLoc:80/path;param?query=arg#frag"
parsed = urlparse(url)
print(parsed)

print(f"scheme -> {parsed.scheme}")
print(f"netloc -> {parsed.netloc}")
print(f"path -> {parsed.path}")
print(f"params -> {parsed.params}")
print(f"query -> {parsed.query}")
print(f"fragment -> {parsed.fragment}")
print(f"username -> {parsed.username}")
print(f"password -> {parsed.password}")
print(f"hostname -> {parsed.hostname}")
print(f"port -> {parsed.port}")