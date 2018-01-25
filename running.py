import Tkinter as tk
import win32api,win32con
import time
import json
f=open('harsh.json','r')
data=json.load(f)
print(data)
for i in data:
    print(i[0],i[1])
    win32api.SetCursorPos((i[0],i[1]))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,i[0],i[1],0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,i[0],i[1],0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,i[0],i[1],0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,i[0],i[1],0,0)
    time.sleep(2)

#while True:



