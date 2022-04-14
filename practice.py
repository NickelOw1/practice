from tkinter import *
from tkinter import messagebox
from scipy import integrate
import math
import numpy as np
import matplotlib.pyplot as plt
vecsin = np.vectorize(math.sin)
f = 50
t = np.linspace(0, 10, 50)

def show_graph():
    plt.plot(t, int(umax.get())*vecsin(2*math.pi*f*t)+(int(umax.get())/10)*vecsin(6*math.pi*f*t)) # построение графика
    plt.show()

def func(t):
    return ((int(umax.get())*math.sin(2*math.pi*f*t)+(int(umax.get())/10)*math.sin(6*math.pi*f*t))**2)/int(res.get())

def show_int_result():
    messagebox.showinfo("Результат вычисления", integrate.quad(func, 0, int(time.get())));

root = Tk()
root.title("GUI на Python")
root.geometry("300x400")

time = IntVar()
res = IntVar()
umax = IntVar()

time_entry = Entry(textvariable=time)
time_entry.grid(row = 1, column = 1, columnspan = 1)

res_entry = Entry(textvariable=res)
res_entry.grid(row = 2, column = 1, columnspan = 1)

umax_entry = Entry(textvariable=umax)
umax_entry.grid(row = 3, column = 1, columnspan = 1)
Label(text="Время:").grid(row=1, column=0)
Label(text="Сопротивление:").grid(row=2, column=0)
Label(text="Максимальное напряжение:").grid(row=3, column=0)
int_button = Button(text="Вычислить интеграл", command=show_int_result)
int_button.place(relx=.5, rely=.5, anchor="c")
graph_button = Button(text="Построить график", command=show_graph)
graph_button.place(relx=.5, rely=.6, anchor="c")


root.mainloop()
