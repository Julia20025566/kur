import tkinter as tk
from tkinter import ttk
from typing import List, Optional, Tuple, Callable
import functools
from models import *
from exeptions import InputError, InputPar
import hashlib

class Forms(tk.Frame):
    win = None
    but = None
    entry = None
    entry1 = None
    label1 = None
    label = None
    login = 0
    parol = 0
    btn_submit = None
    frm_form = None
    frm_buttons = None
    butt = []
    label3 = [
        "Дата:",
        "Время:",
        "Кабинет:",
        "Врач:"
    ]

    label_r = [
        "Полис пациента:",
        "Дата:",
        "Время:",
        "Кабинет:",
        "Врач:"
    ]

    dict_r = {
        "Полис пациента:":"",
        "Дата:": "",
        "Время:": "",
        "Кабинет:": "",
        "Врач:": ""
    }

    label_d = [
        "Время:",
        "Дни недели:",
        "Кабинет:"
    ]

    dict3 = {
        "Дата:": "",
        "Время:": "",
        "Кабинет:": "",
        "Врач:": ""
    }

    label4 = [
        "Дата:",
        "Время:",
        "Врач:",
        "Кабинет:",
    ]
    label5 = [
        "Дата:",
        "Рекомендации и назначенные лекарства:",
    ]
    dict5 = {
        "Дата:": '',
        "Рекомендации и назначенные лекарства:": '',
    }
    label7 = [
        "Врач:",
        "Дата:",
        "Рекомендации и назначенные лекарства:",
    ]
    labelp = ["Полис пациента:"]
    dictp = {"Полис пациента:": ""}
    label2 = [
        "Имя:",
        "Фамилия:",
        "Отчество:",
        "Адрес:",
        "Телефон:",
        "Пароль:",
        "Полис:",
    ]
    dict2 = {
        "Имя:": "",
        "Фамилия:": "",
        "Отчество:": "",
        "Адрес:": "",
        "Телефон:": "",
        "Пароль:": "",
        "Полис:": "",
    }
    labels = [
        "Дата:",
        "Диагноз:",
        "Заключение:",
    ]
    dicts = {
        "День:": "",
        "Диагноз:": "",
        "Заключение:": "",
    }
    entrybut = []
    label6 = []
    """Главный экран графического приложения"""
    def __init__(self, root):
        super().__init__(root)
        self.__root = root
        self.tree: Optional[ttk.Treeview] = None

    def close(self, event):
        for i, k in enumerate(self.label6):
            self.label6[i].destroy()
        for i, k in enumerate(self.entrybut):
            self.entrybut[i].destroy()
        if self.btn_submit != None:
            self.btn_submit.destroy()
        self.label6.clear()
        self.entrybut.clear()
        self.frm_form.destroy()
        if self.frm_buttons != None:
            self.frm_buttons.destroy()

    def exit_(self, event):
        self.win.destroy()

    def clear(self, event):
        for idx, text in enumerate(self.entrybut):
            self.entrybut[idx].delete(0, tk.END)

