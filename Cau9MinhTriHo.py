import os
import time
a='n'
while (a !='Y' and a!='y'):
    a= input("Tắt máy hoặc bị nguyền! (y/n): ")
    print('lời nguyền sẽ trở lại trong 30s nữa...')
    time.sleep(30)
print('Tắt máy!')
os.system('shutdown -s')
