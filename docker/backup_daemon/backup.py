
#daemon script to backup the database at 1:00 AM every day

import os
import time
import datetime

def backup(src_dir, dst_dir="/backup/"):
    now = datetime.datetime.now()
    folder = dst_dir + now.strftime("%Y-%m-%d") + "/"
    if not os.path.exists(folder):
        os.makedirs(folder)
    os.system("tar -zcf " + folder + now.strftime("%H-%M-%S") + ".tar.gz " + src_dir)
    print("Backup completed")

src_dir = "/data/"
time.sleep(20)
while True:
    now = datetime.datetime.now()
    if now.hour == 1 and now.minute == 0:
        backup(src_dir)
    time.sleep(30)