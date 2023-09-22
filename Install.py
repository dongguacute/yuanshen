import win32api
import win32con
import ctypes
import sys
import shutil
import os
import stat
import winreg
import subprocess
from tkinter.ttk import *
import tkinter.filedialog
import tkinter as tk


class mainThread:
    def __init__(self):
        self.dir = None
        self.path_old = os.getcwd()
        root = tk.Tk()
        root.title("输入希沃目录。")
        x = int((root.winfo_screenwidth() - root.winfo_reqwidth()) / 2)
        y = int((root.winfo_screenheight() - root.winfo_reqheight()) / 2)
        root.geometry("500x75")
        root.geometry("+{}+{}".format(x, y))
        self.entry = Entry(root)
        self.entry.pack(fill=tk.X, padx=30)
        f1 = Frame(root)
        f1.pack(side=tk.BOTTOM, pady=5)
        button = Button(f1, text="确定", command=self.get)
        button.grid(column=0, row=0, padx=3)
        button_dir = Button(f1, text="浏览目录...", command=self.browse_dir)
        button_dir.grid(column=1, row=0, padx=3)
        root.mainloop()
        os.makedirs("D:/seewo/check/")
        with open("D:/seewo/check/copy.text","w") as e:
            e.write(self.dir)


    def get(self):
        path = self.entry.get()

    def browse_dir(self):
        self.dir = tkinter.filedialog.askdirectory(mustexist=True, initialdir="C:\Program Files (x86)\Seewo\EasiNote5")
        self.entry.insert(0, self.dir)
        
    

if __name__ == '__main__':
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)

    except Exception:
        pass

    try:
        Admin = ctypes.windll.shell32.IsUserAnAdmin()

    except Exception:
        Admin = False

    if not Admin:
        win32api.MessageBox(0, "此程序需要管理员权限。", "错误: 过低的权限", win32con.MB_ICONHAND | win32con.MB_TOPMOST)
        sys.exit()

    mainThread()