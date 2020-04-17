from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from data import total_status_by_country, total_status_by_country_excel, getCountries, just_global_excel, just_global
from ttkthemes import ThemedTk

window = ThemedTk(theme='arc')
window.title("Covid19")
window.geometry('640x420')

combo = Combobox(window, state="readonly",
                 values=getCountries(), width=36)
combo.current(0)
combo.place(x=200, y=25)


def country():
    if total_status_by_country_excel(combo.get(), combo.get()):
        total_status_by_country_excel(combo.get(), combo.get())
    else:
        messagebox.showinfo('Hata', 'Veri bulunamadı')


def global_data():
    just_global_excel()


def cond():
    if(combo.get() == "Global"):
        global_data()
    else:
        country()


# TreeView
tree = Treeview(window)
tree.place(y=100, x=80)

vsb = Scrollbar(window, orient="vertical", command=tree.yview)
vsb.place(x=544, y=133, height=226)
tree.configure(yscrollcommand=vsb.set)

tree["columns"] = ("one", "two", "three")
tree.column("#0", width=150, minwidth=150, stretch=NO)
tree.column("one", width=100, minwidth=100, stretch=NO)
tree.column("two", width=100, minwidth=100, stretch=NO)
tree.column("three", width=100, minwidth=100)

tree.heading("#0", text="Country", anchor=W)
tree.heading("one", text="Confirmed", anchor=W)
tree.heading("two", text="Deaths", anchor=W)
tree.heading("three", text="Recovered", anchor=W)


def show_info():
    if total_status_by_country(combo.get()) is not None:
        tree.insert("", "end", text=combo.get(), values=(total_status_by_country(combo.get())[0], total_status_by_country(combo.get())[1], total_status_by_country(combo.get())[2]))
    else:
        messagebox.showinfo('Hata', 'Veri bulunamadı')

def global_data_2():
    tree.insert("", "end", text=combo.get(), values=(
        just_global()[0], just_global()[1], just_global()[2]))


def cond_2():
    if(combo.get() == "Global"):
        global_data_2()
    else:
        show_info()
# TreeView


# Button
btn = Button(window, text="Export as Excel", command=cond)
btn.place(x=200, y=60)

show_info_btn = Button(window, text="Show Informations", command=cond_2)
show_info_btn.place(x=320, y=60)
# Button


window.mainloop()
