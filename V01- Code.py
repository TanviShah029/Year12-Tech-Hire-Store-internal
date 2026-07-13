# Tech Hire Store Program
# I made this program for my internal

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
import os

# Accessories for sale
# name, picture
ACCESSORIES=["Gaming Mouse","Keyboard","Headsets","Computer"]

# All colours hex code for every windows
L_BLUE = "#ADD8E6"
NVY_BLUE= "#056b7d"
WHT = "#FFFFFF"

# Make first window
win = Tk()
win.title("Byte & Bolt Tech Hire")
win.geometry("600x500")
win.configure(bg="#ADD8E6")

# Save function to save data
def save():
    messagebox.showinfo("File is saved.")

# Tool bar which is shown in every page
m_tool_bar = Frame(win, bg= NVY_BLUE)
m_tool_bar.pack(side="top", fill="x", ipady=3)


# logo
logo_image = Image.open("Images/logo.png")
logo_image = logo_image.resize((67, 67))
logo_photo = ImageTk.PhotoImage(logo_image)

logo_label = Label(
    m_tool_bar,
    image = logo_photo,
    bg = NVY_BLUE
)

logo_label.image = logo_photo
logo_label.place(relx = 0.97, rely = 0.5, anchor = "e")

# Main title for tech hire store  
m_tl = Label(m_tool_bar, text="Byte and Bolt Tech Hire", font=("Arial", 20, "bold"), bg=NVY_BLUE, fg=WHT)
m_tl.pack(side="top", padx=10, pady=4)

# Menu button showing all pages
main_btn_dsp = Menubutton(m_tool_bar, text="☰", font = ("Arial", 15), bg=L_BLUE)
main_btn_dsp.pack(side="left")
main_btn_dsp.place(relx= 0.05, rely= 0.15)

# Dropdown list for the user to pick from
drp_dwn_for_user = Menu(main_btn_dsp, tearoff=0)
main_btn_dsp["menu"] = drp_dwn_for_user  

drp_dwn_for_user.add_command(label="Hire", command=lambda: choice_set_for_menu("Hire"))
drp_dwn_for_user.add_command(label="Return", command=lambda: choice_set_for_menu("Return"))
drp_dwn_for_user.add_command(label="Quit", command=lambda: choice_set_for_menu("Quit"))

# Search button for user to search anything realted to program
# Choice function to show what user selected  
def choice_set_for_menu(value):
    print(f"Selected: {search}")

# Search function for user to use
def search():
    if not etry.winfo_viewable():
        etry.pack(side="left", padx=5)
        srch_btn_user.config(text="Go")
    else:
        print("Searching for user's entry:", etry.get())
   
etry = Entry(m_tool_bar)

srch_btn_user = Button(m_tool_bar, text="🔍", font = ("Arial", 13), bg= L_BLUE, command=search)
srch_btn_user.pack(side="left")
srch_btn_user.place(relx= 0.13, rely= 0.15)

# Date of hire field for user
frm_frame_hire = Frame(win, bg=L_BLUE)
frm_frame_hire.pack(side="top", pady=40)

hir_label = Label(frm_frame_hire, text="Date of Hire:", font=("Arial", 12, "bold"), bg=L_BLUE, fg=NVY_BLUE)
hir_label.pack(side="left", padx=3)

# Calendar picker for user to pick a hire date from
hir_cale_etry = DateEntry(
    frm_frame_hire,
    width=11,
    font=("Arial", 12),
    bg= NVY_BLUE,      
    fg= WHT,          
    headerbg= L_BLUE,
    noramlbg=WHT,    
    selectmode='day',
    year=2026, month=6, day=15
)
hir_cale_etry.pack(side="left", padx=5)

# First name for user to enter
first_name_label = Label(win, text= "First Name:", font=("Arial", 12, "bold"), bg=L_BLUE, fg=NVY_BLUE)
first_name_label.pack()

first_name_box= Entry(win)
first_name_box.pack(pady=5)

# Last name for user to enter
last_name_label = Label(win, text= "Last Name:", font=("Arial", 12, "bold"), bg=L_BLUE, fg=NVY_BLUE)
last_name_label.pack()

last_name_box= Entry(win)
last_name_box.pack(pady=5)

# Contact Details for user to enter
contact_details_label = Label(win, text= "Contact Details:", font=("Arial", 11, "bold"), bg=L_BLUE, fg=NVY_BLUE)
contact_details_label.pack()

contact_details_box= Entry(win)
contact_details_box.pack(pady=5)


win.mainloop()
