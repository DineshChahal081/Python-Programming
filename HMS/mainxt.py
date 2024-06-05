import platform
import psutil
from datetime import datetime

# print(platform.platform())
# print(platform.uname())
bootime = psutil.boot_time()
bt = datetime.fromtimestamp(bootime)
print(bt)