# 执行外部命令 subprocess

# subprocess.run()
# subprocess.Popen()

import subprocess

a = subprocess.run("ls -l /dev/null", shell=True)