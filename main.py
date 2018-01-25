import Tkinter as tk
import time
import win32api
import json
import _thread
main=tk.Tk()
main.title('Custom Automation')
main.geometry("300x80")
var=tk.StringVar()
list=[]
def cur_pos():
    while True:
        a=win32api.GetCursorPos()
        var.set(a)
        time.sleep(0.1)
def store_command():
    state_left=win32api.GetAsyncKeyState(0x01)
    while True:
        a=win32api.GetAsyncKeyState(0x01)
        if (a != state_left):
            state_left=a
            if(a<0):
                print()
                #print("left button clicked")
            else:
                list.append(win32api.GetCursorPos())
        time.sleep(0.1)

def start():
    _thread.start_new_thread(cur_pos,(),)
    _thread.start_new_thread(store_command,(),)

def stop():
    print(list)
    def save(event):
        widget=event.widget
        f=open(widget.get()+'.json','w')
        json.dump(list,f)
        _thread.exit()
    f2=tk.Frame()
    f2.pack()
    label=tk.Label(f2,text="Save as")
    label.pack()
    entry=tk.Entry(f2,width=20)
    entry.pack(side='bottom')
    entry.bind("<Return>",save)


frame=tk.Frame()
frame.pack()
btn=tk.Button(frame,text="start",command=start,relief=tk.SOLID)
btn.pack(side='left')

btn2=tk.Button(frame,text="stop",command=stop,relief=tk.SOLID)
btn2.pack(side='left')
label=tk.Label(frame,textvariable=var)
label.pack(side='left')
main.mainloop()