#############################################doctor
    def send_talon(self, event, pat):
        try:
            for idx, text in enumerate(self.label3):
                if self.entrybut[idx].get() != '':
                    self.dict3[text] = self.entrybut[idx].get()
                    print(self.dict3[text])
                else:
                    raise InputError("Invalid input", "Check the input fields!")
            create_talon(pat, self.dict3['Дата:'], self.dict3['Время:'], self.dict3['Кабинет:'], self.dict3['Врач:'])
            self.entrybut.clear()
            self.frm_form.destroy()
            self.frm_buttons.destroy()
        except InputError as e:
            e.subscribe()

    def add_talon(self, event, pat):
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
        self.frm_form.pack()
        for idx, text in enumerate(self.label3):
            label = tk.Label(master=self.frm_form, text=text)
            self.entrybut.append(tk.Entry(master=self.frm_form, width=50))
            label.grid(row=idx, column=0, sticky="e")
            self.entrybut[idx].grid(row=idx, column=1)
        self.frm_buttons = tk.Frame()
        self.frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
        btn_submit = tk.Button(master=self.frm_buttons, text="Отправить")
        btn_submit.bind("<Button-1>", functools.partial(self.send_talon, pat=pat))
        btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)
        btn_clear = tk.Button(master=self.frm_buttons, text="Очистить")
        btn_clear.bind("<Button-1>", self.clear)
        btn_clear.pack(side=tk.RIGHT, ipadx=10)

    def add_receipt(self, event, pat, doc):
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
        self.frm_form.pack()
        for idx, text in enumerate(self.label5):
            label = tk.Label(master=self.frm_form, text=text)
            self.entrybut.append(tk.Entry(master=self.frm_form, width=50))
            label.grid(row=idx, column=0, sticky="e")
            self.entrybut[idx].grid(row=idx, column=1)
        self.frm_buttons = tk.Frame()
        self.frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
        btn_submit = tk.Button(master=self.frm_buttons, text="Отправить")
        btn_submit.bind("<Button-1>", functools.partial(self.send_receipt, pat=pat, doc=doc))
        btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)
        btn_clear = tk.Button(master=self.frm_buttons, text="Очистить")
        btn_clear.bind("<Button-1>", self.clear)
        btn_clear.pack(side=tk.RIGHT, ipadx=10)

    def send_receipt(self, event, pat, doc):
        try:
            for idx, text in enumerate(self.label5):
                if self.entrybut[idx].get() != '':
                    self.dict5[text] = self.entrybut[idx].get()
                    print(self.dict5[text])
                else:
                    raise InputError("Invalid input", "Check the input fields!")
            create_receipt(pat, doc, self.dict5['Рекомендации и назначенные лекарства:'], self.dict5['Дата:'])
            self.entrybut.clear()
            self.frm_form.destroy()
            self.frm_buttons.destroy()
        except InputError as e:
            e.subscribe()

    def send_seek_hisory(self, event, doc, pat):
        try:
            for idx, text in enumerate(self.labels):
                if self.entrybut[idx].get() != '':
                    self.dicts[text] = self.entrybut[idx].get()
                    print(self.dicts[text])
                else:
                    raise InputError("Invalid input", "Check the input fields!")
            create_seek_history(pat, doc, self.dicts['Диагноз:'], self.dicts['Дата:'], self.dicts['Заключение:'])
            self.entrybut.clear()
            self.frm_form.destroy()
            self.frm_buttons.destroy()
        except InputError as e:
            e.subscribe()

    def seek_history(self, event, doc, pat):
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
        self.frm_form.pack()
        for idx, text in enumerate(self.labels):
            label = tk.Label(master=self.frm_form, text=text)
            self.entrybut.append(tk.Entry(master=self.frm_form, width=50))
            label.grid(row=idx, column=0, sticky="e")
            self.entrybut[idx].grid(row=idx, column=1)
        self.frm_buttons = tk.Frame()
        self.frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
        btn_submit = tk.Button(master=self.frm_buttons, text="Отправить")
        btn_submit.bind("<Button-1>", functools.partial(self.send_seek_hisory, doc=doc, pat=pat))
        btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)
        btn_clear = tk.Button(master=self.frm_buttons, text="Очистить")
        btn_clear.bind("<Button-1>", self.clear)
        btn_clear.pack(side=tk.RIGHT, ipadx=10)

    def doctor(self, event, key):
        try:
            pat_id = self.entry1.get()
            if is_patient(pat_id):
                self.entry1.delete(0, tk.END)
                self.frm_form.destroy()
                self.but.destroy()
                self.entry1.destroy()
                self.label1.destroy()
                frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=5)
                # Помещает рамку на окно приложения.
                frm_form.pack()
                self.butt.append(tk.Button(self.win, text="Посмотреть карту пациента"))
                self.butt[len(self.butt)-1].bind("<Button-1>", functools.partial(self.see_patient, key=pat_id))
                self.butt[len(self.butt)-1].pack()

                self.butt.append(tk.Button(self.win, text="Добавить запись в историю болезни"))
                self.butt[len(self.butt) - 1].bind("<Button-1>", functools.partial(self.seek_history, pat=pat_id, doc=key))
                self.butt[len(self.butt) - 1].pack()

                self.butt.append(tk.Button(self.win, text="Выписать рецепт"))
                self.butt[len(self.butt)-1].bind("<Button-1>", functools.partial(self.add_receipt, pat=pat_id, doc=key))
                self.butt[len(self.butt)-1].pack()

                self.butt.append(tk.Button(self.win, text="Выписать талон"))
                self.butt[len(self.butt)-1].bind("<Button-1>", functools.partial(self.add_talon, pat=pat_id))
                self.butt[len(self.butt)-1].pack()

                self.butt.append(tk.Button(self.win, text="Выход"))
                self.butt[len(self.butt)-1].bind("<Button-1>", self.exit_)
                self.butt[len(self.butt)-1].pack()

                self.butt.append(tk.Button(self.win, text="Назад"))
                self.butt[len(self.butt)-1].bind("<Button-1>", functools.partial(self.doc_back, doc=key))
                self.butt[len(self.butt)-1].pack()
            else:
                raise InputError("Invalid input", "Check the patient id!")
        except InputError as e:
            e.subscribe()

    def doc_back(self, event, doc):
        for index, t in enumerate(self.butt):
            self.butt[index].destroy()
        self.butt.clear()
        self.frm_form.destroy()
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
        self.frm_form.pack()
        self.label1 = tk.Label(text="Номер пациента")
        self.entry1 = tk.Entry()
        self.label1.pack()
        self.entry1.pack()
        self.but = tk.Button(self.win, text="Ok", bg="white", fg="blue")
        self.but.bind("<Button-1>", functools.partial(self.doctor, key=doc))
        self.but.pack()

    def doctor1(self, key):
        self.win = tk.Tk()
        self.win.title("Главная Доктора")
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
        self.frm_form.pack()
        self.label1 = tk.Label(text="Номер пациента")
        self.entry1 = tk.Entry()
        self.label1.pack()
        self.entry1.pack()
        self.but = tk.Button(self.win, text="Ok", bg="white", fg="blue")
        self.but.bind("<Button-1>", functools.partial(self.doctor, key=key))
        self.but.pack()
        self.win.mainloop()
