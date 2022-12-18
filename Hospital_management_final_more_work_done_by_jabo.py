from tkinter import *

root=Tk()


def Show_P():
    global Patient_frame
    Patient_frame=Frame(root,bg="white")
    Main_frame.destroy()
    Patient_frame.place(x=10,y=100,height=400,width=700)
    Button_Add=Button(Patient_frame,text="Add New Record",font=("Times New Roman",15),command=Add_P,cursor="hand2",bg="grey",width=40,height=2)
    Button_Add.place(x=120,y=20)
    Button_Del=Button(Patient_frame,text="Delete Existing Record",font=("Times New Roman",15),command=Del_P,cursor="hand2",bg="grey",width=40,height=2)
    Button_Del.place(x=120,y=100)
    Button_Dis=Button(Patient_frame,text="Display Existing Record",font=("Times New Roman",15),command=Disp_P,cursor="hand2",bg="grey",width=40,height=2)
    Button_Dis.place(x=120,y=180)
    Button_Mod=Button(Patient_frame,text="Modify Existing Record",font=("Times New Roman",15),command=Mod_P,cursor="hand2",bg="grey",width=40,height=2)
    Button_Mod.place(x=120,y=260)
    Button_Back=Button(Patient_frame,text="Back",font=("Times New Roman",7),command=Main_Frame,cursor="hand2",bg="grey",width=5)
    Button_Back.place(x=2,y=2)
    
def Add_P():
    global ROA
    global DOA
    global D_Name
    global Room_no
    global P_name
    global Add_P_frame
    Add_P_frame=Frame(root,bg="white")
    Patient_frame.destroy()
    Add_P_frame.place(x=10,y=100,height=400,width=700)
    P_name=Entry(Add_P_frame,width=80,border=5)
    P_name.place(x=120,y=20)
    P_name.insert(0,"Enter Patient's name : ")
    ROA=Entry(Add_P_frame,width=80,border=5)
    ROA.place(x=120,y=80)
    ROA.insert(0,"Enter Reason of Admission : ")
    DOA=Entry(Add_P_frame,width=80,border=5)
    DOA.place(x=120,y=140)
    DOA.insert(0,"Enter Date of Admission : ")
    D_Name=Entry(Add_P_frame,width=80,border=5)
    D_Name.place(x=120,y=200)
    D_Name.insert(0,"Enter Doctor's Name : ")
    Room_no=Entry(Add_P_frame,width=80,border=5)
    Room_no.place(x=120,y=260)
    Room_no.insert(0,"Enter Room Number : ")
    Button_Back=Button(Add_P_frame,text="Back",font=("Times New Roman",7),command=Show_P,cursor="hand2",bg="grey",width=5)
    Button_Back.place(x=2,y=2)
    Submit=Button(Add_P_frame,text="Submit",font=("Times New Roman",15),command=lambda:[add_p(),Show_P()],cursor="hand2",bg="grey",width=10,height=1)
    Submit.place(x=300,y=320)
def Del_P():
    global Del_P_frame
    global DelP_ID
    Del_P_frame=Frame(root,bg="white")
    Patient_frame.destroy()
    Del_P_frame.place(x=10,y=100,height=400,width=700)
    DelP_ID=Entry(Del_P_frame,width=80,border=5)
    DelP_ID.place(x=120,y=20)
    DelP_ID.insert(0,"Enter Patient ID whose record you want to delete : ")
    Submit=Button(Del_P_frame,text="Submit",font=("Times New Roman",15),command=lambda:[del_p(),Show_P()],cursor="hand2",bg="grey",width=10,height=1)
    Submit.place(x=300,y=320)
    Button_Back=Button(Del_P_frame,text="Back",font=("Times New Roman",7),command=Show_P,cursor="hand2",bg="grey",width=5)
    Button_Back.place(x=2,y=2)
