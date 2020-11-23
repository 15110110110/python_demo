# coding:utf-8
import tkinter as Tk
from tkinter import ttk as TTK
import tkMessageBox as message
import DataBaseHandle as Db
import sys
import time

timestamp = time.time()
timeArray = time.localtime(timestamp)
date = time.strftime('%Y-%m-%d', timeArray)

db = Db.DataBaseHandle()


def dd(d=''):
    print type(d), d
    sys.exit()


def create_excel():
    message.showinfo('通知', '开始生成')


def error_msg(msg):
    message.showerror('错误信息', msg)


def check_form(pj_name, task_type, select_val, d_time):
    d_count_ = d_time.count('-')
    get_tache_sql = "select id from oa_tache where `explain` = '%s'" % (select_val)
    print get_tache_sql
    tache_data = db.find(get_tache_sql)
    get_pj_sql = "select id from oa_project where project_name = '%s'" % (pj_name)
    print get_pj_sql
    pj_data = db.find(get_pj_sql)
    if not pj_data:
        error_msg('项目名称输入错误')
        return
    else:
        project_id = pj_data['id']
    if not tache_data:
        error_msg('环节错误')
    else:
        tache_id = tache_data['id']
    if d_count_ != 2:
        error_msg('日期格式不正确')
        return


if __name__ == '__main__':
    get_tache_sql = 'select `explain` from oa_tache where id not in (15,27)'
    db = Db.DataBaseHandle()
    tache_data = db.selectDb(get_tache_sql)
    new_tache = []
    for t in tache_data:
        new_tache.append(t['explain'])
    tache_data = tuple(new_tache)
    window = Tk.Tk()
    window.geometry('500x400')
    x = 100
    y = 15
    project_name = Tk.StringVar()
    date_time = Tk.StringVar()
    status = Tk.StringVar()
    Tk.Label(window, text='项目名称：').place(x=x, y=y)
    project_name.set('请输入项目')
    Tk.Entry(window, textvariable=project_name).place(x=220, y=15)
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
    clist.grid(padx=220, pady=100)
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
    project_name_val = project_name.get()
    task_type = type_val.get()
    select_val = clist.get()
    print select_val
    date_val = date_time.get()
    button1 = Tk.Button(window, text='生成EXCEL', bg='#00FFFF',
                        command=lambda: check_form(project_name_val, task_type, select_val, date_val))
    button1.place(x=x, y=y)
    window.mainloop()
