from operator import index
from tkinter import *
from tkinter import ttk
import sqlite3



c = sqlite3.connect("Student.db")
curses=c.cursor()
curses.execute("CREATE TABLE IF NOT EXISTS Student(ID INTEGER,NAME VARCHAR(20),AGE INTEGER,DOB VARCHAR(20),GENDER VARCHAR(20),CITY VARCHAR(20))")
c.commit()
c.close()
print("TABLE CREATED")
class student:
    def __init__(self,main):
        self.main=main
        self.T_Frame=Frame(self.main,height=50,width=1200, background="yellow", bd=2)
        self.T_Frame.pack()
        self.Title=Label(self.T_Frame, text="Student Management System", font="arial 20 bold", width=1200,bg="yellow")
        self.Title.pack()

        self.Frame_1=Frame(self.main, height=580,width=400,bd=2, relief=GROOVE,bg="blue")
        self.Frame_1.pack(side=LEFT)
        self.Frame_1.pack_propagate(0)



        Label(self.Frame_1, text="Student Details",bg="blue",font="arial 12 bold").place(x=20,y=20)

        self.Id=Label(self.Frame_1, text="Id", bg="blue",font="arial 11 bold")
        self.Id.place(x=40,y=60)
        self.Id_Entry=Entry(self.Frame_1,width=40)
        self.Id_Entry.place(x=150,y=60)


        self.Name=Label(self.Frame_1, text="Name", bg="blue",font="arial 11 bold")
        self.Name.place(x=40,y=100)
        self.Name_Entry=Entry(self.Frame_1,width=40)
        self.Name_Entry.place(x=150,y=100)




        self.Age = Label(self.Frame_1, text="Age", bg="blue", font="arial 11 bold")
        self.Age.place(x=40, y=140)
        self.Age_Entry = Entry(self.Frame_1, width=40)
        self.Age_Entry.place(x=150, y=140)

        self.DOB = Label(self.Frame_1, text="DOB", bg="blue", font="arial 11 bold")
        self.DOB.place(x=40, y=180)
        self.DOB_Entry = Entry(self.Frame_1, width=40)
        self.DOB_Entry.place(x=150, y=180)

        self.Gender = Label(self.Frame_1, text="Gender", bg="blue", font="arial 11 bold")
        self.Gender.place(x=40, y=220)
        self.Gender_Entry = Entry(self.Frame_1, width=40)
        self.Gender_Entry.place(x=150, y=220)

        self.City = Label(self.Frame_1, text="City", bg="blue", font="arial 11 bold")
        self.City.place(x=40, y=260)
        self.City_Entry = Entry(self.Frame_1, width=40)
        self.City_Entry.place(x=150, y=260)

        ####### Button #######

        self.Button_Frame=Frame(self.Frame_1,height=250,width=250,relief=GROOVE,bd=2,bg="blue")
        self.Button_Frame.place(x=80,y=300)

        self.Add=Button(self.Button_Frame,text="Add",width=25,font="arial 11 bold",command=self.Add)
        self.Add.pack()

        self.Delete = Button(self.Button_Frame, text="Delete",width=25,font="arial 11 bold",command=self.Delete)
        self.Delete.pack()

        self.Update = Button(self.Button_Frame, text="Update",width=25,font="arial 11 bold",command=self.Update)
        self.Update.pack()

        self.Clear = Button(self.Button_Frame, text="Clear",width=25,font="arial 11 bold",command=self.Clear)
        self.Clear.pack()

        self.Frame_2=Frame(self.main,height=580,width=800,bd=2,relief=GROOVE,bg="yellow")
        self.Frame_2.pack(side=RIGHT)

        self.tree=ttk.Treeview(self.Frame_2,columns=("c1", "c2", "c3", "c4", "c5","c6"),show='headings', height=25)

        self.tree.column("#1",anchor=CENTER,width=50)
        self.tree.heading("#1",text="ID")


        self.tree.column("#2", anchor=CENTER)
        self.tree.heading("#2", text="Name")

        self.tree.column("#3", anchor=CENTER, width=110)
        self.tree.heading("#3", text="DOB")

        self.tree.column("#4", anchor=CENTER, width=115)
        self.tree.heading("#4", text="Age")

        self.tree.column("#5", anchor=CENTER, width=110)
        self.tree.heading("#5", text="Gender")

        self.tree.column("#6", anchor=CENTER)
        self.tree.heading("#6", text="City")
        self.tree.insert("",index=0,values=(24,"pavithran",20,"24-12-2003","male","chennai"))
        self.tree.pack()


    def Add(self):
        id=self.Id_Entry.get()
        name=self.Name_Entry.get()
        age=self.Age_Entry.get()
        dob=self.DOB_Entry.get()
        gender=self.Gender_Entry.get()
        city=self.City_Entry.get()
        c=sqlite3.connect("Student.db")
        curses=c.cursor()
        curses.execute("INSERT INTO Student(ID,NAME,AGE,DOB,GENDER,CITY)VALUES(?,?,?,?,?,?)",(id,name,age,dob,gender,city))
        c.commit()
        c.close()
        print("value inserted")

        self.tree.insert("",index=0,values=(id,name,age,dob,gender,city))


    def Delete(self):
        item=self.tree.selection()[0]
        selected_item=self.tree.item(item)['values'][0]
        print(selected_item)
        c=sqlite3.connect("Student.db")
        cursor=c.cursor()
        cursor.execute("DELETE FROM Student WHERE ID={}".format(selected_item))
        print("value deleted")
        c.commit()
        c.close()
        self.tree.delete(item)

    def Update(self):
        id=self.Id_Entry.get()
        name=self.Name_Entry.get()
        age=self.Age_Entry.get()
        dob=self.DOB_Entry.get()
        gender=self.Gender_Entry.get()
        city=self.City_Entry.get()
        item=self.tree.selection()[0]
        selected_item=self.tree.item(item)['values'][0]
        c=sqlite3.connect("student.db")
        cursor=c.cursor()
        cursor.execute("UPDATE Student SET ID=?,AGE=?,DOB=?,GENDER=?,CITY=? WHERE ID=?" ,(selected_item,name,age,dob,gender,city))
        c.commit()
        c.close()
        print("values updated")
        self.tree.item(item, values=(id,name,age,dob,gender,city))

    def Clear(self):
        self.Id_Entry.delete(0,END)
        self.Name_Entry.delete(0, END)
        self.Age_Entry.delete(0, END)
        self.DOB_Entry.delete(0, END)
        self.Gender_Entry.delete(0, END)
        self.City_Entry.delete(0, END)

main=Tk()
main.title("Student management system")
main.resizable(False,False)
main.geometry("1200x600")

student(main)
main.mainloop()