def Disp_P():
    global Disp_P_frame
    global DisP_ID
    Disp_P_frame=Frame(root,bg="white")
    Patient_frame.destroy()
    Disp_P_frame.place(x=10,y=100,height=400,width=700)
    DisP_ID=Entry(Disp_P_frame,width=80,border=5)
    DisP_ID.place(x=120,y=20)
    DisP_ID.insert(0,"Enter Patient ID whose record you want to See : ")
    Submit=Button(Disp_P_frame,text="Submit",font=("Times New Roman",15),command=disp_p,cursor="hand2",bg="grey",width=10,height=1)
    Submit.place(x=300,y=320)
    Button_Back=Button(Disp_P_frame,text="Back",font=("Times New Roman",7),command=Show_P,cursor="hand2",bg="grey",width=5)
    Button_Back.place(x=2,y=2)
def Mod_P():
    global Mod_P_frame
    Mod_P_frame=Frame(root,bg="white")
    Patient_frame.destroy()
    Mod_P_frame.place(x=10,y=100,height=400,width=700)
    Button_name=Button(Mod_P_frame,text="Change Patient Name  ",font=("Times New Roman",15),command=ModPName,cursor="hand2",bg="grey",width=40,height=2)
    Button_name.place(x=120,y=10)
    Button_ROA=Button(Mod_P_frame,text="Change Reason of Admission  ",font=("Times New Roman",15),command=ModPROA,cursor="hand2",bg="grey",width=40,height=2)
    Button_ROA.place(x=120,y=90)
    Button_DOA=Button(Mod_P_frame,text="Change Date of Admission  ",font=("Times New Roman",15),command=ModPDOA,cursor="hand2",bg="grey",width=40,height=2)
    Button_DOA.place(x=120,y=170)
    Button_D_name=Button(Mod_P_frame,text="Change Doctor Name  ",font=("Times New Roman",15),command=ModPDName,cursor="hand2",bg="grey",width=40,height=2)
    Button_D_name.place(x=120,y=250)
    Button_Room_no=Button(Mod_P_frame,text="Change Room Number  ",font=("Times New Roman",15),command=ModPRoomNo,cursor="hand2",bg="grey",width=40,height=2)
    Button_Room_no.place(x=120,y=330)
    Button_Back=Button(Mod_P_frame,text="Back",font=("Times New Roman",7),command=Show_P,cursor="hand2",bg="grey",width=5)
    Button_Back.place(x=2,y=2)

def ModPName():
    global ModPName_frame
    global ModPName_ID
    global Mod_PName
    ModPName_frame=Frame(root,bg="white")
    Patient_frame.destroy()
    ModPName_frame.place(x=10,y=100,height=400,width=700)
    ModPName_ID=Entry(ModPName_frame,width=80,border=5)
    ModPName_ID.place(x=120,y=20)
    ModPName_ID.insert(0,"Enter Patient ID whose name you want to modify : ")
    Mod_PName=Entry(ModPName_frame,width=80,border=5)
    Mod_PName.place(x=120,y=100)
    Mod_PName.insert(0,"Enter modified name : ")
    Submit=Button(ModPName_frame,text="Submit",font=("Times New Roman",15),command=lambda:[modpname(),Mod_P()],cursor="hand2",bg="grey",width=10,height=1)
    Submit.place(x=300,y=320)
    Button_Back=Button(ModPName_frame,text="Back",font=("Times New Roman",7),command=Show_P,cursor="hand2",bg="grey",width=5)
    Button_Back.place(x=2,y=2)
    
def ModPROA():
    global ModPROA_frame
    global ModPROA_ID
    global Mod_Proa
    ModPROA_frame=Frame(root,bg="white")
    Patient_frame.destroy()
    ModPROA_frame.place(x=10,y=100,height=400,width=700)
    ModPROA_ID=Entry(ModPROA_frame,width=80,border=5)
    ModPROA_ID.place(x=120,y=20)
    ModPROA_ID.insert(0,"Enter Patient ID whose Reason of Admission you want to modify : ")
    Mod_Proa=Entry(ModPROA_frame,width=80,border=5)
    Mod_Proa.place(x=120,y=100)
    Mod_Proa.insert(0,"Enter modified ROA : ")
    Submit=Button(ModPROA_frame,text="Submit",font=("Times New Roman",15),command=lambda:[modroa(),Mod_P()],cursor="hand2",bg="grey",width=10,height=1)
    Submit.place(x=300,y=320)
    Button_Back=Button(ModPROA_frame,text="Back",font=("Times New Roman",7),command=Show_P,cursor="hand2",bg="grey",width=5)
    Button_Back.place(x=2,y=2)

