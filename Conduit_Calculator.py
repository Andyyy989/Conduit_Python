import tkinter as tk

# Data From Table 6
RRRU6 = {
    "12": 11.58, "10": 15.69, "8": 28.18, "6": 37.94, "4": 52.42, "3": 61.93, "2": 73.9, "1": 99.05,
    "1/0": 118.24, "2/0": 141.87, "3/0": 170.64, "4/0": 206.37, "250": 251.65, "300": 292.55, "350": 331.03,
    "400": 372.91, "450": 412.23, "500": 450.51, "600": 561.58, "700": 640.18, "750": 679.33, "800": 718.69,
    "900": 796.73, "1000": 871.97, "1250": 1108, "1500": 1299.73, "1750": 1491.64, "2000": 1681.47 
}

# Data From Table 9
RM = {
    "16": 80.93, "21": 141.6, "27": 229.02, "35": 393.91, "41": 534.56, "53": 879.48, "63": 1255.62, 
    "78": 1935.43, "91": 2583.29, "103": 3324.51, "129": 5215.77, "155": 7524.32
}

#Amp
amp = {
    "12": 30, "10": 60, "8": 100, "6": 200, "4": 300, "3": 400, "2": 500, "1": 600, "1/0": 800,
    "2/0": 1000, "3/0": 1200, "4/0": 1600, "250": 2000, "350": 2500, "400": 3000,
    "500": 4000, "700": 5000, "800": 6000 
}

#Size to Amp
sizeToAmp = {
    "12": 25, "10": 35, "8": 50, "6": 65, "4": 85, "3": 100, "2": 115, "1": 130, 
    "1/0": 150, "2/0": 175, "3/0": 200, "4/0": 230, "250": 255, "300": 285, "350": 310, 
    "500": 380, "750": 475, "1000": 545, "1250": 590, "1500": 625, "1750": 650, "2000": 665
}

#Find largest value-key
def find_largest_value_key(obj, target):
    closest_value = float('inf')  # Initialize closest_value with positive infinity
    closest_value_key = None  # Initialize closest_value_key as None
    
    for key, value in obj.items():  # Iterate through key-value pairs in the obj dictionary
        if value >= target and value < closest_value:  # Check if the value is greater than or equal to the target and less than the current closest_value
            closest_value = value  # Update closest_value with the new closest value found
            closest_value_key = key  # Update closest_value_key with the corresponding key
        
    if closest_value_key is not None:  # If a closest value key was found
        return closest_value_key  # Return the key with the largest value that meets the condition
    else:
        return None  # If no key satisfies the condition, return None

#Switch Wire Types -- returns the total area
def get_area(type, amt, c_size, b_size):
    if type == "R90XLPE, RW75XLPE, RW90XLPE UNJACKETED 600V":
        return int(amt) * float(RRRU6[c_size]) + float(RRRU6[b_size])
    else:
        return None

def get_diameter(type, area):
    if type == "Electrical Metallic Tubing":
        return find_largest_value_key(RM, area)
    else:
        return None

# Function to update the text of the message label when the "Calculate" button is clicked
def print_text():
    # Fetch data from user inputs and prepare message
    conductor_type = type_option_var.get()
    conduit_type = type_option_var2.get()
    amount = text_entry.get()
    conductor_size = conductor_option_var.get()
    amperage = amp_entry1.get() if checkbox_value1.get() else 'N/A'
    manual = bonding_size_var.get() if checkbox_value2.get() else 'N/A'

    if checkbox_value1.get():
        bond_size = find_largest_value_key(amp, float(amperage))
    elif checkbox_value2.get():
        bond_size = float(manual)
    else: 
        bond_size = find_largest_value_key(amp, float(sizeToAmp[conductor_size]))

    area = get_area(conductor_type, amount, conductor_size, bond_size)
    diameter = get_diameter(conduit_type, float(area))
    
    message_var.set(f"{conduit_type} Amt: {amount}, Conductor Size: {conductor_size}, Amps: {amperage}, Bonding Size: {manual}, \n Bond size: {bond_size}, A: {area} D: {diameter}")

# Function to update the GUI when checkboxes are clicked
def checkbox_changed():
    # Hide these widgets
    button_frame.pack_forget()
    amp_frame1.pack_forget()
    bonding_size_frame.pack_forget()
    message_label.pack_forget()

    # Show widgets based on checkbox conditions
    if checkbox_value1.get():
        amp_frame1.pack()
    if checkbox_value2.get():
        bonding_size_frame.pack()

    # Always show button_frame and message_label
    button_frame.pack()
    message_label.pack()

# Create the main window
root = tk.Tk()
root.geometry("1600x900")
root.configure(bg="light blue")

# Main title label
title = tk.Label(root, text="Conduit Size Calculator", font=("Times New Roman", 72), bg="light blue", fg="blue")
title.pack()

# Frame and widgets for selecting type of conductors
type_option_frame = tk.Frame(root, bg="light blue")
type_option_frame.pack()

type_option_label = tk.Label(type_option_frame, text="Select Conductor Type", font=("Times New Roman", 30), bg="light blue")
type_option_label.grid(row=0, column=0)

type_option_var = tk.StringVar()
type_option_menu = tk.OptionMenu(type_option_frame, type_option_var,    "R90XLPE, RW75XLPE, RW90XLPE UNJACKETED 600V", \
                                                                        "R90XLPE, RW75XLPE, RW90XLPE UNJACKETED 1000V", \
                                                                        "R90XLPE, RW75XLPE, R90EP, RW75EP, RW90XLPE, RW90EP JACKETED 600V", \
                                                                        "TWU, TWU75, RWU90XLPE UNJACKETED", \
                                                                        "RPVU90 UNJACKETED 1000V AND 2000V", \
                                                                        "RPVU90 JACKETED 1000V AND 2000V", \
                                                                        "RPVU90 UNJACKETED 2000V", \
                                                                        "RPVU90 JACKETED 1000V", \
                                                                        "RPVU90 JACKETED 2000V", \
                                                                        "TW, TW75", \
                                                                        "TWN75, T90 NYLON")
