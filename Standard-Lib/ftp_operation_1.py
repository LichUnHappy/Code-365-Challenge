# ftpclinet

from ftplib import FTP

# login
ftp = FTP(host='localhost', user='user', passwd='666666')

# encode
ftp.encoding = 'utf-8'

# switch directory
ftp.cwd('/home/bullgo/Temporal/autopy')

# list the file 
# ftp.retrlines('LIST')

# Download file
ftp.retrbinary('RETR note.py', open('note.py', 'wb').write)

# Upload file
# ftp.storbinary('STOR 13.py', open('13.py', 'rb'))

# check the file under dir
for f in ftp.mlsd(path='/home/bullgo/Temporal/autopy'):
    print(f)

