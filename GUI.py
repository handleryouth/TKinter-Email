import tkinter as tk
from tkinter import filedialog, Scrollbar
from email_smptp_using_pdf import attachment_file, sending_without_file

namefile = []

def attachment_button2():
    global namefile
    file_send = filedialog.askopenfilename()
    namefile.append(file_send)
    number = len(namefile)
    if len(namefile) > 1:
        print(f'{number} files selected')
        tk.Label(window, text=f'{number} files selected', background='steel blue').grid(row=6, column=3)
    else:
        tk.Label(window, text=f'{number} file selected', background='steel blue').grid(row=6, column=3)
        print(f'{number} file selected')

def attachment_button():
    subject = e4.get()
    text = e5.get("1.0", 'end-1c')
    email_adress = e1.get()
    send_to = e3.get()
    email_password = e2.get()
    if  namefile:
        file_name = namefile[0:]
        attachment_file(file_name, text, email_password, email_adress, send_to, subject)
        tk.Label(window, text='Mail Sent', background='steel blue').grid(row=8, column=1)
    else:
        sending_without_file(email_adress, send_to, subject, text, email_password)

def list_filename():
    name_only=[]
    x = 6
    if namefile:
        for n in namefile:
            name = str(n)
            name2 = name.split('/')[-1]
            name_only.append(name2)
        for n in name_only:
            tk.Label(window, text=n, background='steel blue').grid(row=x, column=2)
            x += 1
    else:
        tk.Label(window, text='None', background='steel blue').grid(row=6, column=2)
    view_files.grid_forget()
    view_files.grid(row= 7 + len(namefile), column=2)


window = tk.Tk()

window.title('Sending Email, built in python')
window.configure(bg='steelblue')
tk.Label(window, text ='Email Account :', background='steel blue').grid(row=0)
tk.Label(window, text ='Password:', background='steel blue').grid(row=1)
tk.Label(window, text ='Send to:', background='steel blue').grid(row=2)
tk.Label(window, text ='Subject:', background='steel blue').grid(row=3)
tk.Label(window, text ='Message Here:', background='steel blue').grid(row=4)
tk.Label(window, text ='Attachment (All type)', background='steel blue').grid(row=6)

attachment_click = tk.Button(window, text='Select Files', command = attachment_button2)
submit_button = tk.Button(window, text='Submit', command = attachment_button)
view_files = tk.Button(window, text='view files you have attached', command=list_filename)



e1 = tk.Entry(window, width=40)
e2 = tk.Entry(window, width=40, show='*')
e3 = tk.Entry(window, width=40)
e4 = tk.Entry(window, width=40)
scrollbar = Scrollbar(window)
e5 = tk.Text(width = 70, height=30)
scrollbar.config(command=e5.yview, orient='vertical' , highlightcolor='steel blue')
scrollbar.grid(column=2, row=5, sticky='ns')
e5.configure(yscrollcommand=scrollbar.set)


e1.grid(row =0, column=1)
e2.grid(row =1, column=1)
e3.grid(row =2, column=1)
e4.grid(row = 3, column=1)
e5.grid(row = 5, column =1)

attachment_click.grid(row=6, column=1, ipadx=50)
submit_button.grid(row=7, column=1)
view_files.grid(row=7, column=2)

window.mainloop()
