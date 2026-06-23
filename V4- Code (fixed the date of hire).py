# Tech Hire Store Program.
# I made this program for my internal.

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import json
import random
import os
from tkcalendar import Calendar, DateEntry
from datetime import date, datetime

customer_info = {}
hired_details = {}

# Accessories for sale.
# Name and picture. 

ACCESSORIES = {
    "Gaming Mouse": ["Images/Gaming Mouse.png", 55],
    "Keyboard": ["Images/Keyboard.png", 150],
    "Headsets": ["Images/Headsets.png", 250],
    "Computer": ["Images/Computer.png", 1078]
}

cart = []
selected_computer_accessories = None

# All colours hex code for every window.
L_BLUE = "#ADD8E6"
NVY_BLUE= "#056b7d"
WHT = "#FFFFFF"

# Windows page.
current_page= [None]
current_win= [None]

# My first window for the store.
win = Tk()
win.title("Byte & Bolt Tech Hire")
win.geometry("600x500")
win.configure(bg="#ADD8E6")

# Save function to save customer details. 
def load_data():
    if os.path.exists("customer_details.json"):
        with open("customer_details.json","r") as file:
            content=file.read()
            if content.strip() =="":
                return[]
            return json.loads(content)
    return[]

# Tool bar which is shown in every page.
m_tool_bar = Frame(win, bg= NVY_BLUE)
m_tool_bar.pack(side="top", fill="x", ipady=3)

# Main title for tech hire store.  
m_tl = Label(m_tool_bar, text="Byte and Bolt Tech Hire", font=("Arial", 20, "bold"), bg=NVY_BLUE, fg=WHT)
m_tl.pack(side="top", padx=10, pady=4)

# Menu button for every page.
main_btn_dsp = Menubutton(m_tool_bar, text="☰", font = ("Arial", 15), bg=L_BLUE)
main_btn_dsp.pack(side="left")
main_btn_dsp.place(relx= 0.05, rely= 0.15)

# Dropdown list for the user to select from. 
drp_dwn_for_user = Menu(main_btn_dsp, tearoff=0)
main_btn_dsp["menu"] = drp_dwn_for_user  

drp_dwn_for_user.add_command(label="Hire", command=lambda: choice_set_for_menu("Hire"))
drp_dwn_for_user.add_command(label="Return", command=lambda: choice_set_for_menu("Return"))
drp_dwn_for_user.add_command(label="Quit", command=lambda: choice_set_for_menu("Quit"))

# Search button for user to search any pages. 
# Choice function to show what user selected.   
def choice_set_for_menu(value):
    print(f"Selected: {search}")

# Search function for user to use. 
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

# Date of hire field for user. 
frm_frame_hire = Frame(win, bg=L_BLUE)
frm_frame_hire.pack(side="top", pady=40)

hir_label = Label(frm_frame_hire, text="Date of Hire:", font=("Arial", 12, "bold"), bg=L_BLUE, fg=NVY_BLUE)
hir_label.pack(side="left", padx=3)

# Calendar picker for user to pick a date from.
hir_cale_etry = DateEntry(
    frm_frame_hire,
    width=11,
    font=("Arial", 12),
    bg= NVY_BLUE,      
    fg= WHT,          
    headerbg= L_BLUE,
    noramlbg=WHT,    
    selectmode='day',
)

hir_cale_etry.pack(side="left", padx=5)

# Deleting the default date. 
hir_cale_etry.delete(0, END)

# First name for user to enter.
first_name_label = Label(win, text= "First Name:", font=("Arial", 12, "bold"), bg=L_BLUE, fg=NVY_BLUE)
first_name_label.pack()

first_name_box= Entry(win)
first_name_box.pack(pady=5)

# Last name for user to enter.
last_name_label = Label(win, text= "Last Name:", font=("Arial", 12, "bold"), bg=L_BLUE, fg=NVY_BLUE)
last_name_label.pack()

last_name_box= Entry(win)
last_name_box.pack(pady=5)

# Contact Details for user to enter.
contact_details_label = Label(win, text= "Contact Details:", font=("Arial", 11, "bold"), bg=L_BLUE, fg=NVY_BLUE)
contact_details_label.pack()

contact_details_box= Entry(win)
contact_details_box.pack(pady=5)

# I made save records for all the data of customer details to save.
# I made the validations for all fields in hire page.
def load_data():
    if os.path.exists("customer_details.json"):
        with open("customer_details.json","r") as file:
            content=file.read()
            if content.strip() =="":
                return[]
            return json.loads(content)
    return[]

