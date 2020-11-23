import os
import time
for i in range(100000000000):
    a= input("Tắt máy hoặc bị nguyền! (y/n): ")
    if (a =='Y' or a=='y'):
        print('tắt đi!')
        os.system('shutdown -s')
        break
    else:
        print('Lời nguyền sẽ trở lại trong 30s tới!')
        time.sleep(30)