######################################################

##############################################patient

    def op_talon(self, event, day, time, pat):
        print(time)
        for i, k in enumerate(self.butt):
            self.butt[i].destroy()
        self.frm_buttons.destroy()
        self.frm_form.destroy()
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
        self.frm_form.pack()
        for idx, text in enumerate(self.label4):
            self.label6.append(tk.Label(master=self.frm_form, text=text))
            self.entrybut.append(tk.Entry(master=self.frm_form, width=50))
            self.label6[idx].grid(row=idx, column=0, sticky="e")
            self.entrybut[idx].grid(row=idx, column=1)
        pat = find_talon(pat, day, time)
        for idx, text in enumerate(self.label4):
            self.entrybut[idx].insert(0, pat[0][text])
        self.frm_buttons = tk.Frame()
        self.frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
        self.btn_submit = tk.Button(master=self.frm_buttons, text="Закрыть")
        self.btn_submit.bind("<Button-1>", self.close)
        self.btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

    def choose_time(self, event, day, pat):
        print(day)
        for i, k in enumerate(self.butt):
            self.butt[i].destroy()
        self.frm_buttons.destroy()
        self.frm_form.destroy()
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
        self.frm_form.pack()
        self.frm_buttons = tk.Frame()
        self.frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
        pat = find_time(pat, day)
        for c, d in enumerate(pat):
            print(c)
            print(d)
            self.butt.append(tk.Frame())
            self.butt[c] = tk.Button(master=self.frm_buttons, text=d)
            self.butt[c].bind("<Button-1>", functools.partial(self.op_talon, day=day, time=d, pat=pat))
            self.butt[c].pack(side=tk.BOTTOM, ipadx=5, ipady=5)

    def op_receipt(self, event, day, key):
        for i, k in enumerate(self.butt):
            self.butt[i].destroy()
        self.frm_buttons.destroy()
        self.frm_form.destroy()
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
        self.frm_form.pack()
        for idx, text in enumerate(self.label7):
            self.label6.append(tk.Label(master=self.frm_form, text=text))
            self.entrybut.append(tk.Entry(master=self.frm_form, width=50))
            self.label6[idx].grid(row=idx, column=0, sticky="e")
            self.entrybut[idx].grid(row=idx, column=1)
        pat = find_receipt(key, day)
        for idx, text in enumerate(self.label7):
            self.entrybut[idx].insert(0, pat[0][text])
        self.frm_buttons = tk.Frame()
        self.frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
        self.btn_submit = tk.Button(master=self.frm_buttons, text="Закрыть")
        self.btn_submit.bind("<Button-1>", self.close)
        self.btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

    def see_schedule(self, event):
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
        self.frm_form.pack()
        pat = get_all_doc()
        self.frm_buttons = tk.Frame()
        self.frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
        for c, d in enumerate(pat):
            self.butt.append(tk.Frame())
            self.butt[c] = tk.Button(master=self.frm_buttons, text=d[1])
            self.butt[c].bind("<Button-1>", functools.partial(self.see_schedule_doc, doc=d[0]))
            self.butt[c].pack(side=tk.BOTTOM, ipadx=5, ipady=5)

    def see_schedule_doc(self, event, doc):
        for i, k in enumerate(self.butt):
            self.butt[i].destroy()
        self.frm_buttons.destroy()
        self.frm_form.destroy()
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
        self.frm_form.pack()
        for idx, text in enumerate(self.label_d):
            self.label6.append(tk.Label(master=self.frm_form, text=text))
            self.entrybut.append(tk.Entry(master=self.frm_form, width=50))
            self.label6[idx].grid(row=idx, column=0, sticky="e")
            self.entrybut[idx].grid(row=idx, column=1)
        pat = get_schedule(doc)
        for idx, text in enumerate(self.label_d):
            self.entrybut[idx].insert(0, pat[0][text])
        self.frm_buttons = tk.Frame()
        self.frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
        self.btn_submit = tk.Button(master=self.frm_buttons, text="Закрыть")
        self.btn_submit.bind("<Button-1>", self.close)
        self.btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

    def see_talon(self, event, key):
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
        self.frm_form.pack()
        pat = find_date(key)
        print(pat)
        self.frm_buttons = tk.Frame()
        self.frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
        for c, d in enumerate(pat):
            print(c)
            print(d)
            self.butt.append(tk.Frame())
            self.butt[c] = tk.Button(master=self.frm_buttons, text=d)
            self.butt[c].bind("<Button-1>", functools.partial(self.choose_time, day=d, pat=key))
            self.butt[c].pack(side=tk.BOTTOM, ipadx=5, ipady=5)

    def see_receipt(self, event, key):
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
        self.frm_form.pack()
        self.frm_buttons = tk.Frame()
        self.frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
        pat = find_date_r(key)
        for c, d in enumerate(pat):
            self.butt.append(tk.Frame())
            self.butt[c] = tk.Button(master=self.frm_buttons, text=d)
            self.butt[c].bind("<Button-1>", functools.partial(self.op_receipt, day=d, key=key))
            self.butt[c].pack(side=tk.BOTTOM, ipadx=5, ipady=5)


    def see_patient(self, event, key):
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
        self.frm_form.pack()
        for idx, text in enumerate(self.label2):
            label = tk.Label(master=self.frm_form, text=text)
            self.entrybut.append(tk.Entry(master=self.frm_form, width=50))
            label.grid(row=idx, column=0, sticky="e")
            self.entrybut[idx].grid(row=idx, column=1)
        self.frm_buttons = tk.Frame()
        self.frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
        pat = find_patient(key)
        for idx, text in enumerate(self.label2):
            self.entrybut[idx].insert(0, pat[0][text])
        btn_submit = tk.Button(master=self.frm_buttons, text="Закрыть")
        btn_submit.bind("<Button-1>", self.close)
        btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

    def op_seek_his(self, event, day, key):
        for i, k in enumerate(self.butt):
            self.butt[i].destroy()
        self.frm_buttons.destroy()
        self.frm_form.destroy()
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
        self.frm_form.pack()
        for idx, text in enumerate(self.labels):
            self.label6.append(tk.Label(master=self.frm_form, text=text))
            self.entrybut.append(tk.Entry(master=self.frm_form, width=50))
            self.label6[idx].grid(row=idx, column=0, sticky="e")
            self.entrybut[idx].grid(row=idx, column=1)
        self.label6.append(tk.Label(master=self.frm_form, text='Врач:'))
        self.entrybut.append(tk.Entry(master=self.frm_form, width=50))
        self.label6[len(self.label6)-1].grid(row=len(self.label6)-1, column=0, sticky="e")
        self.entrybut[len(self.label6)-1].grid(row=len(self.label6)-1, column=1)
        pat = find_seek_his(key, day)
        for idx, text in enumerate(self.labels):
            self.entrybut[idx].insert(0, pat[0][text])
        self.entrybut[len(self.label6)-1].insert(0, pat[0]['Врач:'])
        self.frm_buttons = tk.Frame()
        self.frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
        self.btn_submit = tk.Button(master=self.frm_buttons, text="Закрыть")
        self.btn_submit.bind("<Button-1>", self.close)
        self.btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

    def see_seek_his(self, even, pat):
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
        self.frm_form.pack()
        self.frm_buttons = tk.Frame()
        self.frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
        pat = find_date_sh(pat)
        for c, d in enumerate(pat):
            self.butt.append(tk.Frame())
            self.butt[c] = tk.Button(master=self.frm_buttons, text=d)
            self.butt[c].bind("<Button-1>", functools.partial(self.op_seek_his, day=d, key=pat))
            self.butt[c].pack(side=tk.BOTTOM, ipadx=5, ipady=5)

    def patient(self, key):
        self.win = tk.Tk()
        self.win.title("Главная Пациента")
        frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=5)
        # Помещает рамку на окно приложения.
        frm_form.pack()
        but1 = tk.Button(self.win)
        but1["text"] = "Посмотреть мою карту"
        but1.bind("<Button-1>", functools.partial(self.see_patient, key=key))
        but1.pack()

        but4 = tk.Button(self.win)
        but4["text"] = "Посмотреть рецепт"
        but4.bind("<Button-1>", functools.partial(self.see_receipt, key=key))
        but4.pack()

        but2 = tk.Button(self.win)
        but2["text"] = "Посмотреть талон"
        but2.bind("<Button-1>", functools.partial(self.see_talon, key=key))
        but2.pack()

        but2 = tk.Button(self.win)
        but2["text"] = "Посмотреть график работы врачей"
        but2.bind("<Button-1>", functools.partial(self.see_schedule))
        but2.pack()

        but5 = tk.Button(self.win)
        but5["text"] = "Посмотреть историю болезни"
        but5.bind("<Button-1>", functools.partial(self.see_seek_his, pat=key))
        but5.pack()

        but3 = tk.Button(self.win)
        but3["text"] = "Выход"
        but3.bind("<Button-1>", self.exit_)
        but3.pack()
        self.win.mainloop()

