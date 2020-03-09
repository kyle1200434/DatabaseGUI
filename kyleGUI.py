from tkinter import *
import csv
from tkinter import messagebox as ms
import uuid


global data
global row
data = []
with open('ambot.csv', 'r') as rf:
    n = csv.reader(rf)
    for row in n:
        if row:
            data.append(row)


# Main Class which consist of all operations and codes for the GUI
class main:
    def __init__(self, master):
        self.master = master
        self.fullname = StringVar()
        self.email = StringVar()
        self.number = StringVar()
        self.var = StringVar()
        self.optionList = ["Mobile", "Work", "Home"]

        self.n_fullName = StringVar()
        self.n_email = StringVar()
        self.n_number = StringVar()
        self.n_var = StringVar()
        self.n_mobile = StringVar()
        self.n_work = StringVar()
        self.n_home = StringVar()
        # Create Widgets
        self.widgets()

    # This Function is used to search and verify if a contact exists
    def search_contacts(self):
        mirror = bool
        fullname = self.n_fullName.get()
        for row in data:
            for field in row:
                if field == fullname:
                    mirror = True
                    print(row)
                    print(data)
                    # display fullname
                    Label(self.find, text='             Full Name: ', font=('', 15), pady=5, padx=5, bg = 'yellow', fg= '#970af5').grid(row=4, column=0)
                    name = Label(self.find, text=str(row[0]), font=('', 15), bg = 'yellow', fg= '#970af5')
                    name.grid(row=4, column=1)
                    Button(self.find, text='EDIT', bd=3, font=('', 10), padx=5, command=self.UpdateName).grid(row=4,
                                                                                                              column=2)

                    # email
                    Label(self.find, text='                E-MAIL: ', font=('', 15), pady=5, padx=5, bg = 'yellow', fg= '#970af5').grid(row=5, column=0)
                    email = Label(self.find, text=row[1], font=('', 15), bg = 'yellow', fg= '#970af5')
                    email.grid(row=5, column=1)
                    Button(self.find, text='EDIT', bd=3, font=('', 10), padx=5, command=self.UpdatEmail).grid(row=5,
                                                                                                              column=2)

                    # mobile
                    Label(self.find, text='MOBILE NUMBER: ', font=('', 15), pady=5, padx=5, bg = 'yellow', fg= '#970af5').grid(row=6, column=0)
                    mobile = Label(self.find, text=row[3], font=('', 15), bg = 'yellow', fg= '#970af5')
                    mobile.grid(row=6, column=1)
                    Button(self.find, text='EDIT', bd=3, font=('', 10), padx=5, command=self.UpdateMobile).grid(row=6,
                                                                                                                column=2)
                    # work
                    Label(self.find, text='  WORK NUMBER: ', font=('', 15), pady=5, padx=5, bg = 'yellow', fg= '#970af5').grid(row=7, column=0)
                    work = Label(self.find, text=row[4], font=('', 15), bg = 'yellow', fg= '#970af5')
                    work.grid(row=7, column=1)
                    Button(self.find, text='EDIT', bd=3, font=('', 10), padx=5, command=self.UpdateWork).grid(row=7,
                                                                                                             column=2)

                    # home
                    Label(self.find, text='   HOME NUMBER: ', font=('', 15), pady=5, padx=5, bg = 'yellow', fg= '#970af5').grid(row=8, column=0)
                    home = Label(self.find, text=row[5], font=('', 15), bg = 'yellow', fg= '#970af5')
                    home.grid(row=8, column=1)
                    Button(self.find, text='EDIT', bd=3, font=('', 10), padx=5, command=self.UpdateHome).grid(row=8,
                                                                                                              column=2)
                    Button(self.find, text='UPDATE', bd=3, font=('', 15), padx=5, command=self.update_writer, bg = 'yellow', fg= '#970af5').grid(
                        row=10, column=0)
                    Button(self.find, text='DELETE', bd=3, font=('', 15), padx=5, command=self.Delete, bg = 'yellow', fg= '#970af5').grid(row=10,
                                                                                                            column=1)

        if mirror != True:
            ms.showerror('Error', 'Name not found!')

    # This Function is used Edit the Name of the contact
    def UpdateName(self):
        fullname = self.n_fullName.get()
        for row in data:
            for field in row:
                if field == fullname:
                    Entry(self.find, textvariable=self.n_fullName, bd=5, font=('', 15)).grid(row=4, column=1)
                    x = int()
                    mirror = bool
                    full_name = self.n_fullName.get()
                    for row in data:
                        for field in row:
                            if field == self.fullname.get():
                                mirror = True
                    if mirror == True:
                        ms.showerror('Oops!', 'A contact with the same name Already exists')
                    else:
                        while x != 1:
                            for row in data:
                                for field in row:
                                    if field == full_name:
                                        row[0] = full_name
                        with open('ambot.csv', 'w') as wf:
                            write_data = csv.writer(wf)
                            for line in data:
                                write_data.writerow(line)

    # This Function is used Edit the Name of the contact
    def UpdatEmail(self):
        fullname = self.n_fullName.get()
        for row in data:
            for field in row:
                if field == fullname:
                    Entry(self.find, textvariable=self.n_email, bd=5, font=('', 15)).grid(row=5, column=1)
                    x = int()
                    full_name = self.n_fullName.get()
                    email_info = self.n_email.get()
                    while x != 1:
                        for row in data:
                            for field in row:
                                if field == full_name:
                                    row[1] = email_info
                                    x = 1
                    with open('ambot.csv', 'w') as wf:
                        write_data = csv.writer(wf)
                        for line in data:
                            write_data.writerow(line)

    # This Function is used Edit the Name of the contact
    def UpdateMobile(self):
        fullname = self.n_fullName.get()
        for row in data:
            for field in row:
                if field == fullname:
                    Entry(self.find, textvariable=self.n_mobile, bd=5, font=('', 15)).grid(row=6, column=1)
                    x = int()
                    full_name = self.n_fullName.get()
                    mobile = self.n_mobile.get()
                    while x != 1:
                        for row in data:
                            for field in row:
                                if field == full_name:
                                    row[3] = mobile
                                    x = 1
                    with open('ambot.csv', 'w') as wf:
                        write_data = csv.writer(wf)
                        for line in data:
                            write_data.writerow(line)

    # This Function is used Edit the Name of the contact
    def UpdateWork(self):
        fullname = self.n_fullName.get()
        for row in data:
            for field in row:
                if field == fullname:
                    Entry(self.find, textvariable=self.n_work, bd=5, font=('', 15)).grid(row=7, column=1)

                    x = int()
                    full_name = self.n_fullName.get()
                    work = self.n_work.get()
                    while x != 1:
                        for row in data:
                            for field in row:
                                if field == full_name:
                                    row[4] = work
                                    x = 1
                    with open('ambot.csv', 'w') as wf:
                        write_data = csv.writer(wf)
                        for line in data:
                            write_data.writerow(line)

    # This Function is used Edit the Name of the contact
    def UpdateHome(self):
        fullname = self.n_fullName.get()
        for row in data:
            for field in row:
                if field == fullname:
                    Entry(self.find, textvariable=self.n_home, bd=5, font=('', 15)).grid(row=8, column=1)
                    x = int()
                    full_name = self.n_fullName.get()
                    home = self.n_home.get()
                    while x != 1:
                        for row in data:
                            for field in row:
                                if field == full_name:
                                    row[5] = home
                                    x = 1
                    with open('ambot.csv', 'w') as wf:
                        write_data = csv.writer(wf)
                        for line in data:
                            write_data.writerow(line)

    # This Function is used to write the manipulated database list to an external database
    def update_writer(self):
        ms.showinfo('Success!', 'Contact Updated')
        with open('ambot.csv', 'w') as wf:
            write_data = csv.writer(wf)
            for line in data:
                write_data.writerow(line)
        root.destroy()

        print(data)

    # This Function is used to Delete a certain contact
    def Delete(self):
        full_name = self.n_fullName.get()
        for row in data:
            for field in row:
                if full_name == field:
                    data.remove(row)
                    with open('ambot.csv', 'w') as wf:
                        write_data = csv.writer(wf)
                        for line in data:
                            write_data.writerow(line)
                    print(data)
        ms.showinfo('Success!', 'Contact Deleted')
        with open('ambot.csv', 'w') as wf:
            write_data = csv.writer(wf)
            for line in data:
                write_data.writerow(line)
        root.destroy()

    # This Function is used to add Contacts and to append a certain data to the global variable
    def add_contacts(self):
        print(data)
        mobile = str()
        work = str()
        home = str()
        mirror = bool
        fullname = self.fullname.get()
        for row in data:
            for field in row:
                if field == self.fullname.get():
                    mirror = True
        if mirror == True:
            ms.showerror('Oops!', 'A contact with the same name Already exists')
        else:
            email = self.email.get()
            type = self.var.get()
            id = uuid.uuid4()
            print(type)
            if type == 'Mobile':
                mobile = self.number.get()
                print(mobile)
                work = 'None'
                home = 'None'
            elif type == 'Work':
                work = self.number.get()
                print(work)
                mobile = 'None'
                home = 'None'
            elif type == 'Home':
                home = self.number.get()
                print(home)
                mobile = 'None'
                work = 'None'
            with open('ambot.csv', 'a') as rf:
                fieldnames = ['FULL_NAME', 'EMAIL', 'ID', 'MOBILE', 'WORK', 'HOME']
                n = csv.DictWriter(rf, fieldnames=fieldnames)
                n.writerow(
                    {'FULL_NAME': fullname, 'EMAIL': email, 'ID': id, 'MOBILE': mobile, 'WORK': work, 'HOME': home, })
                

            ms.showinfo('Success!', 'Contact Added')
            root.destroy()

    # This Functions are used to setup the Packing methods of the widgets for the GUI
    def main(self):
        self.n_fullName.set('')
        self.n_email.set('')
        self.create.pack_forget()
        self.head['text'] = 'Select Your Choice'
        self.home.pack()

    def add(self):
        self.n_fullName.set('')
        self.n_email.set('')
        self.home.pack_forget()
        self.head['text'] = 'ADD NEW CONTACT'
        self.create.pack()

    def search(self):
        self.n_fullName.set('')
        self.n_email.set('')
        self.home.pack_forget()
        self.create.pack_forget()
        self.find.pack_forget()
        self.head['text'] = 'SEARCH CONTACT'
        self.find.pack()

    # This is used to setup the interface
    def widgets(self):
        # entry part
        self.head = Label(self.master, text="\n      \n     Huawei Numbawan     \n       \n", font=('', 24), fg= '#970af5')
        self.head.configure(background = 'Yellow') 
        self.head.pack()
        Label(self.master, text="", bg = '#970af5').pack()

        ##------- HOME --------##
        self.home = Frame(self.master, padx=10, pady=1, bg = '#970af5')
        # buttons part
        Button(self.home, text='\n           Search Contacts           \n', bd=3,fg = '#970af5', bg = 'Light Pink', font=('', 14), padx=5, pady=5, command=self.search).pack()
        Label(self.home, text="", bg = '#970af5').pack()
        Button(self.home, text='\n             Add Contacts             \n', bd=3,fg = '#970af5', bg = 'Light Pink', font=('', 14), padx=5, pady=5, command=self.add).pack()
        Label(self.home, text="", bg = '#970af5').pack()
        self.home.pack()
        ##------- ADD CONTACTS --------##
        self.create = Frame(self.master, padx=10, pady=10, bg = '#970af5')
        Label(self.create, text='              Enter Full Name:\n', font=('', 15), pady=0, padx=0, bg= 'Yellow', fg = '#970af5').grid(sticky=W, row=2, column=0)
        Entry(self.create, textvariable=self.fullname, bd=5, font=('', 15)).grid(row=2, column=1)

        Label(self.create, text='      Enter E-mail Address:\n', font=('', 15), pady=0, padx=0, bg= 'Yellow', fg = '#970af5').grid(sticky=W)
        Entry(self.create, textvariable=self.email, bd=5, font=('', 15)).grid(row=3, column=1)

        Label(self.create, text='                 Enter Number:\n', font=('', 15), pady=0, padx=0, bg= 'Yellow', fg = '#970af5').grid(sticky=W)
        Label(self.create, text='Type:', font=('', 15), pady=5, padx=5, bg= 'Yellow', fg = '#970af5').grid(row=4,column = 2)
        OptionMenu(self.create, self.var, *self.optionList).grid(row=4, columnspan=2, column = 3)
        Entry(self.create, textvariable=self.number, bd=5, font=('', 15)).grid(row=4, column=1)

        Label(self.create, text='', bg='#970af5').grid(sticky=W)

        Button(self.create, text='Add Contact', bg= 'Yellow', fg = '#970af5', bd=3, font=('', 15), padx=5, pady=5, command=self.add_contacts).grid(
            row=8, columnspan=4)
        ##------- SEARCH --------##
        self.find = Frame(self.master, padx=10, pady=10, bg = '#970af5')
        Label(self.find, text='  Enter Full Name: ', font=('', 15), pady=5, padx=5, bg= 'Yellow', fg = '#970af5').grid(sticky=W, row=2, column=0)
        Entry(self.find, textvariable=self.n_fullName, bd=5, font=('', 15)).grid(row=2, column=1)
        Button(self.find, text='Search', bg= 'Yellow', fg = '#970af5', bd=3, font=('', 15), padx=0, pady=0, command=self.search_contacts).grid(
            column=2, row=2)


# Runs the GUI
root = Tk()
root.configure(bg= '#970af5')
main(root)
root.title("Phone")
root.mainloop()