# Tech Hire Store Program.
# I made this program for my internal.
# Tanvi Shah
# 1/07/2026

# Importing everything for the program. 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import json
import random
import os
from tkcalendar import Calendar, DateEntry
from datetime import date, datetime
from barcode import Code128
from barcode.writer import ImageWriter 

# Customer information and hired details. 
customer_info = {}
hired_details = {}

# Return Page window. 
return_page_win = None

# Accessories for sale.
# Name, picture and price are all shown. 

ACCESSORIES = {
    "Gaming Mouse": ["Images/Gaming Mouse.png", 55],
    "Keyboard": ["Images/Keyboard.png", 150],
    "Headsets": ["Images/Headsets.png", 250],
    "Computer": ["Images/Computer.png", 1078],
    "USB Hub": ["Images/USB Hub.png", 50],
    "Webcams": ["Images/Webcams.png", 100],
    "Monitor Stand": ["Images/Monitor Stand.png", 45]
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

# Home window which is shown in the menu.
def home_win_for_usr():
    global current_page, current_win, return_page_win

    if current_win[0] is not None and current_win[0].winfo_exists():
        current_win[0].destroy()

    current_page[0] = None
    current_win[0] = None
    return_page_win = None
    win.deiconify()

# Added a function which shows inspirational quotes for the user.
quot_inspirational_for_usr = [
    "You don't have to see the whole staircase, just take the first step. — Martin Luther King Jr.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.— Winston Churchill.",
    "Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time. — Thomas A. Edison."
    "The secret of getting ahead is getting started. — Mark Twain.",
    "The mind is everything. What you think you become. — Buddha.",
    "Change your thoughts and you change your world. — Norman Vincent Peale",
    "Every day is a fresh start. Make the most of it!",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    ]

# Function for confirmation of exiting the program. 
def cnfrm_exit_program():
    quot_random_for_user = random.choice(quot_inspirational_for_usr)
    choice_of_usr = messagebox.askyesno("Exit Program", f"{quot_random_for_user}\n Are you sure you want to exit Byte & Bolt program?")
    if choice_of_usr:
        win.destroy()

# Home which is displayed in the menu.
def home_win_for_usr():
    global current_page, current_win, return_page_win
    

# My first window for the store.
win = Tk()
win.title("Byte & Bolt Tech Hire")
win.geometry("600x500")
win.configure(bg="#ADD8E6")

win.protocol("WM_DELETE_WINDOW", cnfrm_exit_program) 

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

drp_dwn_for_user.add_command(label="Main Menu", command=home_win_for_usr)
drp_dwn_for_user.add_command(label="Hire", command=lambda: choice_set_for_menu("Hire"))
drp_dwn_for_user.add_command(label="Return", command=lambda: choice_set_for_menu("Return"))

 
# Choice function to show what user selected.   
def choice_set_for_menu(value):
    if value =="Hire":
        computer_accessories()
    elif value =="Return":
        accessories_return()
        
# Search function for user to use. 
def search():
    if not etry.winfo_viewable():
        etry.pack(side="left", padx=5)
        srch_btn_user.config(text="Go")
    else: 
        text = etry.get().strip().lower()
        if text == "hire":
            computer_accessories()
        elif text == "return":
            accessories_return()
        elif text =="main menu":
            home_win_for_usr()
        else:
            messagebox.showerror("Error", "Type Hire or return or main menu.")
         
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
    
# I made the validations for all fields in hire page.
def save_records():
    global cart
    errors=[]

    if not first_name_box.get() or not first_name_box.get().replace(" ","").isalpha():
        errors.append("First name cannot be empty, contain integers, or contain symbols.")

    if not last_name_box.get() or not last_name_box.get().replace(" ","").isalpha():
        errors.append("Last name cannot be empty or contain integers.")

    if not contact_details_box.get() or not contact_details_box.get().replace(" ","").isdigit():
        errors.append("Contact Details cannot be empty or contain letters.")

    if len(contact_details_box.get()) != 10:
        errors.append("Contact details must be 10 numbers")

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

    # This generates a receipt number permanently for that customer. 
    receipt_no_fxd = None

    for rcrd in current_entries:
        if (rcrd["first_name"].lower() == first_name_box.get().lower()
            and rcrd["last_name"].lower() == last_name_box.get().lower()
            and rcrd["contact_details"] == contact_details_box.get()):

            receipt_no_fxd = rcrd["receipt_number"]
            break

    if receipt_no_fxd is None:
        receipt_no_fxd = str(random.randint(10000, 99999))

    # Saving all new records as well as the previous records of the customer.    
    new_record = {
        "first_name": first_name_box.get().strip(),
        "last_name": last_name_box.get().strip(),
        "contact_details": contact_details_box.get().strip(),
        "hire_date": hir_cale_etry.get(),
        "receipt_number": receipt_no_fxd, 
        "cart": list(cart)
    }

    customer_info["first_name"]= first_name_box.get().strip()
    customer_info["last_name"] = last_name_box.get().strip()
    customer_info["contact_details"] =  contact_details_box.get().strip()
    customer_info["hire_date"] = hir_cale_etry.get()
    customer_info["receipt_number"] = receipt_no_fxd
   
    for rcrd in current_entries:
        if(rcrd["first_name"].lower() == new_record["first_name"].lower() and rcrd["last_name"].lower() == new_record["last_name"].lower() and rcrd["contact_details"] == new_record["contact_details"]):
            rcrd["cart"].extend(cart)
            rcrd["hire_date"] = new_record["hire_date"]
            break
    else:
        current_entries.append(new_record)
        
    with open("customer_details.json", "w") as file:
        json.dump(current_entries, file, indent=4)

    cart.clear()

    # Clears all the details of the customer. 
    first_name_box.delete(0, END)
    last_name_box.delete(0, END)
    contact_details_box.delete(0, END)
    hir_cale_etry.delete(0, END)

    messagebox.showinfo("Success", "Record saved successfully!")

# I created a deleting record function. 
def delete_records():
    records = load_data()

    if not records:
        messagebox.showinfo("Records Empty", "There are no customer details saved")
        return

    # I created a new window for deleting records. 
    delete_win = Toplevel()
    delete_win.title("Select a record to delete")
    delete_win.geometry("500x500")
    delete_win.configure(bg=L_BLUE)

    Label(delete_win, text="Please select a record to delete:", font=("Arial", 12, "bold"), bg=L_BLUE, fg=NVY_BLUE).pack(pady=10)

    lst_frame = Frame(delete_win)
    lst_frame.pack(pady=10, padx=25, fill="both", expand=True)

    # I made a scrollbar so that it's easier for the user. 
    scrbr = Scrollbar(lst_frame)
    scrbr.pack(side="right", fill="y")

    listbox_records = Listbox(lst_frame, font=("Arial", 10), yscrollcommand=scrbr.set, selectmode="single", width=45, height=15)
    listbox_records.pack(side="left", fill="both", expand=True)
    scrbr.config(command=listbox_records.yview)

    for item in records:
        display = (
            "Name: "+ item["first_name"] + " " + item["last_name"] +
            "  |   Contact: " + item["contact_details"] +
            "             | Receipt No: " + item.get("receipt_number", "N/A, (save customer details first!)")
        )
        
        listbox_records.insert(END, display)

    # Validations for delete details function. 
    def delete_details():
        selected = listbox_records.curselection()

        if not selected:
            messagebox.showerror("Error", "Select a customer name first")
            return

        index = selected[0]
        
        records.pop(index)

        with open("customer_details.json", "w") as file:
            json.dump(records, file, indent=4)

        listbox_records.delete(index)

        messagebox.showinfo("Success", "Record is deleted successfully!")

    Button(delete_win, text="Delete", bg="red", fg=WHT, font=("Arial", 10, "bold"), width= 18, height=2, command=delete_details).pack(pady=10)
    Button(delete_win, text="Close", bg=NVY_BLUE, fg=WHT, width=18, height=2 , command=delete_win.destroy).pack(pady=5) 

# I created a function to exit the program. 
def exit_program():
    win.destroy()

# I made a new window for computer accessories. 
def computer_accessories():
    global cart, current_page, current_win
    if current_page[0]=="computer_accessories":
        return
    if current_win[0] is not None:
        current_win[0].destroy()
    win.withdraw()
   
    cmpacc_win = Toplevel()
    cmpacc_win.title("Computer Accesories")
    cmpacc_win.geometry("400x600")
    cmpacc_win.configure(bg=L_BLUE)

    current_win[0]= cmpacc_win
    current_page[0]="computer_accessories"

    # Function for closing the window. 
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

    # Function for adding accessories via quanitity picker. 
    def add():
        Accessories = selected_computer_accessories.get()
        if Accessories not in ACCESSORIES:
            messagebox.showerror("Select an item first")
            return
        # Validations for quantity picker. 
        try:
            qty = int(qty_picker.get())
        except ValueError:
            messagebox.showerror("Error", "Quantity must be a valid number")
            return
      
        if qty < 1:
            messagebox.showerror("Error", "Quantity can't be below 1")
            return
        elif qty > 20:
            messagebox.showerror("Error", "Contact our company for any higher purchase.") 
            return

        for _ in range(qty):
            cart.append(Accessories)

        status_box.config(text=f"{qty}x {Accessories} added")
        
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

    # Quantity picker for the better user interface.
    qty_label = Label(cmpacc_win, text="Select Quantity:", bg = L_BLUE, fg= NVY_BLUE, font=("Arial", 11, "bold"))
    qty_label.pack(pady=5)

    qty_picker = Spinbox(cmpacc_win, from_=1, to=20, width=5, font=("Arial", 12))
    qty_picker.pack()
    
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

# I made a new window for viewing receipt.
def view_receipt_page():
    global current_page, current_win, return_page_win
    if current_page[0]=="view_receipt_win":
        return
    if current_win[0] is not None:
        if current_page[0] == "accessories_return":
            current_win[0].withdraw()
        else:
            current_win[0].destroy()
   
    view_receipt_win = Toplevel()
    view_receipt_win.title("BYTE & BOLT RECEIPT")
    view_receipt_win.geometry("400x600")
    view_receipt_win.configure(bg="#ADD8E6")

    current_win[0]= view_receipt_win
    current_page[0]="view_receipt_win"

    # Function for closing the window. 
    def close():
        global current_page, current_win

        view_receipt_win.destroy()

        if return_page_win is not None:
            return_page_win.deiconify()
            return_page_win.lift()

            current_page[0]= "accessories_return"
            current_win[0]= return_page_win

        else:
            current_win[0] = None
            current_page[0] = None
            win.deiconify()
        
    # Tool bar which is shown in every page.
    rece_frame= Frame(view_receipt_win, bg= NVY_BLUE)
    rece_frame.pack(side="top", fill="x", ipady=4)

    # Main title for tech hire store.
    rece_title = Label( rece_frame, text="BYTE & BOLT RECEIPT", font=("Arial", 16, "bold"), bg=NVY_BLUE, fg=WHT)
    rece_title.pack(side="top", padx=10, pady=4)

    # Receipt created with customer details.
    def view_receipt():
        receipt_no=customer_info.get("receipt_number", "N/A, (save customer details first)")
        receipt_variable = StringVar(value=str(receipt_no))

        receipt_label= Label(view_receipt_win,text="Receipt Number:",bg=L_BLUE,fg=NVY_BLUE, font=("Arial",12, "bold"),width=15)
        receipt_label.place(relx=0.10, rely=0.22)

        receipt_entry=Entry(view_receipt_win, textvariable=receipt_variable, state="readonly",bg=L_BLUE,width=29)
        receipt_entry.place(relx=0.55, rely=0.22)

        Label(view_receipt_win, text="Date of Hire: " + customer_info.get("hire_date", ""), bg=L_BLUE, fg=NVY_BLUE, font=("Arial", 13, "bold")).place(relx=0.30, rely=0.10)
        
        Label(view_receipt_win, text=("----------------------"), bg = L_BLUE).place(relx= 0.35, rely=0.28)

        recei_name_lbl= Label(view_receipt_win,text="Customer name: " +customer_info.get("first_name","").title()+" "+customer_info.get("last_name","").title(),bg=L_BLUE, fg= NVY_BLUE, font=("Arial",13, "bold"),width=30)
        recei_name_lbl.place(relx=0.10, rely=0.15)
        
        itms_frame = Frame(view_receipt_win, bg=L_BLUE)
        itms_frame.place(relx=0.23, rely=0.33)
        
        total = 0

     # All purchases shown in the cart.
        receipt_cart = cart.copy()
        
        if not receipt_cart:
            Label(itms_frame, text="[You have nothing added in your cart!]", font =("Arial", 11), bg=L_BLUE, fg=NVY_BLUE).pack()
        else:
            for item in set(receipt_cart):
                qty = receipt_cart.count(item)
                prc_item = ACCESSORIES[item][1]
                subttl = prc_item * qty
                total += subttl

                item_txt = f"{qty}x {item} - $ {subttl}.00"
                Label(itms_frame, text=item_txt, font=("Arial", 11, "bold"), bg=L_BLUE, fg=NVY_BLUE).pack(anchor="w", pady=4)

                Label(view_receipt_win, text=("----------------------"), bg = L_BLUE).place(relx= 0.34, rely=0.55)
                
        # Total label and thankyou label. 
        total_Label = Label(view_receipt_win, text="Total $ " + str(total), font=("Arial", 14, "bold"), bg = L_BLUE, fg=NVY_BLUE)
        total_Label.place(relx = 0.34, rely= 0.63)
            
        Label(view_receipt_win, text=("----------------------"), bg = L_BLUE).place(relx= 0.34, rely=0.70)
        Label(view_receipt_win, text=("THANK YOU 😊"), bg = L_BLUE, font=("Arial", 17, "bold")).place(relx= 0.26, rely=0.75)

        if receipt_no != "N/A, (Please save customer details first!)":
            try:
                options = {"module_height": 8.0, "font_size": 10, "text_distance": 5.0, "background": L_BLUE}
                bar_code_for_rcpt = Code128(str(receipt_no), writer=ImageWriter())
                bar_code_for_rcpt.save("bar_code_rcpt", options=options)

                img = Image.open("bar_code_rcpt.png")
                img = img.resize((240, 65), Image.Resampling.LANCZOS)
                img_bar_code = ImageTk.PhotoImage(img)

                bar_code_label = Label(view_receipt_win, image=img_bar_code, bg=L_BLUE)
                bar_code_label.image = img_bar_code 
                bar_code_label.place(relx=0.20, rely=0.83)
            except Exception as e:
                print("Barcode Generation Error:", e)
                                                                
        # Close button. 
        bar_btn_close = Button(view_receipt_win, text="Close", bg=NVY_BLUE, fg=WHT, font=("Arial", 10, "bold"), width=12, command=close)
        bar_btn_close.place(relx=0.38, rely=0.94)

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

# I made a new window for return page.
def accessories_return():
    global current_page, current_win, return_page_win
    if current_page[0] == "accessories_return":
        return
    if current_win[0] is not None:
        current_win[0].destroy()
    win.withdraw()

    return_win_shown = Toplevel()
    return_win_shown.title("Return page")
    return_win_shown.geometry("600x500")
    return_win_shown.configure(bg=L_BLUE)

    return_page_win = return_win_shown

    current_win[0] = return_win_shown
    current_page[0] = "accessories_return"

    # Function created for closing window pages. 
    def close():
        global current_page, current_win, return_page_win

        current_page[0] = None
        current_win[0] = None
        return_page_win = None

        return_win_shown.destroy()
        win.deiconify()
 
    # Menu dropdown for return page.
    rtrn_tool_bar = Frame(return_win_shown, bg = NVY_BLUE)
    rtrn_tool_bar.pack(side="top", fill="x", ipady=3)

    rtrn_tl = Label(rtrn_tool_bar, text="Byte and Bolt Tech Hire return", font=("Arial", 16, "bold"), bg=NVY_BLUE, fg=WHT)
    rtrn_tl.pack(side="top", padx=10, pady=4)

    rtrn_btn_dsp = Menubutton(rtrn_tool_bar, text="☰", font=("Arial", 15), bg=L_BLUE)
    rtrn_btn_dsp.pack(side="left")
    rtrn_btn_dsp.place(relx=0.05, rely=0.15)

    rtrn_drp_dwn_for_user = Menu(rtrn_btn_dsp, tearoff=0)
    rtrn_btn_dsp["menu"] = rtrn_drp_dwn_for_user
    
    rtrn_drp_dwn_for_user.add_command(label="Main Menu", command=home_win_for_usr)
    rtrn_drp_dwn_for_user.add_command(label="Hire", command=lambda: [close(), computer_accessories()])
    rtrn_drp_dwn_for_user.add_command(label="Return", command=lambda: None)

    # Search Button for return page.    
    def rtrn_search():
        if not etry_rtrn.winfo_viewable():
            etry_rtrn.pack(side="left", padx=5)
            srch_btn_return.config(text="Go")
            return

        text = etry_rtrn.get().strip().lower()
        
        if text == "hire":
            computer_accessories()
        elif text == "return":
            accessories_return()
        elif text =="main menu":
            home_win_for_usr()
        else:
            messagebox.showerror("Error", "Type Hire or return or main menu.")
       
    etry_rtrn = Entry(rtrn_tool_bar)

    srch_btn_return = Button(rtrn_tool_bar, text="🔍", font=("Arial", 13), bg=L_BLUE, command=rtrn_search)
    srch_btn_return.pack(side="left")
    srch_btn_return.place(relx=0.13, rely=0.15)
    
    # Customer details shown in return page.
    Label(return_win_shown, text="Please enter the following to view customer file:", font=("Arial", 12, "bold"), bg=L_BLUE, fg=NVY_BLUE).pack(pady=10)

    Label(return_win_shown, text="First Name:", font=("Arial", 10, "bold"), bg=L_BLUE, fg=NVY_BLUE).pack()
    frst_box_rtrn = Entry(return_win_shown, font=("Arial", 11), width=25)
    frst_box_rtrn.pack(pady=2)

    Label(return_win_shown, text="Last Name:", font=("Arial", 10, "bold"), bg=L_BLUE, fg=NVY_BLUE).pack()
    lst_box_rtrn = Entry(return_win_shown, font=("Arial", 11), width=25)
    lst_box_rtrn.pack(pady=2)

    Label(return_win_shown, text="Contact Details:", font=("Arial", 10, "bold"), bg=L_BLUE, fg=NVY_BLUE).pack()
    cnt_box_rtrn = Entry(return_win_shown, font=("Arial", 11), width=25)
    cnt_box_rtrn.pack(pady=2)

    full_name_of_cust = Label(return_win_shown, text="Customer name: ", bg=L_BLUE, fg=NVY_BLUE, font=("Arial", 11, "bold"))
    full_name_of_cust.pack(pady=(10, 2))

    cnt_details_of_usr = Label(return_win_shown, text="Contact Details: ", font=("Arial", 11, "bold"), bg=L_BLUE, fg=NVY_BLUE)
    cnt_details_of_usr.pack(pady=2)

    # Function created for selecting which particular item the customer wants to return. 
    def item_rtrn_cust(rcrds_list_of_customer, cust_idx_matched):
        global cart
        if not cart:
            messagebox.showinfo("Info", "This customer has no hires left in their cart to return!")
            return

        # A window for selecting item/s to return. 
        item_rtrn_slct_win = Toplevel()
        item_rtrn_slct_win.title("Select Item to Return")
        item_rtrn_slct_win.geometry("300x350")
        item_rtrn_slct_win.configure(bg=L_BLUE)

        Label(item_rtrn_slct_win, text="Pick an item to return:", font=("Arial", 11, "bold"), bg=L_BLUE, fg=NVY_BLUE).pack(pady=10)

        # A listbox to show the items the customer currently has hired. 
        item_lst_box_customer = Listbox(item_rtrn_slct_win, font=("Arial", 10), selectmode="single", width=25, height=10)
        item_lst_box_customer.pack(pady=5)

        items_dstnct = list(set(cart))
        for item in items_dstnct:
            count = cart.count(item)
            item_lst_box_customer.insert(END, f"{item} (Qty: {count})")

        # Item confirmation function for user. 
        def item_cnfrm_selection():
            global cart
            selection = item_lst_box_customer.curselection()
            if not selection:
                messagebox.showerror("Error", " Select an item from the list first!")
                return

            # Selecting and removing the chosen accesories purchased. 
            selected_txt = item_lst_box_customer.get(selection[0])
            acc_chosen_by_cst = selected_txt.split(" (Qty:")[0]

            cart.remove(acc_chosen_by_cst)

            bar_btn_return.config(text=f"Return amount: ${ACCESSORIES[acc_chosen_by_cst][1]}")

            # Matching the customer details that were previously saved. 
            rcrds_list_of_customer[cust_idx_matched]["cart"] = list(cart)
            with open("customer_details.json", "w") as file:
                json.dump( rcrds_list_of_customer, file, indent=4)

            messagebox.showinfo("Success", f"Successfully returned 1x {acc_chosen_by_cst}!")

            item_lst_box_customer.delete(0, END)

            # Counting the amount of items purchaed and showing it. 
            for item in set(cart):
                count = cart.count(item)
                item_lst_box_customer.insert(END, f"{item} (Qty: {count})")

            # Returning back to the return win. 
            return_win_shown.lift()

        # Buttons created for cofirming return and closing window. 
        Button(item_rtrn_slct_win, text="Confirm Return", bg=NVY_BLUE, fg=WHT, font=("Arial", 10, "bold"), command=item_cnfrm_selection).pack(pady=10)
        Button(item_rtrn_slct_win, text="Close", bg="red", fg=WHT, font=("Arial", 10, "bold"), command=item_rtrn_slct_win.destroy).pack()

    # Created a small window just to show customer details with their receipt number. 
    def rcpt_no_show():
        rcpt_no_win = Toplevel(return_win_shown)
        rcpt_no_win.title("Receipt Number")
        rcpt_no_win.geometry("300x150")
        rcpt_no_win.configure(bg=L_BLUE)

        # Labels for the receipt function. 
        Label(rcpt_no_win, text=f"{customer_info['first_name'].title()} {customer_info['last_name'].title()}", bg=L_BLUE, fg=NVY_BLUE, font=("Arial", 12, "bold")).pack(pady=(20, 10))
        Label(rcpt_no_win, text=f"Receipt Number: {customer_info['receipt_number']}", bg=L_BLUE, fg=NVY_BLUE, font=("Arial", 12, "bold")).pack()

    # Function for searching the data of the customer.
    def lkup_cst_run_search(mode_action):
        global customer_info, cart

        frst_input_of_customer = frst_box_rtrn.get().strip()
        lst_input_of_customer = lst_box_rtrn.get().strip()
        cnt_input_of_customer = cnt_box_rtrn.get().strip()

        # Validation for customer lookup function. 
        if not frst_input_of_customer or not lst_input_of_customer or not cnt_input_of_customer:
            messagebox.showerror("Error", "Enter first name, last name, contact details please!")
            return
        
        # Reloading the file to make sure that the current changes are kept.
        records = load_data()
        match_fnd_of_customer = None
        idx_match_customer = -1

        idx = 0
        while idx < len(records):
            r = records[idx]
            if r["first_name"].lower() == frst_input_of_customer.lower() and r["last_name"].lower() == lst_input_of_customer.lower() and r["contact_details"] == cnt_input_of_customer:
                match_fnd_of_customer = r
                idx_match_customer = idx
                break
            idx += 1

        # Validation for saved records. 
        if idx_match_customer == -1:
            messagebox.showerror("Error", "No saved records are matched with those customer details")
            return

        # Making sure that the customer details matches. 
        customer_info["first_name"] = match_fnd_of_customer ["first_name"]
        customer_info["last_name"] = match_fnd_of_customer ["last_name"]
        customer_info["contact_details"] = match_fnd_of_customer ["contact_details"]
        customer_info["receipt_number"] = match_fnd_of_customer.get("receipt_number", "Save customer details on home page!")
        customer_info["hire_date"] = match_fnd_of_customer.get("hire_date", "") 
        
        cart.clear()
        cart.extend(match_fnd_of_customer.get("cart", []))

        # Labels with details shown. 
        full_name_of_cust.config(text="Customer name: " + customer_info["first_name"].title() + " " + customer_info["last_name"].title())
        cnt_details_of_usr.config(text="Contact Details: " + customer_info["contact_details"])

        if mode_action == "view":
            view_receipt_page()
        elif mode_action == "return":
            item_rtrn_cust(records, idx_match_customer)
        elif mode_action == "rcpt_only":
            rcpt_no_show()
            
    # All buttons and a button container for return page.
    bar_btn_customer = Frame(return_win_shown, bg=L_BLUE)
    bar_btn_customer.pack(pady=15)

    bar_btn_view_purchases= Button(bar_btn_customer, text="View purchases", bg=NVY_BLUE, fg=WHT, font=("Arial", 11, "bold"), width=15, height=2, command=lambda:lkup_cst_run_search("view"))
    bar_btn_view_purchases.pack(side="left", padx=2)

    bar_btn_return_item = Button(bar_btn_customer, text="Return item", bg=NVY_BLUE, fg=WHT, font=("Arial", 11, "bold"), width=15, height=2, command=lambda:lkup_cst_run_search("return"))
    bar_btn_return_item.pack(side="left", padx=2)

    bar_btn_return= Label(return_win_shown, text="Return amount: $0", bg=L_BLUE, fg=NVY_BLUE, font=("Arial", 11, "bold"))
    bar_btn_return.pack(pady=5)
    
    bar_btn_receipt_no = Button(bar_btn_customer, text="Receipt number", bg=NVY_BLUE, fg=WHT, font=("Arial", 11, "bold"), width=15, height=2, command=lambda:lkup_cst_run_search("rcpt_only"))
    bar_btn_receipt_no.pack(side="left", padx=2)

    quit_btn = Button(return_win_shown, text="Quit", bg=NVY_BLUE, fg=WHT, font=("Arial", 11, "bold"), width=15, height=2, command=close)
    quit_btn.pack(pady=15)

# Looping the program created.   
win.mainloop()
