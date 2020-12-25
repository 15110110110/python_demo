import tkinter as Tk
from tkinter import ttk as TTK
import database.DataBaseHandle as Db
import sys
import time

timeStamp = time.time()
timeArr = time.localtime(timeStamp)
date = time.strftime('%Y-%m-%d', timeArr)

db = Db.DataBaseHandle()


def dd(d=''):
    print(type(d), d)
    sys.exit()


get_project_data_sql = 'select `project_name` from oa_project where is_show = 1'
project_data = db.selectDb(get_project_data_sql)
new_project = []
for p in project_data:
    new_project.append(p['project_name'])
new_project = tuple(new_project)
get_tache_sql = 'select `explain` from oa_tache where id not in (15,27)'
db = Db.DataBaseHandle()
tache_data = db.selectDb(get_tache_sql)
new_tache = []
for t in tache_data:
    new_tache.append(t['explain'])
tache_data = tuple(new_tache)
window = Tk.Tk(className='小脚本')
window.geometry('500x400')
x = 100
y = 15
project_name = Tk.StringVar()
date_time = Tk.StringVar()
status = Tk.StringVar()
Tk.Label(window, text='项目名称：').place(x=x, y=y)
# project_name.set('请输入项目')
# Tk.Entry(window, textvariable=project_name).place(x=220, y=15)
project_list = TTK.Combobox(window)
project_list['values'] = new_project
project_list.current(0)
project_list.grid(padx=220, pady=15)
y = y + 45
Tk.Label(window, text='选择类型：').place(x=x, y=y)
type_val = Tk.IntVar()
type_val.set(1)
Tk.Radiobutton(window, text='镜头', variable=type_val, value=1).place(x=220, y=50)
Tk.Radiobutton(window, text='资产', variable=type_val, value=2).place(x=300, y=50)
y = y + 45
Tk.Label(window, text='选择环节：').place(x=x, y=y)
clist = TTK.Combobox(window)
clist['values'] = tache_data
clist.current(0)
clist.grid(padx=220, pady=45)
y = y + 45
Tk.Label(window, text='输入日期：').place(x=x, y=y)
date_time.set(date)
Tk.Entry(window, textvariable=date_time).place(x=220, y=150)
y = y + 45
Tk.Label(window, text='输入状态：').place(x=x, y=y)
status.set('制作中')
Tk.Entry(window, textvariable=status).place(x=220, y=200)
y = y + 105
x = x + 100


def create_excel():
    project_val = project_list.get()
    print(project_val)


button1 = Tk.Button(window, text='生成excel', command=create_excel)
button1.place(x=x, y=y)

window.mainloop()