def save_records():
    errors=[]

    if not first_name_box.get() or not first_name_box.get().replace(" ","").isalpha():
        errors.append("First name cannot be empty, contain integers, or contain symbols.")

    if not last_name_box.get() or not last_name_box.get().replace(" ","").isalpha():
        errors.append("Last name cannot be empty or contain integers.")

    if not contact_details_box.get() or not contact_details_box.get().replace(" ","").isdigit():
        errors.append("Contact Details cannot be empty or contain letters.")

    if len(contact_details_box.get()) > 10:
        errors.append("Contact details must be less than 10 numbers")

    if hir_cale_etry.get() =="":
        errors.append("Please select a date.")
    else:
        try:
            DateEntry_val=datetime.strptime(hir_cale_etry.get(),"%m/%d/%y").date()
            if DateEntry_val < date.today():
                errors.append("Date cannot be in the past")
        except ValueError:
            errors.append("Invalid date format.")

    if errors:
        messagebox.showerror("Error","\n".join(errors))
        return

    current_entries = load_data()
   
    new_record = {
        "first_name": first_name_box.get().strip(),
        "last_name": last_name_box.get().strip(),
        "contact_details": contact_details_box.get().strip(),
        "hire_date": hir_cale_etry.get()
    }

    customer_info["first_name"]=first_name_box.get().strip()
    customer_info["last_name"] = last_name_box.get().strip()
    customer_info["contact_details"] =  contact_details_box.get().strip()
    customer_info["hire_date"] = hir_cale_etry.get()
   
    current_entries.append(new_record)

    with open("customer_details.json", "w") as file:
        json.dump(current_entries, file, indent=4)
       
    messagebox.showinfo("Success", "Record saved successfully!")

# I created a deleting record function. 
def delete_records():
    file = open("customer_details.json", "w")
    file.close()

    messagebox.showinfo("Success", "All records are deleted")

# I created a function to exit the program. 
def exit_program():
    win.destroy()

# I made a new window for computer accessories. 
def computer_accessories():
    if current_page[0]=="computer_accessories":
        return
    if current_win[0] is not None:
        current_win[0].destroy()
    win.withdraw()
   
    cmpacc_win = Toplevel()
    cmpacc_win.title("Computer Accesories")
    cmpacc_win.geometry("400x600")
    cmpacc_win.configure(bg="#ADD8E6")

    current_win[0]= cmpacc_win
    current_page[0]="computer_accessories"

    def close():
        current_page[0]= None
        current_win[0]= None 
        win.deiconify()
        cmpacc_win.destroy()

    cmpacc_win.protocol("WM_DELETE_WINDOW", close)

    # Tool bar which is shown in every page.
    acc_frame= Frame(cmpacc_win, bg= NVY_BLUE)
    acc_frame.pack(side="top", fill="x", ipady=3)

    # Main title for tech hire store.
    acc_title = Label(acc_frame, text="Computer Accessories", font=("Arial", 17, "bold"), bg=NVY_BLUE, fg=WHT)
    acc_title.pack(side="top", padx=10, pady=4)

    # I made a dropdown to show all computer accessories list.  
    def show_computer_accessories(event=None):
        choice= selected_computer_accessories.get()
        if choice in ACCESSORIES:
            try:
                pic = Image.open( ACCESSORIES[choice][0])
                pic = pic.resize((170, 170))
                photo = ImageTk.PhotoImage(pic)
                image_box.config(image=photo, text="", bg=L_BLUE)
                image_box.image = photo
            except:
                image_box.config(text="no pic", image='', bg=L_BLUE)

            price_box.config(text="$" + str(ACCESSORIES[choice] [1]))

    def add():
        Accessories = selected_computer_accessories.get()
        if Accessories in ACCESSORIES:
            cart.append(Accessories)
            status_box.config(text= Accessories + " added")
           
    # Dropdown list.
    selected_computer_accessories = StringVar()
    dropdown = ttk.Combobox(cmpacc_win, textvariable=selected_computer_accessories, values=list(ACCESSORIES.keys()))
    values=list(ACCESSORIES.keys())
    dropdown.pack(pady=30)
    dropdown.bind("<<ComboboxSelected>>", show_computer_accessories)

    # Images show up here.
    image_box = Label(cmpacc_win, font=("Arial", 12), bg=L_BLUE)
    image_box.pack(pady=10)

    # Price Label goes here.
    price_box = Label(cmpacc_win, font=("Arial", 14, "bold"), bg=L_BLUE)
    price_box.pack()

    # Buttons for this page.
    add_button = Button(cmpacc_win, text="Add to Cart", bg= NVY_BLUE, fg=WHT, font=("Arial", 10, "bold"), width = 15, height =2, command=add)
    add_button.pack()
    add_button.place(relx= 0.15, rely=0.70)

    add_view_receipt_button= Button(cmpacc_win, text="View Receipt", bg= NVY_BLUE, fg=WHT, font=("Arial", 10, "bold"), width = 15, height =2, command=view_receipt_page)
    add_view_receipt_button.pack()
    add_view_receipt_button.place(relx= 0.50, rely=0.70)

    # Status message. 
    status_box = Label(cmpacc_win, font=("Arial", 10, "bold"), bg=L_BLUE, fg=NVY_BLUE, width = 25, height =2)
    status_box.place(relx=0.25, rely =0.78)

    dropdown.current(0)
    show_computer_accessories()

    def exit_page():
        if current_win[0] is not None:
            try:
                current_win[0].destroy()
            except:
                pass
        win.destroy()

    bar_btn_exit_page= Button(cmpacc_win, text="Exit", bg= NVY_BLUE, fg=WHT, font=("Arial", 10, "bold"), width = 15, height =2, command= exit_page)
    bar_btn_exit_page.pack()
    bar_btn_exit_page.place(relx= 0.32, rely=0.86)