def ModPDOA():
    global ModPDOA_frame
    global ModPDOA_ID
    global Mod_Pdoa
    ModPDOA_frame=Frame(root,bg="white")
    Patient_frame.destroy()
    ModPDOA_frame.place(x=10,y=100,height=400,width=700)
    ModPDOA_ID=Entry(ModPDOA_frame,width=80,border=5)
    ModPDOA_ID.place(x=120,y=20)
    ModPDOA_ID.insert(0,"Enter Patient ID whose DOA you want to modify : ")
    Mod_Pdoa=Entry(ModPDOA_frame,width=80,border=5)
    Mod_Pdoa.place(x=120,y=100)
    Mod_Pdoa.insert(0,"Enter modified DOA : ")
    Submit=Button(ModPDOA_frame,text="Submit",font=("Times New Roman",15),command=lambda:[moddoa(),Mod_P()],cursor="hand2",bg="grey",width=10,height=1)
    Submit.place(x=300,y=320)
    Button_Back=Button(ModPDOA_frame,text="Back",font=("Times New Roman",7),command=Show_P,cursor="hand2",bg="grey",width=5)
    Button_Back.place(x=2,y=2)

def ModPDName():
    global ModPDName_frame
    global ModPDName_ID
    global Mod_Pdname
    ModPDName_frame=Frame(root,bg="white")
    Patient_frame.destroy()
    ModPDName_frame.place(x=10,y=100,height=400,width=700)
    ModPDName_ID=Entry(ModPDName_frame,width=80,border=5)
    ModPDName_ID.place(x=120,y=20)
    ModPDName_ID.insert(0,"Enter Patient ID whose Doctor's Name you want to modify : ")
    Mod_Pdname=Entry(ModPDName_frame,width=80,border=5)
    Mod_Pdname.place(x=120,y=100)
    Mod_Pdname.insert(0,"Enter modified doctor's name : ")
    Submit=Button(ModPDName_frame,text="Submit",font=("Times New Roman",15),command=lambda:[moddocname(),Mod_P()],cursor="hand2",bg="grey",width=10,height=1)
    Submit.place(x=300,y=320)
    Button_Back=Button(ModPDName_frame,text="Back",font=("Times New Roman",7),command=Show_P,cursor="hand2",bg="grey",width=5)
    Button_Back.place(x=2,y=2)

def ModPRoomNo():
    global ModPRoomNo_frame
    global ModPRNO_ID
    global Mod_Prno
    ModPRoomNo_frame=Frame(root,bg="white")
    Patient_frame.destroy()
    ModPRoomNo_frame.place(x=10,y=100,height=400,width=700)
    ModPRNO_ID=Entry(ModPRoomNo_frame,width=80,border=5)
    ModPRNO_ID.place(x=120,y=20)
    ModPRNO_ID.insert(0,"Enter Patient ID whose Room No. you want to modify : ")
    Mod_Prno=Entry(ModPRoomNo_frame,width=80,border=5)
    Mod_Prno.place(x=120,y=100)
    Mod_Prno.insert(0,"Enter modified Room No. : ")
    Submit=Button(ModPRoomNo_frame,text="Submit",font=("Times New Roman",15),command=lambda:[modroomno(),Mod_P()],cursor="hand2",bg="grey",width=10,height=1)
    Submit.place(x=300,y=320)
    Submit.bind("<Enter>", lambda:[modroomno(),Mod_P()])
    Button_Back=Button(ModPRoomNo_frame,text="Back",font=("Times New Roman",7),command=Show_P,cursor="hand2",bg="grey",width=5)
    Button_Back.place(x=2,y=2)

    
