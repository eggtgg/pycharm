import os
import time
while 1==1:
    a= input("Tắt máy hoặc bị nguyền! (y/n): ")
    if (a=="Y" or a=='y'):
        break
    print('lời nguyền sẽ trở lại trong 30s nữa...')
    time.sleep(1)
print('Tắt máy!')
os.system('shutdown -s')
