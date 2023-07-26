import tkinter as tk

window = tk.Tk()
window.geometry("1600x900")
window.configure(bg="light blue")

title = tk.Label(window, text = "Motor Breaker Sizing Calculator", font = ("Times New Roman",72), bg = "light blue", fg = "purple")
title.pack()

horse_power = tk.StringVar(window)
horse_power.set("1/2")


window.mainloop()