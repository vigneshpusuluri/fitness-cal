
from tkinter import*
import random
import time
import datetime
import sqlite3


root=Tk()
root.geometry("1600x8000")
root.title("FITNESS REPORT")


Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

#=================================================================================
#                  TIME
#================================================================================
localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('helvetica',50,'bold'),text="FITNESS REPORT ",fg="Black",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)

db=sqlite3.connect('mydata123.db')
cur=db.cursor()
cur.execute("create table if not exists vignesh(ref char(20),bm int,bgroup char(3),age float,height float,weight float,name char(10))")
        
def datab(randomRef,B,CoBlood_group,CoAge,CoHeight,CoWeight,CoName):
    cur.execute("insert into vignesh values(?,?,?,?,?,?,?)",(randomRef,B,CoBlood_group,CoAge,CoHeight,CoWeight,CoName))
    db.commit()
def comp():
        root3=Tk()
        root3["bg"]="green"
        root3.minsize(700,600)
        root3.maxsize(700,600)
        Label(root3,text="RECORDS",font=("helvetica",30),bg='white').place(x=210,y=15)
        t=Text(root3,width=75,height=30)
        t.place(x=40,y=50)
        t.focus_set()
        cur.execute("select * from vignesh")
        lst=cur.fetchall()
        t.insert(END,"REFNO\tBMI\tBLOOD GROUP\tAGE\tHEIGHT\tWEIGHT\tNAME\n\n")
        t.place(x=40,y=60)
        loc=100
        i=0
        while(i<len(lst)):
            t.insert(END,"\n"+str(lst[i][0])+"\t"+str(lst[i][1])+"\t"+str(lst[i][2])+"\t"+str(lst[i][3])+"\t"+str(lst[i][4])+"\t"+str(lst[i][5])+"\t"+str(lst[i][6]))
            t.place(x=40,y=loc)
            loc+=30
            i+=1
       
            
    
def Ref():
    x=random.randint(10908,500876)
    randomRef=str(x)
    rand.set(randomRef)

    if (Blood_group.get()==""):
        CoBlood_group=0
    else:
        CoBlood_group=str(Blood_group.get())


    
    if (Age.get()==""):
        CoAge=0
    else:
        CoAge=float(Age.get())



    if (Height.get()==""):
        CoHeight=None
    else:
        CoHeight=float(Height.get())



    if (Weight.get()==""):
        CoWeight=None
    else:
        CoWeight=float(Weight.get())

        
    if (Sex.get()==""):
        CoSex=0
    else:
        CoSex=float(Sex.get())

     
    if (Name.get()==""):
        CoName=0
    else:
        CoName=str(Name.get())

    B =(CoWeight/(CoHeight)*(CoHeight))

    P= (B/6)
   

    BMI.set(B)
    Points.set(P)
    datab(randomRef,B,CoBlood_group,CoAge,CoHeight,CoWeight,CoName)

