import tkinter as tk

# Data From Table 6 -- verified
RRRU6 = {
    "12": 11.58, "10": 15.69, "8": 28.18, "6": 37.94, "4": 52.42, "3": 61.93, "2": 73.9, "1": 99.05,
    "1/0": 118.24, "2/0": 141.87, "3/0": 170.64, "4/0": 206.37, "250": 251.65, "300": 292.55, "350": 331.03,
    "400": 372.91, "450": 412.23, "500": 450.51, "600": 561.58, "700": 640.18, "750": 679.33, "800": 718.69,
    "900": 796.73, "1000": 871.97, "1250": 1108, "1500": 1299.73, "1750": 1491.64, "2000": 1681.47 
}

RRRU10 = {
    "12": 16.62, "10": 21.48, "8": 28.18, "6": 46.69, "4": 62.63, "3": 72.99, "2": 85.93, "1": 122.52, 
    "1/0": 134.78, "2/0": 169.72, "3/0": 210.06, "4/0": 239.7, "250": 288.63, "300": 332, "350": 372.91, 
    "400": 417.28, "450": 458.82, "500": 499.16, "600": 582.78, "700": 622.8, "750": 702.62, "800": 742.64, 
    "900": 821.94, "1000": 898.33, "1250": 1153.3, "1500": 1348.74, "1750": 1544.12, "2000": 1737.16 
}

RRRRRRJ6 = {
    "12": 16.62, "10": 21.48, "8": 35.78, "6": 56.35, "4": 73.75, "3": 84.95, "2": 98.87, "1": 143.35, 
    "1/0": 166.27, "2/0": 194.09, "3/0": 227.51, "4/0": 268.51, "250": 353.32, "300": 401.15, "350": 446, 
    "400": 494.41, "450": 539.54, "500": 583.21, "600": 708.74, "700": 796.73, "750": 840.33, "800": 884.05, 
    "900": 970.38, "1000": 1053.24, "1250": 1410.63, "1500": 1625.97, "1750": 1839.84, "2000": 2050.04 
}

TTRU = {
    "12": 22.56, "10": 27.99, "8": 47.29, "6": 59.72, "4": 77.76, "3": 89.42, "2": 103.51, "1": 137.89, 
    "1/0": 160.16, "2/0": 187.48, "3/0": 220.62, "4/0": 262.45, "250": 320.47, "300": 364.4, "350": 408.64, 
    "400": 455.03, "450": 498.36, "500": 540.78, "600": 661.43, "700": 746.03, "750": 788.74, "800": 831.11, 
    "900": 914.88, "1000": 995.38, "1250": 1199.5, "1500": 1499.5, "1750": 1651.8, "2000": 1851.26 
}

RU1020 = {
    "12": 22.56, "10": 28.18, "8": 47.42, "6": 59.86, "4": 77.76, "3": 89.25, "2": 103.51, "1": 137.89, 
    "1/0": 159.93, "2/0": 187.23, "3/0": 220.62, "4/0": 261.01, "250": 319.84, "300": 365.76, "350": 411.15, 
    "400": 455.03, "450": 498.36, "500": 540.36, "600": 622.34, "700": 747.48, "750": 789.74, "800": 830.6, 
    "900": 915.95, "1000": 996.5, "1250": 1247.86, "1500": 1450.85, "1750": 1653.24, "2000": 1852.79
}

RJ1020 = {
    "12": 29.42, "10": 35.78, "8": 67.78, "6": 82.52, "4": 103.33, "3": 116.52, "2": 148.71, "1": 189.42, 
    "1/0": 215.12, "2/0": 246.61, "3/0": 284.72, "4/0": 364.06, "250": 433, "300": 486.17, "350": 538.36, 
    "400": 588.36, "450": 637.49, "500": 684.88, "600": 821.43, "700": 915.95, "750": 962.66, "800": 1007.72, 
    "900": 1101.52, "1000": 1189.69, "1250": 1567.89, "1500": 1794.51, "1750": 2018.86, "2000": 2238.77
}

