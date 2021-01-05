# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 11:15:01 2018
Description:tkinter界面切换
Version:

@author: HJY
"""
import tkinter as tk
from PIL import Image, ImageTk
import xcx.login_file.Login as lw


class basedesk():
    def __init__(self, master):
        self.root = master
        self.root.config()
        self.root.title('Base page')

        lw.Login_window(self.root)


class initface():
    def __init__(self, master):
        self.master = master
        self.master.geometry('450x400')
        # 基准界面initface
        self.initface = tk.Frame(self.master, )
        self.initface.pack()
        btn = tk.Button(self.initface, text='登录', command=self.login)
        btn.pack()

    def login(self):
        self.initface.destroy()
        face1(self.master)


class face1():
    def __init__(self, master):
        self.master = master
        self.master.config(bg='blue')
        self.face1 = tk.Frame(self.master, )
        self.face1.pack()
        btn_back = tk.Button(self.face1, text='face1 back', command=self.back)
        btn_back.pack()

    def back(self):
        self.face1.destroy()
        initface(self.master)


if __name__ == '__main__':
    root = tk.Tk()
    basedesk(root)
    root.mainloop()