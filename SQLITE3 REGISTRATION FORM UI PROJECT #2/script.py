import tkinter, sqlite3
root = tkinter.Tk()

class reg:
    def __init__(self, master):
        self.master = master 
        self.master.title("Registration Form")
        self.master.geometry('500x500')

        tkinter.Label(self.master, text="Registration Form", width=20, font=('bold', 20), fg='green').place(x=93, y=53)

        tkinter.Label(self.master, text="Full Name", width=10, font=('bold', 10)).place(x=160, y=123)
        self.fullname_Entry = tkinter.Entry(self.master, width=15)
        self.fullname_Entry.place(x=240, y=125)

        tkinter.Label(self.master, text="Email", width=10, font=('bold', 10)).place(x=160, y=163)
        self.email_Entry = tkinter.Entry(self.master, width=15)
        self.email_Entry.place(x=240, y=165)

        genderVar = tkinter.StringVar()
        genderVar.set("Male")
        tkinter.Label(self.master, text="Gender", width=10, font=('bold', 10)).place(x=160, y=203)
        self.male_Radiobutton = tkinter.Radiobutton(self.master, text="Male", value="Male", variable=genderVar)
        self.female_Radiobutton = tkinter.Radiobutton(self.master, text="Female", value="Female", variable=genderVar)
        self.male_Radiobutton.place(x=240 ,y=205)
        self.female_Radiobutton.place(x=300, y=205)

        pythonVar = tkinter.StringVar()
        pythonVar.set("Python")
        javaVar = tkinter.StringVar()
        javaVar.set("Java")
        tkinter.Label(self.master, text="Programming", width=10, font=('bold', 10)).place(x=160, y=243)
        self.pythonCheckbutton = tkinter.Checkbutton(self.master, text="Python", variable=pythonVar, onvalue="Python", offvalue="Not Python")
        self.javaCheckbutton = tkinter.Checkbutton(self.master, text="Java", variable=javaVar, onvalue="Java", offvalue="Not Java")
        self.pythonCheckbutton.place(x=240, y=245)
        self.javaCheckbutton.place(x=300, y=245)

        self.SubmitButton = tkinter.Button(self.master, text="Submit !", fg="#FFFFFF", bg="red", font=('Courier', 15))
        self.SubmitButton.configure(command=lambda:self.submit(self.fullname_Entry, self.email_Entry, genderVar, pythonVar, javaVar))
        self.SubmitButton.place(x=200, y=290)

    def submit(self, fullname, email, gender, python, java):
        self.FullName = fullname
        self.email = email
        self.gender = gender 
        self.python = python 
        self.java = java 

        self.FullName = self.FullName.get()
        self.email = self.email.get()
        self.gender = self.gender.get()
        self.python = self.python.get()
        self.java = self.java.get()

        self.connection = sqlite3.connect('database.db')
        self.connection_cursor = self.connection.cursor()
        self.connection_cursor.execute("CREATE TABLE IF NOT EXISTS myTable(FullName TEXT, Email TEXT, Gender TEXT, Python TEXT, Java TEXT)")

        self.connection_cursor.execute("INSERT INTO myTable VALUES('{0}', '{1}', '{2}', '{3}', '{4}')".format(self.FullName, self.email, self.gender, self.python, self.java)) 
        self.connection.commit()
        
registration = reg(root)    
root.mainloop()
