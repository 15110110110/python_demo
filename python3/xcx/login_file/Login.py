import tkinter as Tk
from PIL import Image, ImageTk

class Login_window():
    def __init__(self, window):
        self.window = window
        self.window.geometry('450x400')
        self.Login = Tk.Frame(self.window)
        self.Login.pack()
        # canvas = Tk.Canvas(self.Login, height=170, width=500)
        # photo = ImageTk.PhotoImage(Image.open('/Users/shihongxiao/www/python3/tkinter/1596616898432.jpg'))
        # image = canvas.create_image(0, 0, anchor='nw', image=photo)
        # canvas.pack(side='top')
        # self.var_user_name = Tk.StringVar()
        # self.var_user_name.set('请输入账号')
        # self.var_user_pwd = Tk.StringVar()
        # Tk.Label(self.Login, text='账号：').place(x=50, y=230)
        # Tk.Entry(self.Login, textvariable=self.var_user_name).place(x=100, y=230)
        # Tk.Label(self.Login, text='密码：').place(x=50, y=270)
        # Tk.Entry(self.Login, textvariable=self.var_user_pwd, show='*').place(x=100, y=270)
        # Tk.Button(self.Login, text='登录', command=self.login).place(x=50, y=310)
        btn = Tk.Button(self.Login, text='登录', command=self.login)
        btn.pack(anchor='center')


    def login(self):
        print(123)
