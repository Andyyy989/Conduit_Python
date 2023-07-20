import tkinter as tk

def print_text():
    input_text = text_entry.get()
    amp1_text = amp_entry1.get() if checkbox_value1.get() else 'N/A'
    bonding_size_text = bonding_size_var.get() if checkbox_value2.get() else 'N/A'
    conductor_option_value = conductor_option_var.get()
    type_option_value = type_option_var.get()
    message_var.set(f"Text: {input_text}, Amps 1: {amp1_text}, Bonding Size: {bonding_size_text}, Checkbox 1: {'Checked' if checkbox_value1.get() else 'Not checked'}, Checkbox 2: {'Checked' if checkbox_value2.get() else 'Not checked'}, Conductor Size: {conductor_option_value}, Type: {type_option_value}")

def checkbox_changed():
    button_frame.pack_forget()
    amp_frame1.pack_forget()
    bonding_size_frame.pack_forget()
    message_label.pack_forget()
    if checkbox_value1.get():
        amp_frame1.pack()
    if checkbox_value2.get():
        bonding_size_frame.pack()
    button_frame.pack()
    message_label.pack()

root = tk.Tk()
root.geometry("800x600")
root.configure(bg="light blue")

title = tk.Label(root, text="Conduit Sizing Calculator", font=("Times New Roman", 40), bg="light blue", fg="blue")
title.pack()

type_option_frame = tk.Frame(root, bg="light blue")
type_option_frame.pack()

type_option_label = tk.Label(type_option_frame, text="Select the type of conductors:", font=("Times New Roman", 20), bg="light blue")
type_option_label.grid(row=0, column=0)

type_option_var = tk.StringVar()
type_option_menu = tk.OptionMenu(type_option_frame, type_option_var, "R90XLPE")
type_option_menu.config(font=("Times New Roman", 20), bg="light blue")
type_option_menu.grid(row=0, column=1)

input_frame = tk.Frame(root, bg="light blue")
input_frame.pack()

input_label = tk.Label(input_frame, text="Enter the amount of conductors:", font=("Times New Roman", 20), bg="light blue")
input_label.grid(row=0, column=0)

text_entry = tk.Entry(input_frame, font=("Times New Roman", 20), width=10)
text_entry.grid(row=0, column=1)

conductor_option_frame = tk.Frame(root, bg="light blue")
conductor_option_frame.pack()

conductor_option_label = tk.Label(conductor_option_frame, text="Enter conductor size:", font=("Times New Roman", 20), bg="light blue")
conductor_option_label.grid(row=0, column=0)

conductor_option_var = tk.StringVar()
conductor_option_menu = tk.OptionMenu(conductor_option_frame, conductor_option_var, 12, 10, 8, 6)
conductor_option_menu.config(font=("Times New Roman", 20), bg="light blue")
conductor_option_menu.grid(row=0, column=1)

checkbox_value1 = tk.IntVar()
checkbox1 = tk.Checkbutton(root, text="Size bonding conductor based on breaker size", font=("Times New Roman", 20), bg="light blue", variable=checkbox_value1, command=checkbox_changed)
checkbox1.pack()

amp_frame1 = tk.Frame(root, bg="light blue")

amp_label1 = tk.Label(amp_frame1, text="Enter the amperage of the breaker:", font=("Times New Roman", 20), bg="light blue", fg="blue")
amp_label1.grid(row=0, column=0)

amp_entry1 = tk.Entry(amp_frame1, font=("Times New Roman", 20), width=10)
amp_entry1.grid(row=0, column=1)

checkbox_value2 = tk.IntVar()
checkbox2 = tk.Checkbutton(root, text="Manual input of bonding conductor", font=("Times New Roman", 20), bg="light blue", variable=checkbox_value2, command=checkbox_changed)
checkbox2.pack()

bonding_size_frame = tk.Frame(root, bg="light blue")

bonding_size_label = tk.Label(bonding_size_frame, text="Select bonding conductor size:", font=("Times New Roman", 20), bg="light blue", fg="blue")
bonding_size_label.grid(row=0, column=0)

bonding_size_var = tk.StringVar()
bonding_size_menu = tk.OptionMenu(bonding_size_frame, bonding_size_var, 12, 10, 8, 6)
bonding_size_menu.config(font=("Times New Roman", 20), bg="light blue")
bonding_size_menu.grid(row=0, column=1)

button_frame = tk.Frame(root, bg="light blue")
button = tk.Button(button_frame, text="Calculate", command=print_text, font=("Times New Roman", 20), bg="blue", fg="white")
button.pack()

message_var = tk.StringVar()
message_label = tk.Label(root, textvariable=message_var, font=("Times New Roman", 20), bg="light blue")

button_frame.pack()
message_label.pack()

root.mainloop()