# I made a new window for viewing receipt.
def view_receipt_page():
    if current_page[0]=="view_receipt_win":
        return
    if current_win[0] is not None:
         current_win[0].destroy()
    win.withdraw()
   
    view_receipt_win = Toplevel()
    view_receipt_win.title("BYTE & BOLT RECEIPT")
    view_receipt_win.geometry("400x600")
    view_receipt_win.configure(bg="#ADD8E6")

    current_win[0]= view_receipt_win
    current_page[0]="view_receipt_win"

    def close():
        current_page[0]= None
        current_win[0]= None
        win.deiconify()
        view_receipt_win.destroy()

    view_receipt_win.protocol("WM_DELETE_WINDOW", close)

    # Tool bar which is shown in every page.
    rece_frame= Frame(view_receipt_win, bg= NVY_BLUE)
    rece_frame.pack(side="top", fill="x", ipady=4)

    # Main title for tech hire store.
    rece_title = Label( rece_frame, text="BYTE & BOLT RECEIPT", font=("Arial", 16, "bold"), bg=NVY_BLUE, fg=WHT)
    rece_title.pack(side="top", padx=10, pady=4)

    def exit_page():
        if current_win[0] is not None:
            try:
                current_win[0].destroy()
            except:
                pass
        win.destroy()      

    def gene_receipt_no():
        text = ""
        random_number = random.randint(10000, 99999)
        receipt = text + str(random_number)
        return receipt

    # Receipt created with customer details.
    def view_receipt():
        receipt_no=gene_receipt_no()
        receipt_variable = StringVar(value=str(receipt_no))

        receipt_label= Label(view_receipt_win,text="Receipt Number:",bg=L_BLUE,fg=NVY_BLUE, font=("Arial",13, "bold"),width=15)
        receipt_label.pack()
        receipt_label.place(relx=0.10, rely=0.25)

        receipt_entry=Entry(view_receipt_win, textvariable=receipt_variable, state="readonly",bg=L_BLUE,width=20)
        receipt_entry.pack()
        receipt_entry.place(relx=0.55, rely=0.25)

        recei_name_lbl= Label(view_receipt_win,text="Customer name: "+customer_info.get("first_name","")+" "+customer_info.get("last_name",""),bg=L_BLUE, fg=NVY_BLUE, font=("Arial",13, "bold"),width=30)
        recei_name_lbl.pack()
      
        label = Label(view_receipt_win, text="", bg=L_BLUE)
        label.pack()

    view_receipt()  

# I made the buttons for hire page.
bar_btn_computer_accessories= Button(text="Computer Accessories", bg= NVY_BLUE, fg=WHT, font=("Arial", 10, "bold"), width = 17, height =2, command=computer_accessories)
bar_btn_computer_accessories.pack(padx=1, pady=1)
bar_btn_computer_accessories.place(relx= 0.25, rely=0.70)

bar_btn_save= Button(text="Save", bg= NVY_BLUE, fg=WHT, font=("Arial", 10, "bold"), width = 17, height =2, command=save_records)
bar_btn_save.pack(padx=1, pady=1)
bar_btn_save.place(relx= 0.55, rely=0.70)

bar_btn_delete= Button(text="Delete", bg= NVY_BLUE, fg=WHT, font=("Arial", 10, "bold"), width = 17, height =2, command =delete_records)
bar_btn_delete.pack(padx=1, pady=1)
bar_btn_delete.place(relx= 0.25, rely=0.84)

bar_btn_exit= Button(text="Exit", bg= NVY_BLUE, fg=WHT, font=("Arial", 10, "bold"), width = 17, height =2, command=exit_program)
bar_btn_exit.pack(padx=1, pady=1)
bar_btn_exit.place(relx= 0.55, rely=0.84)

win.mainloop()