RU20 = {
    "12": 22.56, "10": 28.18, "8": 41.51, "6": 53.2, "4": 70.14, "3": 81.07, "2": 94.69, "1": 132.94, 
    "1/0": 154.6, "2/0": 181.46, "3/0": 214.34, "4/0": 254.19, "250": 312.28, "300": 357.67, "350": 402.57, 
    "400": 446, "450": 488.91, "500": 530.52, "600": 650.54, "700": 734.93, "750": 776.84, "800": 817.37, 
    "900": 902.06, "1000": 982.01, "1250": 1247.86, "1500": 1450.85, "1750": 1653.24, "2000": 1852.79
}

RJ10 = {
    "12": 22.56, "10": 28.18, "8": 44.3, "6": 66.91, "4": 85.77, "3": 97.82, "2": 112.72, "1": 171.34, 
    "1/0": 195.82, "2/0": 225.91, "3/0": 262.45, "4/0": 306.35, "250": 396.2, "300": 447.13, "350": 497.18, 
    "400": 545.32, "450": 592.66, "500": 638.39, "600": 732.53, "700": 821.94, "750": 866.22, "800": 908.99, 
    "900": 998.18, "1000": 1082.2, "1250": 1461.67, "1500": 1680.74, "1750": 1898.08, "2000": 2111.48
}

RJ20 = {
    "12": 29.42, "10": 44.3, "8": 60.68, "6": 74.66, "4": 94.52, "3": 107.15, "2": 138.09, "1": 183.61, 
    "1/0": 208.93, "2/0": 239.98, "3/0": 277.59, "4/0": 355.99, "250": 424.19, "300": 476.84, "350": 528.48, 
    "400": 578.08, "450": 626.8, "500": 673.8, "600": 808.27, "700": 902.06, "750": 948.42, "800": 993.15, 
    "900": 1086.28, "1000": 1173.85, "1250": 1567.89, "1500": 1794.51, "1750": 2018.86, "2000": 2388.77
}

TT = {
    "12": 11.85, "10": 15.69, "8": 28.18, "6": 46.69, "4": 62.63, "3": 72.99, "2": 85.93, "1": 122.52, 
    "1/0": 143.78, "2/0": 169.72, "3/0": 201.06, "4/0": 239.7, "250": 296.51, "300": 340.45, "350": 381.86, 
    "400": 426.75, "450": 468.75, "500": 509.5, "600": 627.24, "700": 710.16, "750": 751.36, "800": 792.73, 
    "900": 874.59, "1000": 953.34, "1250": 1199.5, "1500": 1398.67, "1750": 1597.51, "2000": 1793.76
}

TTN = {
    "12": 8.45, "10": 13.66, "8": 23.67, "6": 32.67, "4": 53.2, "3": 62.77, "2": 74.82, "1": 100.82, 
    "1/0": 120.18, "2/0": 143.99, "3/0": 172.96, "4/0": 208.93, "250": 255.6, "300": 296.81, "350": 355.56, 
    "400": 377.72, "450": 417.28, "500": 455.79
}

# Data From Table 9 -- verified
RM = {
    "16": 80.93, "21": 141.6, "27": 229.02, "35": 393.91, "41": 534.56, "53": 879.48, "63": 1255.62, 
    "78": 1935.43, "91": 2583.29, "103": 3324.51, "129": 5215.77, "155": 7524.32
}

FM = {
    "12": 28.47, "16": 79.22, "21": 133.58, "27": 202.68, "35": 316.69, "41": 456.04, "53": 810.73,
    "63": 1266.77, "78": 1824.15, "91": 2482.87, "103": 3242.93
}

RP = {
    "16": 66.69, "21": 122.79, "27": 202.68, "35": 316.69, "41": 456.04, "53": 810.3, "63": 1180.51, 
    "78": 1824.15, "91": 2455.02, "103": 3147.88, "129": 4795.72, "155": 7045.04, "200": 12489.83
}

RR = {
    "53": 810.73, "78": 1824.15, "91": 2455.02, "103": 3147.88, "129": 5015.34, "155": 7045.04
}