def page2():
        root.destroy()
        root1=Tk()
        Tops=Frame(root1, width=1600,relief=SUNKEN)
        Tops.pack(side=TOP)

        f1=Frame(root1,width=800,height=700,relief=SUNKEN)
        f1.pack(side=LEFT)





        lblInfo=Label(Tops,font=('helvetica',25,'bold'),text="DETAILED REPORT ",fg="black",bd=5,anchor='w')
        lblInfo.grid(row=0,column=0)


        def Ref2():
            x=random.randint(10908,500876)
            randomRef=str(x)
            rand.set(randomRef)

            if (Blood_group.get()==""):
                CoBlood_group=0
            else:
                CoBlood_group=str(Blood_group.get())


        
            if (Age.get()==""):
                CoAge=0
            else:
                CoAge=float(Age.get())



            if (Height.get()==""):
                CoHeight=None
            else:
                CoHeight=float(Height.get())



            if (Weight.get()==""):
                CoWeight=None
            else:
                CoWeight=float(Weight.get())

            
            if (Sex.get()==""):
                CoSex=0
            else:
                CoSex=str(Sex.get())

         
            if (Name.get()==""):
                CoName=0
            else:
                CoName=str(Name.get())



            if (BP.get()==""):
                CoBP=None
            else:
                CoBP=float(BP.get())


            if (PR.get()==""):
                CoPR=None
            else:
                CoPR=float(PR.get())

            if (RBC.get()==""):
                CoRBC=None
            else:
                CoRBC=float(RBC.get())

            if (WBC.get()==""):
                CoWBC=None
            else:
                CoWBC=float(WBC.get())

            if (Platelets.get()==""):
                CoPlatelets=None
            else:
                CoPlatelets=float(Platelets.get())

            if (UA.get()==""):
                CoUA=None
            else:
                CoUA=float(UA.get())

            B =(CoWeight/(CoHeight)*(CoHeight))

            P= (B/6)
            if (CoRBC>4.7 and CoWBC>4000 and CoPlatelets>3000):
                x="Healthy"

            else:
                x="Un Healthy"

            BMI.set(B)
            Points.set(P)
            Hel.set(x)
     
        
        def qExit():
            root1.destroy()
        
        def Info():
            rootin = Tk()
            L=Label(rootin, text="________________BMI________________")
            L.pack()

            L1=Label(rootin, text="BMI of less than 18.5")
            L1.pack()

            L3= Label(rootin, text="A BMI of less than 18.5 indicates that you are underweight, so you may need to put on some weight. You are recommended to ask your doctor or a dietitian for advice.")
            L3.pack()

            L4= Label(rootin, text="BMI of 18.5-24.9")
            L4.pack()

            L5= Label(rootin, text="A BMI of 18.5-24.9 indicates that you are at a healthy weight for your height. By maintaining a healthy weight, you lower your risk of developing serious health problems.")
            L5.pack()

            L6= Label(rootin, text="BMI of 25-29.9")
            L6.pack()

            L7= Label(rootin, text="A BMI of 25-29.9 indicates that you are slightly overweight. You may be advised to lose some weight for health reasons. You are recommended to talk to your doctor or a dietitian for advice.")
            L7.pack()

            L8= Label(rootin, text="BMI of over 30")
            L8.pack()

            L9= Label(rootin, text="A BMI of over 30 indicates that you are heavily overweight. Your health may be at risk if you do not lose weight. You are recommended to talk to your doctor or a dietitian for advice.")
            L9.pack()

            L10= Label(rootin, text="________________BLOOD PRESSURE________________")
            L10.pack()

            L24= Label(rootin, text="The normal blood pressure is 80 - 120 mm Hg")
            L24.pack()

            L11= Label(rootin, text="Incase of high blood pressure, you are suggested to reduce the intake of sodium, caffine and alcohol. Exercie regularly and maintain a healthy diet.")
            L11.pack()

            L12= Label(rootin, text="Incase of low blood pressure, you are suggested to eat more salt, drink more water,avoid alcohol and have lots of non-alcoholic fluids. Get regular exercise to promote blood flow.")
            L12.pack()

            L13= Label(rootin, text="________________PULSE RATE________________")
            L13.pack()

            L14= Label(rootin, text="For adults 18 and older, a normal resting heart rate is between 60 and 100 beats per minute(BPM).For children ages 6 to 15, the normal resting heart rate is between 70 and 100 bpm.")
            L14.pack()

            L15= Label(rootin, text="________________URIC ACID________________")
            L15.pack()

            L25=Label(rootin,text=" Normal Uric acid levels are 2.4-6.0 mg/dL (female) and 3.4-7.0 mg/dL (male)")
            L25.pack()

            L16= Label(rootin, text="To reduce the uric acid levels in blood, you may need to limit intake of alcohol, sugary foods and reduce purine rich foods like meat, poultry, seafood and pulses and vegetables like cauliflower, spinach, peas and mushroom")
            L16.pack()

            L17= Label(rootin, text="Incase of love uric acid levels, you are suggested to increase the intake of food rich in purine as mentioned above, have low fat milk and diary products daily.")
            L17.pack()

            L18= Label(rootin, text="________________RBC COUNT________________")
            L18.pack()

            L25=Label(rootin,text=" Normal RBC count for - Male: 4.7 to 6.1 million cells per microliter (cells/mcL) Female: 4.2 to 5.4 million cells/mcL.")
            L25.pack()

            L19= Label(rootin, text="To increase the count of RBC, eat iron-rich food, increase vitamin-C and folic acid intake. Avoid iron blockers and exercise.")
            L19.pack()

            L20= Label(rootin, text="To reduce RBC count, always keep yourself hydrated, quit smoking. Also try to avoid iron supplementation.")
            L20.pack()

            L21= Label(rootin, text="________________WBC COUNT________________")
            L21.pack()

            L24= Label(rootin, text="The normal number of WBCs in the blood is 4,500 to 11,000 WBC per microliter")
            L24.pack()

            L22= Label(rootin, text="To increase the count of WBC, eat more ctrus fruits, broccoli, garlic, ginger, spinach, yogurt, almonds")
            L22.pack()

            L23= Label(rootin, text="To reduce WBC count, include vitamin-C, fatty acids and antioxidants in your diet. Avoid food rich in sugar, salt and fats.")
            L23.pack()

            L26=Label(rootin,text="________________CHOLESTEROL________________")
            L26.pack()

            L27=Label(rootin,text="A desirable total cholesterol level for adults without heart disease is less than 200 mg/dL.")
            L27.pack()

            L28=Label(rootin,text="Incase of high cholesterol levels, reduce the intake of saturated fats, eliminate trans fat, add protien and food containing omega-3 fatty acids to your diet")
            L28.pack()

            L29=Label(rootin,text="Incase of low cholesterol levels,eat saturated food found in animal products and trans fats present in cookies and have food high in cholesterol like meat and full-dairy products.")
            L29.pack()


            def close(): 
                rootin.destroy()

           
            L31=Button(rootin,text = "EXIT",command=close,bg="RED")
            L31.pack()




        def Reset():
            rand.set("") 
            Blood_group.set("")
            Age.set("")
            Height.set("")
            Points.set("")
            BMI.set("")
            Weight.set("")
            BP.set("")
            PR.set("")
            RBC.set("")
            WBC.set("")
            Platelets.set("")
            UA.set("")
            Sex.set("")
            Name.set("")
            Hel.set("")
        
        rand = StringVar()
        Blood_group=StringVar()
        Age=StringVar()
        Height=IntVar()
        Points=IntVar()
        BMI=IntVar()
        Weight=IntVar()
        Sex=StringVar()
        Name=StringVar()
        BP=IntVar()
        PR=IntVar()
        RBC=IntVar()
        WBC=IntVar()
        Platelets=IntVar()
        UA=IntVar()
        Hel=StringVar()



        lblReference= Label(f1, font=('arial', 16, 'bold'),text="Reference",bd=16,anchor="w")
        lblReference.grid(row=0, column=0)
        txtReference=Entry(f1, font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify='right')
        txtReference.grid(row=0,column=1)

        lblName= Label(f1, font=('arial', 16, 'bold'),text="Name",bd=16,anchor="w")
        lblName.grid(row=1, column=0)
        txtName=Entry(f1, font=('arial',16,'bold'),textvariable=Name,bd=10,insertwidth=4,bg="powder blue",justify='right')
        txtName.grid(row=1,column=1)


        lblAge= Label(f1, font=('arial', 16, 'bold'),text="Age",bd=16,anchor="w")
        lblAge.grid(row=2, column=0)
        txtAge=Entry(f1, font=('arial',16,'bold'),textvariable=Age,bd=10,insertwidth=4,bg="powder blue",justify='right')
        txtAge.grid(row=2,column=1)


        lblSex= Label(f1, font=('arial', 16, 'bold'),text="Sex",bd=16,anchor="w")
        lblSex.grid(row=3, column=0)
        txtSex=Entry(f1, font=('arial',16,'bold'),textvariable=Sex,bd=10,insertwidth=4,bg="powder blue",justify='right')
        txtSex.grid(row=3,column=1)

        lblBlood_group= Label(f1, font=('arial', 16, 'bold'),text="Blood group",bd=16,anchor="w")
        lblBlood_group.grid(row=0, column=4)
        txtBlood_group=Entry(f1, font=('arial',16,'bold'),textvariable=Blood_group,bd=10,insertwidth=4,bg="powder blue",justify='right')
        txtBlood_group.grid(row=0,column=5)

        lblHeight= Label(f1, font=('arial', 16, 'bold'),text="Height",bd=16,anchor="w")
        lblHeight.grid(row=4, column=0)
        txtHeight=Entry(f1, font=('arial',16,'bold'),textvariable=Height,bd=10,insertwidth=4,bg="powder blue",justify='right')
        txtHeight.grid(row=4,column=1)

        lblWeight= Label(f1, font=('arial', 16, 'bold'),text="Weight",bd=16,anchor="w")
        lblWeight.grid(row=5, column=0)
        txtWeight=Entry(f1, font=('arial',16,'bold'),textvariable=Weight,bd=10,insertwidth=4,bg="powder blue",justify='right')
        txtWeight.grid(row=5,column=1)

        lblBP= Label(f1, font=('arial', 16, 'bold'),text="Blood Pressure",bd=16,anchor="w")
        lblBP.grid(row=1, column=4)
        txtBP=Entry(f1, font=('arial',16,'bold'),textvariable=BP,bd=10,insertwidth=4,bg="powder blue",justify='right')
        txtBP.grid(row=1,column=5)

        lblPR= Label(f1, font=('arial', 16, 'bold'),text="Pulse Rate",bd=16,anchor="w")
        lblPR.grid(row=2, column=4)
        txtPR=Entry(f1, font=('arial',16,'bold'),textvariable=PR,bd=10,insertwidth=4,bg="powder blue",justify='right')
        txtPR.grid(row=2,column=5)

        lblRBC= Label(f1, font=('arial', 16, 'bold'),text="RBC Count",bd=16,anchor="w")
        lblRBC.grid(row=3, column=4)
        txtRBC=Entry(f1, font=('arial',16,'bold'),textvariable=RBC,bd=10,insertwidth=4,bg="powder blue",justify='right')
        txtRBC.grid(row=3,column=5)

        lblWBC= Label(f1, font=('arial', 16, 'bold'),text="WBC Count",bd=16,anchor="w")
        lblWBC.grid(row=4, column=4)
        txtWBC=Entry(f1, font=('arial',16,'bold'),textvariable=WBC,bd=10,insertwidth=4,bg="powder blue",justify='right')
        txtWBC.grid(row=4,column=5)


        lblPlatelets= Label(f1, font=('arial', 16, 'bold'),text="Platelets Count",bd=16,anchor="w")
        lblPlatelets.grid(row=5, column=4)
        txtPlatelets=Entry(f1, font=('arial',16,'bold'),textvariable=Platelets,bd=10,insertwidth=4,bg="powder blue",justify='right')
        txtPlatelets.grid(row=5,column=5)

        lblUA= Label(f1, font=('arial', 16, 'bold'),text="Uric Acid",bd=16,anchor="w")
        lblUA.grid(row=6, column=0)
        txtUA=Entry(f1, font=('arial',16,'bold'),textvariable=UA,bd=10,insertwidth=4,bg="powder blue",justify='right')
        txtUA.grid(row=6,column=1)

        lblSubBMI= Label(f1, font=('arial', 16, 'bold'),text="Healthy",bd=16,anchor="w")
        lblSubBMI.grid(row=3, column=2)
        txtSubBMI=Entry(f1, font=('arial',16,'bold'),textvariable=Hel,bd=10,insertwidth=4,bg="powder blue",justify='right')
        txtSubBMI.grid(row=3,column=3)



        lblSubBMI= Label(f1, font=('arial', 16, 'bold'),text="Points",bd=16,anchor="w")
        lblSubBMI.grid(row=4, column=2)
        txtSubBMI=Entry(f1, font=('arial',16,'bold'),textvariable=Points,bd=10,insertwidth=4,bg="powder blue",justify='right')
        txtSubBMI.grid(row=4,column=3)

        lblBMICost= Label(f1, font=('arial', 16, 'bold'),text="BMI",bd=16,anchor="w")
        lblBMICost.grid(row=5, column=2)
        txtBMICost=Entry(f1, font=('arial',16,'bold'),textvariable=BMI,bd=10,insertwidth=4,bg="powder blue",justify='right')
        txtBMICost.grid(row=5,column=3)


        btnBMI=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="RESULT",bg="powder blue",command=Ref2).grid(row=7,column=1)

        btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="RESET",bg="powder blue",command=Reset).grid(row=7,column=2)

        btnINFO=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="MORE INFO",bg="powder blue",command=Info).grid(row=7,column=3)
        
        btnEXIT=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="EXIT",bg="powder blue",command=qExit).grid(row=7,column=4)
        #btnCOMP=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="HALTHY",bg="powder blue",command=p).grid(row=7,column=4)

