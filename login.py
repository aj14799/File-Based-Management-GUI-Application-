from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
class win1:
    def __init__(self):
        self.root=Tk()
        self.root.title("File Based Management".center(420))
        self.root.configure(background = "black")
        bg_color="#074463" 
        self.root.geometry("1350x700+0+0")

        self.bg_icon=ImageTk.PhotoImage(file="maxresdefault.jpg")
        self.user_icon=ImageTk.PhotoImage(file="download (1).jpg")
        self.pass_icon=ImageTk.PhotoImage(file="download (1).png")
        self.logo_icon=ImageTk.PhotoImage(file="logo.jpg")
        self.signup_icon=ImageTk.PhotoImage(file="signup.jpg")
        
        #------------Variable----------------#
        self.uname=StringVar()
        self.pass_=StringVar()

        bg_lbl=Label(self.root,image=self.bg_icon).pack(fill=Y)
        
        title=Label(self.root,text="File Based Management",font=("times new roman",40,"bold"),bd=5,relief=GROOVE, fg="white", bg=bg_color,pady=2)
        title.place(x=0, y=0,relwidth=1)

        F1=LabelFrame(self.root, bd=10, relief=GROOVE, text="Welcome to File Based Management",font=("times new roman",30,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1,height=160)

        lbl=Label(F1,text="CREATOR:---",bg=bg_color, fg="white",font=("times new roman",20, "bold")).grid(row=0,column=0,padx=20,pady=10)

        lbl2=Label(F1,text="Aditya Jha",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=0,column=2,padx=20,pady=10)

        Login_Frame=LabelFrame(self.root, bd=10, relief=GROOVE, text="LogIn",font=("times new roman",20,"bold"),fg="gold",bg=bg_color)
        Login_Frame.place(x=750,y=290,height=350)


        logolbl=Label(Login_Frame, image= self.logo_icon,bd=0).grid(row=0,columnspan=2,pady=10)
        
        userlbl=Label(Login_Frame, text="Username", compound=LEFT, font= ("times new roman",20,"bold"),image= self.user_icon,bg="white").grid(row=1,column=0,padx=20,pady=10)
        txtuser=Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)
        
        passlbl=Label(Login_Frame, text="Password", compound=LEFT, font= ("times new roman",20,"bold"),image= self.pass_icon,bg="white").grid(row=2,column=0,padx=20,pady=10)
        txtpass=Entry(Login_Frame,bd=5,textvariable=self.pass_,relief=GROOVE,font=("",15),show="*").grid(row=2,column=1,padx=20)

        btn_login=Button(Login_Frame,text="Login", command=self.logfun, width=15,font=("arial 15 bold"),bg="yellow",fg="red").grid(row=3,column=1,pady=10)
        
       # btn_signup=Button(Login_Frame, image=self.signup_icon, width=130, font=("times new roman",14,"bold"),bg=bg_color).grid(row=3,column=0,pady=10)

        

        self.root.mainloop()

    def logfun(self):
        if self.uname.get()=="Aditya" and self.pass_.get()=="AA":
            messagebox.showinfo("Info",f"Welcome{self.uname.get()}")
            self.root.destroy()
            import main
        
        elif self.uname.get()=="" or self.pass_.get()=="":
            messagebox.showerror("Error","All fields must!!")
        else:
            messagebox.showerror("Error","Invalid Username or Password!!")




obj=win1()