MLF = {
    "12": 47.45, "16": 78.43, "21": 136.3, "27": 219.62, "35": 385.95, "41": 502.91, "53": 827.09,
    "63": 1246.5, "78": 1910.36, "91": 2482.87, "103": 3242.93
}

NMLF = {
    "12": 45.77, "16": 75.38, "21": 131.38, "27": 210.9, "35": 374.8, "41": 502.91, "53": 839.39
}

EM = {
    "16": 74.51, "21": 132.03, "27": 215.65, "35": 376.1, "41": 515.3, "53": 852.76, "63": 1513.1, 
    "78": 2280.49, "91": 2980.35, "103": 3801.33
}

ENM = {
    "16": 66.78, "21": 121.43, "27": 202.2, "35": 357.42, "41": 491.91, "53": 822.91
}

RRCMI = {
    "16": 93.7, "21": 160.6, "27": 270.44, "35": 456.04, "41": 613.5, "53": 994.37, "63": 1521.84,
    "78": 2261.26, "103": 3782, "129": 5822.66, "155": 8249.89
}

RRCMD = {
    "16": 44.79, "21": 105.09, "27": 190.74, "35": 301.71, "41": 438.02, "53": 794.54, "63": 1246.9,
    "78": 1799.81, "91": 2454.46, "103": 3210.45, "129": 5006.61
}

HDPE4 = {
    "16": 67.61, "21": 122.91, "27": 202.68, "35": 359.33, "41": 493.4, "53": 822.91, "63": 1173.97,
    "78": 1821.28, "103": 3157.95, "129": 4980.47, "155": 7210.66, "200": 12521.17
}

HDPE8 = {
    "16": 51.07, "21": 98.42, "27": 167.06, "35": 303.86, "41": 421.53, "53": 718.4, "63": 1019.63,
    "78": 1600.67, "103": 2809.08, "129": 4467.52, "155": 6411.67
}

HDPE9 = {
    "16": 75.18, "21": 121.3, "27": 194.16, "35": 311.92, "41": 409.42, "53": 641.56, "63": 937.59,
    "78": 1391.8, "103": 2289.07, "129": 3499.32, "155": 4958.34, "200": 8406.4, "275": 13053.55
}

HDPE11 = {
    "16": 83.47, "21": 135, "27": 215.82, "35": 348.58, "41": 460.12, "53": 721.11, "63": 1053.92,
    "78": 1565.88, "103": 2574.18, "129": 3935.89, "155": 5575.56, "200": 9455.81, "275": 14683.21
}

HDPE135 = {
    "16": 91.01, "21": 146.98, "27": 234.65, "35": 378.93, "41": 500.9, "53": 791.06, "63": 1156.75,
    "78": 1718.01, "103": 2825.15, "129": 4318.92, "155": 6119.75, "200": 10376.5, "275": 16115.65
}

HDPE155 = {
    "16": 95.44, "21": 153.99, "27": 245.77, "35": 396.81, "41": 524.24, "53": 830, "63": 1217,
    "78": 1807.43, "103": 2973.63, "129": 4545.79, "155": 6441.33, "200": 10918.96, "275": 16960.37
}

#Amp -- verified
amp = {
    "12": 30, "10": 60, "8": 100, "6": 200, "4": 300, "3": 400, "2": 500, "1": 600, "1/0": 800,
    "2/0": 1000, "3/0": 1200, "4/0": 1600, "250": 2000, "350": 2500, "400": 3000,
    "500": 4000, "700": 5000, "800": 6000 
}

