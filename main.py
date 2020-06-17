from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
from tkinter import ttk
import os, pickle

class File_App:
    def __init__(self,root):
        self.root=root
        self.root.title("File Management".center(420))
        self.root.configure(background = "black")
        bg_color="#074463" 
        self.root.geometry("1350x700+0+0")
        
        title=Label(self.root,text="File Based Record System",font=("times new roman",35,"bold"),bd=5,relief=GROOVE ,bg="yellow",pady=2).pack(fill=X)

        Student=LabelFrame(self.root, bd=10, relief=GROOVE,font=("times new roman",30,"bold"),fg="gold",bg=bg_color)
        Student.place(x=0,y=70,height=460)

        stitle=Label(Student,text="Student Details",bg=bg_color, fg="white",font=("times new roman",30, "bold")).grid(row=0,columnspan=4,pady=10)


        #--------------Variables-----------------
        self.s_id =StringVar()
        self.name =StringVar()
        self.course =StringVar()
        self.address =StringVar()
        self.city =StringVar()
        self.contact =StringVar()
        self.date =StringVar()
        self.degree =StringVar()
        self.id_proof =StringVar()
        self.payment =StringVar()





        lblsid=Label(Student,text="Student Id",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=1,column=0,padx=20,pady=10,sticky="w")
        txtsid=Entry(Student,bd=7,relief=GROOVE,textvariable=self.s_id,width=21,font="arial 15 bold").grid(row=1,column=1,padx=20,pady=10)
     
        lblname=Label(Student,text="Name",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(sticky="w",row=2,column=0,padx=20,pady=10)
        txtname=Entry(Student,bd=7,relief=GROOVE,textvariable=self.name, width=21,font="arial 15 bold").grid(row=2,column=1,padx=20,pady=10,sticky="w")

        lblcontact=Label(Student,text="Contact",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=1,sticky="w",column=2,padx=20,pady=10)
        txtcontact=Entry(Student,bd=7,relief=GROOVE,textvariable=self.contact,width=21,font="arial 15 bold").grid(row=1,column=3,padx=20,pady=10)

        
        lbldate=Label(Student,text="Date(dd/mm/yyyy)",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(sticky="w",row=2,column=2,padx=20,pady=10)
        txtdate=Entry(Student,bd=7,relief=GROOVE,textvariable=self.date,width=21,font="arial 15 bold").grid(row=2,column=3,padx=20,pady=10)

        
        lblcouse=Label(Student,text="Course",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=3,sticky="w",column=0,padx=20,pady=10)
        txtcourse=Entry(Student,bd=7,relief=GROOVE,textvariable=self.course,width=21,font="arial 15 bold").grid(row=3,column=1,padx=20,pady=10)

        
        lblSD=Label(Student,text="Select Degree",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=3,sticky="w",column=2,padx=20,pady=10)

        
        lbladdress=Label(Student,text="Address",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=4,sticky="w",column=0,padx=20,pady=10)
        txtaddress=Entry(Student,bd=7,textvariable=self.address,relief=GROOVE,width=21,font="arial 15 bold").grid(row=4,column=1,padx=20,pady=10)

        
        lblIP=Label(Student,text="ID Proof",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=4,sticky="w",column=2,padx=20,pady=10)

        
        lblcity=Label(Student,text="City",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=5,column=0,sticky="w",padx=20,pady=10)
        txtcity=Entry(Student,bd=7,relief=GROOVE,textvariable=self.city,width=21,font="arial 15 bold").grid(row=5,column=1,padx=20,pady=10)

        
        lblPM=Label(Student,text="Payment Mode",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(sticky="w",row=5,column=2,padx=20,pady=10)
        
        degreecombobox=ttk.Combobox(Student,width=20, textvariable=self.degree,state="readonly",font="arial 15 bold")
        degreecombobox['values']=("BCA","MCA","B.Tech","MBA","M.Tech")
        degreecombobox.grid(row=3,column=3,pady=10, padx=20)   
        
        IPcombobox=ttk.Combobox(Student,width=20, textvariable=self.id_proof,state="readonly",font="arial 15 bold")
        IPcombobox['values']=("Addhar Card","Pan Card","Driving Licence","PassPort","VoterId Card")
        IPcombobox.grid(row=4,column=3,pady=10, padx=20)

        PMcombobox=ttk.Combobox(Student,width=20, textvariable=self.payment,state="readonly",font="arial 15 bold")
        PMcombobox['values']=("Cash","NEFT","Internet Banking","Credit Card","Debit Card","Paytm","PhonePay")
        PMcombobox.grid(row=5,column=3,pady=10, padx=20)


        btnframe=Frame(self.root,bd=10,relief=GROOVE, bg="light blue")
        btnframe.place(x=0,y=535,width=1350, height=290)

        btnsave=Button(btnframe,text="Save", command=self.save_data, font="arial 15 bold", bd=7, width=18,height=3,bg="yellow").grid(row=0,column=0,padx=15,pady=30)
        btndelete=Button(btnframe,text="Delete",command=self.delete, font="arial 15 bold", bd=7, width=18,height=3,bg="yellow").grid(row=0,column=1,padx=15,pady=30)
        btnclear=Button(btnframe,text="Clear", command=self.clear,font="arial 15 bold", bd=7, width=18,height=3,bg="yellow").grid(row=0,column=2,padx=15,pady=30)
        btnlog=Button(btnframe,text="Logout", command=self.logout,font="arial 15 bold", bd=7, width=18,height=3,bg="yellow").grid(row=0,column=3,padx=15,pady=30)
        btnexit=Button(btnframe,text="Exit", command=self.exit,font="arial 15 bold", bd=7, width=18,height=3, bg="yellow").grid(row=0,column=4,padx=15,pady=30)

        fileframe=Frame(self.root,bd=10,relief=GROOVE)
        fileframe.place(x=915, y=70,width=440,height=460)

        ftitle=Label(fileframe,text="All Files", font="arial 20 bold",bd=5,relief=GROOVE,bg="light blue").pack(side=TOP,fill=X)

        scroll_y=Scrollbar(fileframe,orient=VERTICAL)
        self.f_list=Listbox(fileframe,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.f_list.yview)
        self.f_list.pack(fill=BOTH,expand=1)

        self.f_list.bind("<ButtonRelease-1>",self.get_data)
        self.show_files()

    def save_data(self):
        present="no"
        if self.s_id.get()=="":
            messagebox.showerror("Error","Student Id must be Required!!!")
        else:
            f=os.listdir("Files/")
            if len(f)>0:
                for i in f:
                    if i.split(".")[0] == self.s_id.get():
                        present="yes"
                if present=="yes":
                    ask=messagebox.askyesnocancel("Update","File already presennt \nDo you really want to Update?!!")
                    if ask>0:
                        self.save_file()
                        messagebox.showinfo("Update","Record has Been saved!!")
                        self.show_files()
                else:
                    self.save_file()
                    messagebox.showinfo("Saved","Record has Been saved!!")
                    self.show_files()      
    
            else:
                self.save_file()
                messagebox.showinfo("Saved","Record has Been saved!!")
                self.show_files()      
    
    def save_file(self):
        f=open("Files/"+str(self.s_id.get())+".txt","w")
        f.write(
                    str(self.s_id.get())+","+
                    str(self.name.get())+","+
                    str(self.course.get())+","+
                    str(self.address.get())+","+
                    str(self.city.get())+","+
                    str(self.contact.get())+","+
                    str(self.date.get())+","+
                    str(self.degree.get())+","+
                    str(self.id_proof.get())+","+
                    str(self.payment.get())
                )
        f.close()
        self.show_files()    
           
    def show_files(self):
        Files=os.listdir("Files/")
        self.f_list.delete(0,END)
        if len(Files)>0:        
            for i in Files:
                self.f_list.insert(END,i)

    def get_data(self,ev):
        getcursor=self.f_list.curselection()
        #print(self.f_list.get(getcursor))
        f1=open("Files/"+self.f_list.get(getcursor))
        value=[]
        for f in f1:
            value=f.split(",")
        self.s_id.set(value[0])
        self.name.set(value[1])
        self.course.set(value[2])
        self.address.set(value[3])
        self.city.set(value[4])
        self.contact.set(value[5])
        self.date.set(value[6])
        self.degree.set(value[7])
        self.id_proof.set(value[8])
        self.payment.set(value[9])


    def clear(self):
        self.s_id.set("")
        self.name.set("")
        self.course.set("")
        self.address.set("")
        self.city.set("")
        self.contact.set("")
        self.date.set("")
        self.degree.set("")
        self.id_proof.set("")
        self.payment.set("")
    
    def delete(self):
        present="no"
        if self.s_id.get()=="":
            messagebox.showerror("Error","Student Id must be Required!!!")
        else:
            f=os.listdir("Files/")
            if len(f)>0:
                for i in f:
                    if i.split(".")[0] == self.s_id.get():
                        present="yes"
                if present=="yes":
                    ask=messagebox.askyesnocancel("Delete","Do you really want to delete?!!")
                    if ask>0:
                        os.remove("Files/"+self.s_id.get()+".txt")
                        messagebox.showinfo("Success","Deleted Successfully")
                        self.show_files()
                else:
                    messagebox.showerror("Error","File not found!!!!")

    def exit(self):
        ask=messagebox.askyesnocancel("Exit","Do you really want to Exit?!!")
        if ask>0:
            self.root.destroy()
        else:
            return

    def logout(self):
        self.root.destroy()
        import login

root=Tk()
obj=File_App(root)
root.mainloop()