type_option_menu.config(font=("Times New Roman", 20), bg="light blue")
type_option_menu.grid(row=0, column=1)

# Frame and widgets for selecting type of conductors
type_option_frame2 = tk.Frame(root, bg="light blue")
type_option_frame2.pack()

type_option_label2 = tk.Label(type_option_frame2, text="Select Conduit Type", font=("Times New Roman", 30), bg="light blue")
type_option_label2.grid(row=0, column=0)

type_option_var2 = tk.StringVar()
type_option_menu2 = tk.OptionMenu(type_option_frame2, type_option_var2, "Electrical Metallic Tubing", \
                                                                        "Rigid Metal Conduit", \
                                                                        "Flexible Metal Conduit", \
                                                                        "Rigid PVC Conduit", \
                                                                        "Rigid EB1 PVC and Rigid DB2/ES2 PVC Conduit", \
                                                                        "Metallic Liquid-tight Flexible Conduit", \
                                                                        "Non-metallic Liquid-tight Flexible Conduit", \
                                                                        "Electrical Non-metallic Tubing", \
                                                                        "Rigid RTRC Conduit Marked IPS", \
                                                                        "Rigid RTRC Conduit Marked ID", \
                                                                        "HDPE Conduit Schedule 40", \
                                                                        "HDPE Conduit Schedule 80", \
                                                                        "HDPE DR9 Conduit", \
                                                                        "HDPE DR11 Conduit", \
                                                                        "HDPE DR13.5 Conduit", \
                                                                        "HDPE DR15.5 Conduit")
type_option_menu2.config(font=("Times New Roman", 20), bg="light blue")
type_option_menu2.grid(row=0, column=1)

# Frame and widgets for entering the amount of conductors
input_frame = tk.Frame(root, bg="light blue")       
input_frame.pack()

input_label = tk.Label(input_frame, text="Enter the amount of conductors:", font=("Times New Roman", 30), bg="light blue")
input_label.grid(row=0, column=0)

text_entry = tk.Entry(input_frame, font=("Times New Roman", 20), width=10)
text_entry.grid(row=0, column=1)

# Frame and widgets for entering conductor size
conductor_option_frame = tk.Frame(root, bg="light blue")
conductor_option_frame.pack()

conductor_option_label = tk.Label(conductor_option_frame, text="Select Conductor Size:", font=("Times New Roman", 30), bg="light blue")
conductor_option_label.grid(row=0, column=0)

conductor_option_var = tk.StringVar()
conductor_option_menu = tk.OptionMenu(conductor_option_frame, conductor_option_var, "12", "10", "8", "6", "4", "3", "2", "1", "1/0", "2/0", "3/0", "4/0", "250", "300", "350", "500", \
                                                                                    "750", "1000", "1250", "1500", "1750", "2000")
conductor_option_menu.config(font=("Times New Roman", 20), bg="light blue")
conductor_option_menu.grid(row=0, column=1)

# Checkbutton and corresponding frame for sizing bonding conductor based on breaker size
checkbox_value1 = tk.IntVar()
checkbox1 = tk.Checkbutton(root, text="Size bonding conductor based on breaker size", font=("Times New Roman", 30), bg="light blue", variable=checkbox_value1, command=checkbox_changed)
checkbox1.pack()

amp_frame1 = tk.Frame(root, bg="light blue")

amp_label1 = tk.Label(amp_frame1, text="Enter the amperage of the breaker:", font=("Times New Roman", 30), bg="light blue", fg="blue")
amp_label1.grid(row=0, column=0)

amp_entry1 = tk.Entry(amp_frame1, font=("Times New Roman", 20), width=10)
amp_entry1.grid(row=0, column=1)

# Checkbutton and corresponding frame for manual input of bonding conductor
checkbox_value2 = tk.IntVar()
checkbox2 = tk.Checkbutton(root, text="Manual input of bonding conductor", font=("Times New Roman", 30), bg="light blue", variable=checkbox_value2, command=checkbox_changed)
checkbox2.pack()

bonding_size_frame = tk.Frame(root, bg="light blue")

bonding_size_label = tk.Label(bonding_size_frame, text="Select bonding conductor size:", font=("Times New Roman", 30), bg="light blue", fg="blue")
bonding_size_label.grid(row=0, column=0)

bonding_size_var = tk.StringVar()
bonding_size_menu = tk.OptionMenu(bonding_size_frame, bonding_size_var, "12", "10", "8", "6", "4", "3", "2", "1", "1/0", "2/0", "3/0", "4/0", "250", "300", "350", "500", \
                                                                                    "750", "1000", "1250", "1500", "1750", "2000")
bonding_size_menu.config(font=("Times New Roman", 20), bg="light blue")
bonding_size_menu.grid(row=0, column=1)

# Calculate button
button_frame = tk.Frame(root, bg="light blue")
button = tk.Button(button_frame, text="Calculate", command=print_text, font=("Times New Roman", 40), bg="blue", fg="white")
button.pack()

# Label to display the message
message_var = tk.StringVar()
message_label = tk.Label(root, textvariable=message_var, font=("Times New Roman", 30), bg="light blue")

button_frame.pack()
message_label.pack()

# Start the main loop
root.mainloop()