#Size to Amp -- verified
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
    elif type == "R90XLPE, RW75XLPE, RW90XLPE UNJACKETED 1000V":
        return int(amt) * float(RRRU10[c_size]) + float(RRRU10[b_size])
    elif type == "R90XLPE, RW75XLPE, R90EP, RW75EP, RW90XLPE, RW90EP JACKETED 600V":
        return int(amt) * float(RRRRRRJ6[c_size]) + float(RRRRRRJ6[b_size])
    elif type == "TWU, TWU75, RWU90XLPE UNJACKETED":
        return int(amt) * float(TTRU[c_size]) + float(TTRU[b_size])
    elif type == "RPVU90 UNJACKETED 1000V AND 2000V":
        return int(amt) * float(RU1020[c_size]) + float(RU1020[b_size])
    elif type == "RPVU90 JACKETED 1000V AND 2000V":
        return int(amt) * float(RJ1020[c_size]) + float(RJ1020[b_size])
    elif type == "RPVU90 UNJACKETED 2000V":
        return int(amt) * float(RU20[c_size]) + float(RU20[b_size])
    elif type == "RPVU90 JACKETED 1000V":
        return int(amt) * float(RJ10[c_size]) + float(RJ10[b_size])
    elif type == "RPVU90 JACKETED 2000V":
        return int(amt) * float(RJ20[c_size]) + float(RJ20[b_size])
    elif type == "TW, TW75":
        return int(amt) * float(TT[c_size]) + float(TT[b_size])
    elif type == "TWN75, T90 NYLON(Max Size: 500)":
        return int(amt) * float(TTN[c_size]) + float(TTN[b_size])
    else:
        return None

#Switch area -- returns the conduit size
def get_diameter(type, area):
    if type == "Electrical Metallic Tubing":
        return find_largest_value_key(EM, area)
    elif type == "Rigid Metal Conduit":
        return find_largest_value_key(RM, area)
    elif type == "Flexible Metal Conduit":
        return find_largest_value_key(FM, area)
    elif type == "Rigid PVC Conduit":
        return find_largest_value_key(RP, area)
    elif type == "Rigid EB1 PVC and Rigid DB2/ES2 PVC Conduit":
        return find_largest_value_key(RR, area)
    elif type == "Metallic Liquid-tight Flexible Conduit":
        return find_largest_value_key(MLF, area)
    elif type == "Non-metallic Liquid-tight Flexible Conduit":
        return find_largest_value_key(NMLF, area)
    elif type == "Electrical Non-metallic Tubing":
        return find_largest_value_key(ENM, area)
    elif type == "Rigid RTRC Conduit Marked IPS":
        return find_largest_value_key(RRCMI, area)
    elif type == "Rigid RTRC Conduit Marked ID":
        return find_largest_value_key(RRCMD, area)
    elif type == "HDPE Conduit Schedule 40":
        return find_largest_value_key(HDPE4, area)
    elif type == "HDPE Conduit Schedule 80":
        return find_largest_value_key(HDPE8, area)
    elif type == "HDPE DR9 Conduit":
        return find_largest_value_key(HDPE9, area)
    elif type == "HDPE DR11 Conduit":
        return find_largest_value_key(HDPE11, area)
    elif type == "HDPE DR13.5 Conduit":
        return find_largest_value_key(HDPE135, area)
    elif type == "HDPE DR15.5 Conduit":
        return find_largest_value_key(HDPE155, area)
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

    if conductor_type == '':
        message_var.set("Please Select a Conductor Type")
    elif conduit_type == '':
        message_var.set("Please Select a Conduit Type")
    elif amount == '': 
        message_var.set("Please enter the amount of conduits.")
    elif conductor_size == '':
        message_var.set("Please Select a Conductor Size")
        
    if checkbox_value2.get():
        bond_size = manual
    elif checkbox_value1.get():
        bond_size = find_largest_value_key(amp, float(amperage))
    else: 
        bond_size = find_largest_value_key(amp, float(sizeToAmp[conductor_size]))

    area = get_area(conductor_type, amount, conductor_size, bond_size)
    diameter = get_diameter(conduit_type, float(area))
    
    if diameter == None:
        message_var.set("Cannot find a suitable conduit")
    else:
        message_var.set(f"Your Conduit Size is {diameter}mm \n Conductor: {conductor_size}AWG \n Bonding Conductor: {bond_size}AWG \n 40% Area: {round(area,2)}")

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
                                                                        "TWN75, T90 NYLON(Max Size: 500)")
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