##########################################################

############################################registrator
    def delete_patient(self, event):
        try:
            for idx, text in enumerate(self.labelp):
                if self.entrybut[idx].get() != '':
                    self.dictp[text] = self.entrybut[idx].get()
                    print(self.dictp[text])
                else:
                    raise InputError("Invalid input", "Check the input fields!")
            delete_patient_(self.dictp['Полис пациента:'])
            self.entrybut.clear()
            self.frm_form.destroy()
            self.frm_buttons.destroy()
        except InputError as e:
            e.subscribe()

    def delete_talon(self, event):
        try:
            for idx, text in enumerate(self.label_r):
                if self.entrybut[idx].get() != '':
                    self.dict3[text] = self.entrybut[idx].get()
                    print(self.dict3[text])
                else:
                    raise InputError("Invalid input", "Check the input fields!")
            delete_talon(self.dict3['ID пациента:'], self.dict3['Дата:'], self.dict3['Время:'], self.dict3['Кабинет:'], self.dict3['Врач:'])
            self.entrybut.clear()
            self.frm_form.destroy()
            self.frm_buttons.destroy()
        except InputError as e:
            e.subscribe()

    def send_talon_r(self, event):
        try:
            for idx, text in enumerate(self.label_r):
                if self.entrybut[idx].get() != '':
                    self.dict_r[text] = self.entrybut[idx].get()
                    print(self.dict_r[text])
                else:
                    raise InputError("Invalid input", "Check the input fields!")
            create_talon(self.dict_r['ID пациента:'], self.dict_r['Дата:'], self.dict_r['Время:'], self.dict_r['Кабинет:'], self.dict_r['Врач:'])
            self.entrybut.clear()
            self.frm_form.destroy()
            self.frm_buttons.destroy()
        except InputError as e:
            e.subscribe()

    def add_talon_r(self, event):
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
        self.frm_form.pack()
        for idx, text in enumerate(self.label_r):
            label = tk.Label(master=self.frm_form, text=text)
            self.entrybut.append(tk.Entry(master=self.frm_form, width=50))
            label.grid(row=idx, column=0, sticky="e")
            self.entrybut[idx].grid(row=idx, column=1)
        self.frm_buttons = tk.Frame()
        self.frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
        btn_submit = tk.Button(master=self.frm_buttons, text="Отправить")
        btn_submit.bind("<Button-1>", self.send_talon_r)
        btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)
        btn_clear = tk.Button(master=self.frm_buttons, text="Очистить")
        btn_clear.bind("<Button-1>", self.clear)
        btn_clear.pack(side=tk.RIGHT, ipadx=10)

    def del_talon(self, event):
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
        self.frm_form.pack()
        for idx, text in enumerate(self.label_r):
            label = tk.Label(master=self.frm_form, text=text)
            self.entrybut.append(tk.Entry(master=self.frm_form, width=50))
            label.grid(row=idx, column=0, sticky="e")
            self.entrybut[idx].grid(row=idx, column=1)
        self.frm_buttons = tk.Frame()
        self.frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
        btn_submit = tk.Button(master=self.frm_buttons, text="Удалить")
        btn_submit.bind("<Button-1>", self.delete_talon)
        btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)
        btn_clear = tk.Button(master=self.frm_buttons, text="Очистить")
        btn_clear.bind("<Button-1>", self.clear)
        btn_clear.pack(side=tk.RIGHT, ipadx=10)

    def del_patient(self, event):
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
        self.frm_form.pack()
        for idx, text in enumerate(self.labelp):
            label = tk.Label(master=self.frm_form, text=text)
            self.entrybut.append(tk.Entry(master=self.frm_form, width=50))
            label.grid(row=idx, column=0, sticky="e")
            self.entrybut[idx].grid(row=idx, column=1)
        self.frm_buttons = tk.Frame()
        self.frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
        btn_submit = tk.Button(master=self.frm_buttons, text="Удалить")
        btn_submit.bind("<Button-1>", self.delete_patient)
        btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)
        btn_clear = tk.Button(master=self.frm_buttons, text="Очистить")
        btn_clear.bind("<Button-1>", self.clear)
        btn_clear.pack(side=tk.RIGHT, ipadx=10)

    def add_patient(self, event):
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
        self.frm_form.pack()
        for idx, text in enumerate(self.label2):
            # Создает ярлык с текстом из списка ярлыков.
            label = tk.Label(master=self.frm_form, text=text)
            # Создает текстовое поле которая соответствует ярлыку.
            # entry = tk.Entry(master=self.frm_form, width=50)
            self.entrybut.append(tk.Entry(master=self.frm_form, width=50))
            # Использует менеджер геометрии grid для размещения ярлыков и
            # текстовых полей в строку, чей индекс равен idx.
            label.grid(row=idx, column=0, sticky="e")
            # entry.grid(row=idx, column=1)
            self.entrybut[idx].grid(row=idx, column=1)
        self.frm_buttons = tk.Frame()
        self.frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

        btn_submit = tk.Button(master=self.frm_buttons, text="Отправить")
        btn_submit.bind("<Button-1>", self.send_patient)
        btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

        btn_clear = tk.Button(master=self.frm_buttons, text="Очистить")
        btn_clear.bind("<Button-1>", self.clear)
        btn_clear.pack(side=tk.RIGHT, ipadx=10)

    def send_patient(self, event):
        try:
            for idx, text in enumerate(self.label2):
                if self.entrybut[idx].get() != '':
                    self.dict2[text] = self.entrybut[idx].get()
                else:
                    raise InputError("Invalid input", "Check the input fields!")
            parol1 = hashlib.md5(self.dict2['Пароль:'].encode()).hexdigest()
            create_patient(self.dict2['Имя:'], self.dict2['Фамилия:'], self.dict2['Отчество:'], self.dict2['Адрес:'],
                           self.dict2['Телефон:'], parol1, self.dict2['Полис:'])
            self.entrybut.clear()
            self.frm_form.destroy()
            self.frm_buttons.destroy()
        except InputError as e:
            e.subscribe()

    def registrator(self):
        self.win = tk.Tk()
        self.win.title("Главная Регистратора")
        frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=10)
        frm_form.pack()
        but1 = tk.Button(self.win)
        but1["text"] = "Добавить пациента"
        but1.bind("<Button-1>", self.add_patient)
        but1.pack(side=tk.TOP)

        but4 = tk.Button(self.win)
        but4["text"] = "Удалить пациента"
        but4.bind("<Button-1>", self.del_patient)
        but4.pack(side=tk.TOP)

        but2 = tk.Button(self.win)
        but2["text"] = "Добавить талон"
        but2.bind("<Button-1>", self.add_talon_r)
        but2.pack(side=tk.TOP)

        but5 = tk.Button(self.win)
        but5["text"] = "Удалить талон"
        but5.bind("<Button-1>", self.del_talon)
        but5.pack(side=tk.TOP)

        but3 = tk.Button(self.win)
        but3["text"] = "Выход"
        but3.bind("<Button-1>", self.exit_)
        but3.pack(side=tk.TOP)
        self.win.mainloop()
    ####################################################################################
    def init(self, event):
        self.login = self.entry.get()
        parol = self.entry1.get()
        self.parol = hashlib.md5(parol.encode()).hexdigest()
        try:
            if self.login != '' and self.parol != '':
                if is_doctor(self.login):
                    if true_parol_d(self.login, self.parol):
                        self.__root.destroy()
                        self.doctor1(self.login)
                    else:
                        raise InputPar("Invalid input", "Incorrect parol!")
                elif is_patient(self.login):
                    if true_parol_p(self.login, self.parol):
                        self.__root.destroy()
                        self.patient(self.login)
                    else:
                        raise InputPar("Invalid input", "Incorrect parol!")
                elif is_registrator(self.login):
                    if true_parol_r(self.login, self.parol):
                        self.__root.destroy()
                        self.registrator()
                    else:
                        raise InputPar("Invalid input", "Incorrect parol!")
                else:
                    raise InputPar("Invalid input", "Incorrect login!")
            else:
                raise InputError("Invalid input", "Input login or parol!")
        except (InputError, InputPar) as e:
            e.subscribe()
            self.entry.delete(0, tk.END)
            self.entry1.delete(0, tk.END)


    def createPanelWithButton(self):
        self.label = tk.Label(text="Логин")
        self.entry = tk.Entry()
        self.label.pack()
        self.entry.pack()

        self.label1 = tk.Label(text="Пароль")
        self.entry1 = tk.Entry(show='*')
        self.label1.pack()
        self.entry1.pack()
        but1 = tk.Button(self.__root, text="Ok", bg="white", fg="blue")
        but1.bind("<Button-1>", self.init)
        but1.pack()
