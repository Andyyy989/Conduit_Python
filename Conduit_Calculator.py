import tkinter as tk

def print_text():
    # Get the current value of the entry field
    input_text = text_entry.get()

    # Get the current value of the checkbox
    checkbox_value = checkbox_var.get()

    # Get the current value of the option menu
    option_value = option_var.get()

    # Set the message label text
    message_var.set(f"Text: {input_text}, Checkbox: {'Checked' if checkbox_value else 'Not checked'}, Option: {option_value}")

# Create the main window
root = tk.Tk()
root.geometry("800x600")
root.configure(bg="light blue")

# Add a big centered title with even larger font
title = tk.Label(root, text="Conduit Sizing Calculator", font=("Times New Roman", 40), bg="light blue")
title.pack()

# Create a frame to hold the text entry field and its label
input_frame = tk.Frame(root, bg="light blue")
input_frame.pack()

# Add a label for the text entry field
input_label = tk.Label(input_frame, text="Enter the amount of conductors:", font=("Times New Roman", 20), bg="light blue")
input_label.grid(row=0, column=0)

# Create a text entry field with a smaller width
text_entry = tk.Entry(input_frame, font=("Times New Roman", 20), width=10)
text_entry.grid(row=0, column=1)

# Create a checkbox
checkbox_var = tk.IntVar()
checkbox = tk.Checkbutton(root, text="Check me", font=("Times New Roman", 20), bg="light blue", variable=checkbox_var)
checkbox.pack()

# Create a frame to hold the option label and option menu
option_frame = tk.Frame(root, bg="light blue")
option_frame.pack()

# Add a label for the option menu
option_label = tk.Label(option_frame, text="Select the type of conductors:", font=("Times New Roman", 20), bg="light blue")
option_label.grid(row=0, column=0)

# Create an option menu
option_var = tk.StringVar()
option_menu = tk.OptionMenu(option_frame, option_var, "Option 1", "Option 2", "Option 3")
option_menu.config(font=("Times New Roman", 20), bg="light blue")
option_menu.grid(row=0, column=1)

# Create a button with the text "Calculate" and pack it so it appears above the message label
button = tk.Button(root, text="Calculate", command=print_text, font=("Times New Roman", 20), bg="light blue")
button.pack()

# Create a label to display the message with larger font and pack it last so it appears at the bottom
message_var = tk.StringVar()
message_label = tk.Label(root, textvariable=message_var, font=("Times New Roman", 20), bg="light blue")
message_label.pack()

# Start the main loop
root.mainloop()
