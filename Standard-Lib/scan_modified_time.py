import os 
import datetime

print(f"Current time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
for dirpath, dirname , files in os.walk(r"./"):
    for file in files:
        absPathFile = os.path.join(dirpath, file) 
        # print(absPathFile)
        modifiedTime = datetime.datetime.fromtimestamp(os.path.getmtime(absPathFile))
        now = datetime.datetime.now()
        diffTiime = now - modifiedTime
        # print(diffTiime)
        # print(diffTiime.days)
        # print(diffTiime.seconds)
        # print((diffTiime.seconds%3600)//60)

        print(f"{absPathFile}".ljust(25), f"Modified time:{modifiedTime.strftime('%Y-%m-%d %H:%M:%S')}", f"up to {diffTiime.days:3d} day {diffTiime.seconds//3600:2d} hours {(diffTiime.seconds%3600)//60:2d} minutes")