#DOCTOR

def Show_D():
    global Doctor_frame
    Doctor_frame=Frame(root,bg="white")
    Main_frame.destroy()
    Doctor_frame.place(x=10,y=100,height=400,width=700)
    Button_Add=Button(Doctor_frame,text="Add New Record",font=("Times New Roman",15),command=Add_D,cursor="hand2",bg="grey",width=40,height=3)
    Button_Add.place(x=120,y=20)
    Button_Del=Button(Doctor_frame,text="Delete Existing Record",font=("Times New Roman",15),command=Del_D,cursor="hand2",bg="grey",width=40,height=3)
    Button_Del.place(x=120,y=140)
    Button_Dis=Button(Doctor_frame,text="Display Existing Record",font=("Times New Roman",15),command=Disp_D,cursor="hand2",bg="grey",width=40,height=3)
    Button_Dis.place(x=120,y=260)
    Button_Back=Button(Doctor_frame,text="Back",font=("Times New Roman",7),command=Main_Frame,cursor="hand2",bg="grey",width=5)
    Button_Back.place(x=2,y=2)


def Add_D():
    global Salary
    global Age
    global Dname
    global Field
    global Position
    global Add_D_frame
    Add_D_frame=Frame(root,bg="white")
    Doctor_frame.destroy()
    Add_D_frame.place(x=10,y=100,height=400,width=700)
    Dname=Entry(Add_D_frame,width=80,border=5)
    Dname.place(x=120,y=20)
    Dname.insert(0,"Enter Doctor's name : ")
    Salary=Entry(Add_D_frame,width=80,border=5)
    Salary.place(x=120,y=80)
    Salary.insert(0,"Enter Salary : ")
    Age=Entry(Add_D_frame,width=80,border=5)
    Age.place(x=120,y=140)
    Age.insert(0,"Enter Doctor's Age : ")
    Position=Entry(Add_D_frame,width=80,border=5)
    Position.place(x=120,y=200)
    Position.insert(0,"Enter Doctor's Position : ")
    Field=Entry(Add_D_frame,width=80,border=5)
    Field.place(x=120,y=260)
    Field.insert(0,"Enter Field : ")
    Button_Back=Button(Add_D_frame,text="Back",font=("Times New Roman",7),command=Show_D,cursor="hand2",bg="grey",width=5)
    Button_Back.place(x=2,y=2)
    Submit=Button(Add_D_frame,text="Submit",font=("Times New Roman",15),command=lambda:[Add_d(),Show_D()],cursor="hand2",bg="grey",width=10,height=1)
    Submit.place(x=300,y=320)


def Del_D():
    global Del_D_frame
    global DelD_ID
    Del_D_frame=Frame(root,bg="white")
    Doctor_frame.destroy()
    Del_D_frame.place(x=10,y=100,height=400,width=700)
    DelD_ID=Entry(Del_D_frame,width=80,border=5)
    DelD_ID.place(x=120,y=20)
    DelD_ID.insert(0,"Enter Doctor ID whose record you want to delete : ")
    Button_Back=Button(Del_D_frame,text="Back",font=("Times New Roman",7),command=Show_D,cursor="hand2",bg="grey",width=5)
    Button_Back.place(x=2,y=2)
    Submit=Button(Del_D_frame,text="Submit",font=("Times New Roman",15),command=lambda:[del_d(),Show_D()],cursor="hand2",bg="grey",width=10,height=1)
    Submit.place(x=300,y=320)
def Disp_D():
    global Disp_D_frame
    global DisD_ID
    Disp_D_frame=Frame(root,bg="white")
    Doctor_frame.destroy()
    Disp_D_frame.place(x=10,y=100,height=400,width=700)
    DisD_ID=Entry(Disp_D_frame,width=80,border=5)
    DisD_ID.place(x=120,y=20)
    DisD_ID.insert(0,"Enter Doctor ID whose record you want to See : ")
    Submit=Button(Disp_D_frame,text="Submit",font=("Times New Roman",15),command=disp_d,cursor="hand2",bg="grey",width=10,height=1)
    Submit.place(x=300,y=320)
    Button_Back=Button(Disp_D_frame,text="Back",font=("Times New Roman",7),command=Show_D,cursor="hand2",bg="grey",width=5)
    Button_Back.place(x=2,y=2)