def qExit():
    root.destroy()

def Reset():
    rand.set("") 
    Blood_group.set("")
    Age.set("")
    Height.set("")
    Points.set("")
    BMI.set("")
    Weight.set("")
    Name.set("")
    

rand = StringVar()
Blood_group=StringVar()
Age=StringVar()
Height=IntVar()
Points=IntVar()
BMI=IntVar()
Weight=IntVar()
Sex=StringVar()
Name=StringVar()
v=IntVar()


lblReference= Label(f1, font=('arial', 16, 'bold'),text="Reference",bd=16,anchor="w")
lblReference.grid(row=0, column=0)
txtReference=Entry(f1, font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtReference.grid(row=0,column=1)

lblName= Label(f1, font=('arial', 16, 'bold'),text="Name",bd=16,anchor="w")
lblName.grid(row=1, column=0)
txtName=Entry(f1, font=('arial',16,'bold'),textvariable=Name,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtName.grid(row=1,column=1)


lblAge= Label(f1, font=('arial', 16, 'bold'),text="Age",bd=16,anchor="w")
lblAge.grid(row=2, column=0)
txtAge=Entry(f1, font=('arial',16,'bold'),textvariable=Age,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtAge.grid(row=2,column=1)


lblSex= Label(f1, font=('arial', 16, 'bold'),text="Sex",bd=16,anchor="w")
lblSex.grid(row=3, column=0)
txtSex=Radiobutton(f1,font=('arial', 16, 'bold'), text="Male", variable=v, value=1)
txtSex.grid(row=3,column=1)
txtSex=Radiobutton(f1,font=('arial', 16, 'bold'), text="Female", variable=v, value=2)
txtSex.grid(row=4,column=1)


lblBlood_group= Label(f1, font=('arial', 16, 'bold'),text="Blood group",bd=16,anchor="w")
lblBlood_group.grid(row=5, column=0)
txtBlood_group=Entry(f1, font=('arial',16,'bold'),textvariable=Blood_group,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtBlood_group.grid(row=5,column=1)

lblHeight= Label(f1, font=('arial', 16, 'bold'),text="Height",bd=16,anchor="w")
lblHeight.grid(row=1, column=4)
txtHeight=Entry(f1, font=('arial',16,'bold'),textvariable=Height,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtHeight.grid(row=1,column=5)

lblWeight= Label(f1, font=('arial', 16, 'bold'),text="Weight",bd=16,anchor="w")
lblWeight.grid(row=0, column=4)
txtWeight=Entry(f1, font=('arial',16,'bold'),textvariable=Weight,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtWeight.grid(row=0,column=5)


lblSubBMI= Label(f1, font=('arial', 16, 'bold'),text="Points",bd=16,anchor="w")
lblSubBMI.grid(row=4, column=4)
txtSubBMI=Entry(f1, font=('arial',16,'bold'),textvariable=Points,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSubBMI.grid(row=4,column=5)

lblBMICost= Label(f1, font=('arial', 16, 'bold'),text="BMI",bd=16,anchor="w")
lblBMICost.grid(row=5, column=4)
txtBMICost=Entry(f1, font=('arial',16,'bold'),textvariable=BMI,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtBMICost.grid(row=5,column=5)

#==========================================Buttons==========================================================================================
btnBMI=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="BMI",bg="powder blue",command=Ref).grid(row=7,column=1)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="powder blue",command=Reset).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="powder blue",command=qExit).grid(row=7,column=3)

btnpage2=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="COUSTMISED",bg="powder blue",command=page2).grid(row=7,column=4)


btnpage2=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="COMPARE",bg="powder blue",command=comp).grid(row=7,column=5)


root.mainloop()


