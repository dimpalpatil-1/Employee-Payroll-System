from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # pip install pillow
import pymysql

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration")
        self.root.geometry("1350x700+0+0")
        # ==Bg Image===

        self.bg = ImageTk.PhotoImage(file="images/b2.jpg")
        bg = Label(self.root, image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)

        # ==left Image===

        self.left = ImageTk.PhotoImage(file="images/side.png")
        left = Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)

        # ======Registration Frame
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)
        title = Label(frame1, text="REGISTER HERE", font=("times new roman", 18, "bold"), bg="white", fg="green").place(
            x=50, y=30)

        # ===========Row1
        f_name = Label(frame1, text="First Name", font=("times new roman", 14, "bold"), bg="white", fg="gray").place(
            x=50, y=100)
        self.txt_fname = Entry(frame1, font=("times new roman", 14), bg="light gray")
        self.txt_fname.place(x=50, y=130, width=250)

        l_name = Label(frame1, text="Last Name", font=("times new roman", 14, "bold"), bg="white", fg="gray").place(
            x=370, y=100)
        self.txt_lname = Entry(frame1, font=("times new roman", 14), bg="light gray")
        self.txt_lname.place(x=370, y=130, width=250)

        # ===========Row2
        contact = Label(frame1, text="Contact", font=("times new roman", 14, "bold"), bg="white", fg="gray").place(
            x=50, y=170)
        self.txt_contact = Entry(frame1, font=("times new roman", 14), bg="light gray")
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame1, text="Email", font=("times new roman", 14, "bold"), bg="white", fg="gray").place(
            x=370, y=170)
        self.txt_email = Entry(frame1, font=("times new roman", 14), bg="light gray")
        self.txt_email.place(x=370, y=200, width=250)

        # ===========Row3
        question = Label(frame1, text="Security Questios", font=("times new roman", 14, "bold"), bg="white",
                         fg="gray").place(x=50, y=240)

        self.cmb_quest = ttk.Combobox(frame1, font=("times new roman", 12), state="readonly", justify=CENTER)
        self.cmb_quest['values'] = ("Select", "Your first pet name", "Your birth place", "Your best friend name")
        self.cmb_quest.place(x=50, y=270, width=250)
        self.cmb_quest.current(0)

        answer = Label(frame1, text="Answers", font=("times new roman", 14, "bold"), bg="white", fg="gray").place(
            x=370, y=240)
        self.txt_answer = Entry(frame1, font=("times new roman", 14), bg="light gray")
        self.txt_answer.place(x=370, y=270, width=250)

        # ===========Row4
        password = Label(frame1, text="Password", font=("times new roman", 14, "bold"), bg="white",
                         fg="gray").place(x=50, y=310)
        self.txt_password = Entry(frame1, font=("times new roman", 14), bg="light gray")
        self.txt_password.place(x=50, y=340, width=250)

        cpassword = Label(frame1, text="Confirm Password", font=("times new roman", 14, "bold"), bg="white",
                          fg="gray").place(x=370, y=310)
        self.txt_cpassword = Entry(frame1, font=("times new roman", 14), bg="light gray")
        self.txt_cpassword.place(x=370, y=340, width=250)

        # =========Terms
        self.var_chk = IntVar()
        chk = Checkbutton(frame1, text="I agree the terms and conditions.", variable=self.var_chk, onvalue=1,
                          offvalue=0, bg="white", font=(10)).place(x=50, y=380)

        # ====Register now
        btn_register = Button(frame1, text="  Register now →  ", bg="light green", bd=3,
                              font=("times new roman", 14, "bold"), cursor="hand2", command=self.register_data).place(
            x=50, y=420)

        # ====Username
        username_label = Label(self.root, text="Username (Email)", font=("times new roman", 14, "bold"), bg="white",
                               fg="gray").place(x=100, y=150)
        self.txt_username = Entry(self.root, font=("times new roman", 14), bg="light gray")
        self.txt_username.place(x=100, y=190, width=250)

        # ====Password
        password_label = Label(self.root, text="Password", font=("times new roman", 14, "bold"), bg="white",
                               fg="gray").place(x=100, y=230)
        self.txt_password_login = Entry(self.root, font=("times new roman", 14), bg="light gray", show="*")
        self.txt_password_login.place(x=100, y=270, width=250)

        # ====Sign in
        btn_login = Button(self.root, text="Sign in", bg="light green", bd=3, font=("times new roman", 14, "bold"),
                           cursor="hand2", command=self.sign_in).place(x=100, y=310, width=100)

    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.cmb_quest.delete(0, END)
        self.txt_answer.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_cpassword.delete(0, END)
        self.cmb_quest.current(0)
        self.var_chk.set(0)
        self.txt_fname.focus_set()

    def register_data(self):
        if self.txt_fname.get() == "" or self.txt_lname.get() == "" or self.txt_contact.get() == "" or \
                self.txt_email.get() == "" or self.cmb_quest.get() == "Select" or self.txt_answer.get() == "" or \
                self.txt_password.get() == "" or self.txt_cpassword.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)

        elif self.txt_password.get() != self.txt_cpassword.get():
            messagebox.showerror("Error", "Password and Confirm Password does not match", parent=self.root)

        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Please agree our terms and conditions", parent=self.root)

        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password="", database="employee2")
                cur = con.cursor()
                cur.execute("select * from employee where email= %s", self.txt_email.get())
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "User already exists, please try with another email", parent=self.root)
                else:
                    cur.execute(
                        "insert into employee (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                        (self.txt_fname.get(),
                         self.txt_lname.get(),
                         self.txt_contact.get(),
                         self.txt_email.get(),
                         self.cmb_quest.get(),
                         self.txt_answer.get(),
                         self.txt_password.get()
                         ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Registration Successful", parent=self.root)
                    self.clear()

            except Exception as es:
                messagebox.showerror("Error", f"Error due to :{str(es)}", parent=self.root)

    def sign_in(self):
        username = self.txt_username.get()
        password = self.txt_password_login.get()

        try:
            con = pymysql.connect(host='localhost', user='root', password="", database="employee2")
            cur = con.cursor()
            cur.execute("select * from employee where email= %s and password= %s", (username, password))
            row = cur.fetchone()
            con.close()

            if row is not None:
                messagebox.showinfo("Success", "Sign in Successful", parent=self.root)
                # Add your code for what to do after successful sign-in
                self.root.destroy()
                import employee
            else:
                messagebox.showerror("Error", "Invalid username or password", parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Error due to :{str(es)}", parent=self.root)

root = Tk()
obj = Register(root)
root.mainloop()