root.title("JAAM Hospital database")
root.geometry("720x540+200+50")
root.resizable(False,False)
Heading=Label(root,text="JAAM HOSPITAL",font=("Times New Roman",30)).place(x=200,y=10)
def Main_Frame():
    global Main_frame

    Main_frame=Frame(root,bg="white")
    Main_frame.place(x=10,y=100,height=400,width=700)
    Button_P=Button(Main_frame,text="Use Patient Database",font=("Times New Roman",15),cursor="hand2",command=Show_P,bg="grey",padx=60,pady=175)
    Button_D=Button(Main_frame,text="Use Doctor Database",font=("Times New Roman",15),cursor="hand2",command=Show_D,bg="grey",padx=60,pady=175)
    Button_P.place(x=35,y=5)
    Button_D.place(x=375,y=5)
Main_Frame()








#====================SQL=====================

import pymysql as py

con=py.connect(host="127.0.0.1", user="root", database="hospital", passwd="Ferrari550#")
cur=con.cursor()

def add_p():
    global con
    N=0
    cur.execute("Select p_id from patient")
    Rec=cur.fetchall()
    if len(Rec)!=0:
        for i in Rec:
            ID=i[0]+1
    
    else:
        ID=0
    cur.execute(F"insert into patient values('{ID}','{P_name.get()}','{ROA.get()}','{DOA.get()}','{D_Name.get()}','{Room_no.get()}')")
    con.commit()
    
   
    

def del_p():
    
    cur.execute(F"delete from patient where P_id='{DelP_ID.get()}'")
    con.commit()
        

def disp_p():


    cur.execute(F"Select * from patient where P_id='{DisP_ID.get()}'")
    con.commit()
    R=cur.fetchall()
    Record=Label(Disp_P_frame,text=F"{R[0]}",font=("Times New Roman",15))
    Record.place(x=120,y=100)
    
    
        
        
def moddocname():
    cur.execute(F"update patient set d_name='{Mod_Pdname.get()}' where P_id='{ModPDName_ID.get()}'")
    con.commit()

def modpname():
    cur.execute(F"update patient set p_name='{Mod_PName.get()}' where P_id='{ModPName_ID.get()}'")
    con.commit()

def moddoa():
    cur.execute(F"update patient set DOA='{Mod_Pdoa.get()}' where P_id='{ModPDOA_ID.get()}'")
    con.commit()

def modroa():
    cur.execute(F"update patient set reason_of_admission='{Mod_Proa.get()}' where P_id='{ModPROA_ID.get()}'")
    con.commit()

def modroomno():
    cur.execute(F"update patient set room_no='{Mod_Prno.get()}' where P_id='{ModPRNO_ID.get()}'")
    con.commit()


'''



DOCTOR TABLE



'''

def Add_d():
    global con
    N=0
    cur.execute("Select d_id from doctor")
    Rec=cur.fetchall()
    if len(Rec)!=0:
        for i in Rec:
            ID=i[0]+1
    
    else:
        ID=0
    cur.execute(F"insert into doctor values('{ID}','{Dname.get()}','{Age.get()}','{Field.get()}','{Position.get()}','{Salary.get()}')")
    con.commit()

def del_d():
    cur.execute(F"delete from doctor where D_id='{DelD_ID.get()}'")
    con.commit()

def disp_d():
    cur.execute(F"Select * from doctor where D_id='{DisD_ID.get()}'")
    con.commit()
    R=cur.fetchall()
    Record=Label(Disp_D_frame,text=F"{R[0]}",font=("Times New Roman",15))
    Record.place(x=120,y=100)



root.mainloop()
