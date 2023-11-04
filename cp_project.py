
import csv
from csv import writer
from tkinter import *
from tkinter import messagebox


#************************add question in spelling bee


def for_add_ques_in_speeling_bee():
    if add_sp.get()=="":
        messagebox.showwarning(" FAILED","   PLEASE TRY AGAIN.\n Field are Empty ")
    else:     
         add__1=add_sp.get()
         add__2=add__1.split(',')
         tup1=tuple(add__2)
         with open('spellingbee.csv', 'a',newline="") as csv2file:
            csvreader2 = csv.writer(csv2file)
            csvreader2.writerow(tup1)
            messagebox.showinfo( "SUCCESSFULLY " )
            csv2file.close()



##*********************add question in intelligence************

def add_ques_sp():
    global frame6
    
    global add2,add_sp
    frame5.destroy()
    frame6=Frame(root,bg="white")
    frame6.place(x=250,y=50,width=500,height=600)
    labeltext3=Label(frame6, 
     text="WELCOME" ,
     font="Broadway 40 bold italic ",
     fg='brown',
     bg="white").place(x=50,y=50)
   
   #l1 for usernaame
    add2=Label(frame6,
    text='Add Question:',
    bg="white",
    fg='brown')
    l=('Consolas',20)
    add2.config(font=l)
    add2.place(x=50,y=160)

   #e1 entry for username entry
    add_sp=Entry(frame6,
    width=80,
    border=0,
    bg="#d49562",
    fg='brown')
    l=('Consolas',20)
    add_sp.config(font=l)
    add_sp.place(x=50,y=260)

    #****************** BUTTON FOR ADD QUESTION***************
    _button5 = Button(frame6,
   text="Add Question",
   width=20,
   height=1,
   border=0,
   bg="white",
   fg='brown',
   activeforeground='brown',
   font=" Algerian 30 italic  ",
   activebackground="white",command=for_add_ques_in_speeling_bee).place(x=50,y=360)  


    labeltext4=Label(frame6,  text="Instruction:\nplease place (,)between question &\nintelligence_question and answer\nexample:\nChoose The Correct Spelling,\nJudgmental,Judgmentel,Judgmantal,Judgmaantal " ,font=" Consolas 10 ",fg='brown',bg="white").place(x=50,y=440)
             

#*************************FOR ADD QUESTION************************88
def add_ques():
    global frame5
    frame2.destroy()
    frame5=Frame(root,bg="white")
    frame5.place(x=250,y=50,width=400,height=500)
    Label(frame5,text="ADD\nQUESTION" ,
    font=" Algerian 40 bold italic ",
    fg='brown',
    bg="white").place(x=60,y=90) 
    label_1=Label(frame5,
    text="choice the domain" ,
    font=" Algerian 20 bold italic ",
    fg='brown',
    bg="white").place(x=60,y=220) 

    _button4 = Button(frame5,
    text="INTELLIGENCE",
    width=20,
    height=1,
    border=0,
    bg="white",
    fg='brown',
    activeforeground='brown',
    font="Algerian 30 italic  ",
    activebackground="white"
    ,command=add_ques_intelli).place(x=0,y=250)
    
    _button5 = Button(frame5,
   text="SPELLING \nBEE",
   width=20,
   height=1,
   border=0,
   bg="white",
   fg='brown',
   activeforeground='brown',
   font=" Algerian 30 italic  ",
   activebackground="white",command=add_ques_sp).place(x=0,y=350)  




#********************domain2 for intelligence*****************88
def domain2():
    root.destroy()
    root_1=Tk()
    root_1.geometry("900x800")
    img_1=PhotoImage(file="img_2.png")
    labelimage_1=Label(root_1,image=img_1).place(x=0,y=0 ,relheight=1,relwidth=1)
    global frame4
    frame4=Frame(root_1,bg="white")
    frame4.place(x=150,y=50,width=800,height=700)
    line1=0
    with open('intelligence.csv', 'r') as csv1file:
             csvreader1 = csv.reader(csv1file)
             for row in csvreader1:
                if line1== 0:
                       line1+= 1
                else:
                    Label(frame4,text=f"{row[0]}A.{row[1]}B.{row[2]}C.{row[3]}D.{row[4]}\n",
                    font="Calibri 12",
                    fg='brown',
                    bg="white").pack()
                line1+= 1
    root_1.mainloop()            
#*******************domain1 for spelling bee***********
line1=0

def domain1():
    root.destroy()
    root_2=Tk()
    root_2.geometry("900x800")
    img_2=PhotoImage(file="img_2.png")
    labelimage=Label(root_2,image=img_2).place(x=0,y=0 ,relheight=1,relwidth=1)
    global frame4
    frame4=Frame(root_2,bg="white")
    frame4.place(x=150,y=50,width=850,height=700)
    line1=0
    with open('spellingbee.csv', 'r') as csv1file:
             csvreader1 = csv.reader(csv1file)
             for row in csvreader1:
                if line1== 0:
                       line1+= 1
                else:
                    Label(frame4,text=f"{row[0]}A.{row[1]} B.{row[2]} C.{row[3]} D.{row[4]}\n",font="Calibri 12",fg='brown',bg="white").pack(pady=0)
                line1+= 1
    root_2.mainloop()            
#*******************display question*********************
def display_question():
    global frame3
    frame2.destroy()
    frame3=Frame(root,bg="white")
    frame3.place(x=250,y=50,width=400,height=500)
    Label(frame3,  text="DOMAIN!" ,
    font=" Algerian 40 bold italic ",
    fg='brown',
    bg="white").place(x=60,y=90) 

    _button4 = Button(frame3,
    text="INTELLIGENCE",
    width=20,
    height=1,
    border=0,
    bg="white",
    fg='brown',
    activeforeground='brown',
    font="Algerian 30 italic  ",
    activebackground="white",justify=CENTER,command=domain2).place(x=0,y=200)
    _button5 = Button(frame3,
   text="SPELLING \nBEE",
   width=20,
   height=1,
   border=0,
   bg="white",
   fg='brown',
   activeforeground='brown',
   font=" Algerian 30 italic  ",
   activebackground="white",command=domain1).place(x=0,y=310)  
#************************for add question in csv file 
def for_add_ques_in_intelli():
    if add_qi.get()=="":
        messagebox.showwarning(" FAILED","   PLEASE TRY AGAIN.\n Field are Empty ")
    else:     
         add_1=add_qi.get()
         add_2=add_1.split(',')
         tup1=tuple(add_2)
         with open('intelligence.csv', 'a',newline="") as csv2file:
            csvreader2 = csv.writer(csv2file)
            csvreader2.writerow(tup1)
            messagebox.showinfo( "SUCCESSFULLY " )
            csv2file.close()



##*********************add question in intelligence************
def add_ques_intelli():
    global frame6
    
    global add,add_qi
    frame5.destroy()
    frame6=Frame(root,bg="white")
    frame6.place(x=250,y=50,width=500,height=600)
    labeltext3=Label(frame6,
      text="WELCOME" ,
      font="Broadway 40 bold italic ",
      fg='brown',
      bg="white").place(x=50,y=50)
   
   #l1 for usernaame
    add=Label(frame6,text='Add Question:',
    bg="white",
    fg='brown')
    l=('Consolas',20)
    add.config(font=l)
    add.place(x=50,y=160)

   #e1 entry for username entry
    add_qi=Entry(frame6,
    width=80,
    border=0,
    bg="#d49562",
    fg='brown')
    l=('Consolas',20)
    add_qi.config(font=l)
    add_qi.place(x=50,y=260)

    #****************** BUTTON FOR ADD QUESTION***************
    _button5 = Button(frame6,
   text="Add Question",
   width=20,
   height=1,
   border=0,
   bg="white",
   fg='brown',
   activeforeground='brown',
   font=" Algerian 30 italic  ",
   activebackground="white",command=for_add_ques_in_intelli).place(x=50,y=360)  


    labeltext4=Label(frame6,  
    text="Instruction:\nplease place (,)between question &\nintelligence_question and answer\nexample:\nHow many hours are there in\n a year,8772,8020,8121,8000,8000 " ,
    font=" Consolas 10 ",
    fg='brown',
    bg="white").place(x=50,y=440)
   
  

#**********************show add question and display question*************
def display():
    global frame2
    frame1.destroy()
    frame2=Frame(root,bg="white")
    frame2.place(x=250,y=50,width=400,height=500)
    Label(frame2,
      text="WELCOME!" ,
      font=" Algerian 40 bold italic ",
      fg='brown',
      bg="white").place(x=60,y=90)  

    _button4 = Button(frame2,
    text="DISPLAY\n  QUESTION",
    width=20,
    height=1,
    border=0,
    bg="white",
    fg='brown',
    activeforeground='brown',
    font="Algerian 30 italic  ",
    activebackground="white",justify=CENTER,command=display_question).place(x=0,y=200)
    _button5 = Button(frame2,
   text="ADD\nQUESTION",
   width=20,
   height=1,
   border=0,
   bg="white",
   fg='brown',
   activeforeground='brown',
   font=" Algerian 30 italic  ",
   activebackground="white",command=add_ques).place(x=0,y=310)  

#******************for checking the user name and pasword is completely fill also both are correct***
def comp_fil():
    admin_name=admin_e1.get()
    admin_password=password_e1.get()
    if admin_e1.get()== "" and password_e1.get()=='':
        messagebox.showwarning(" FAILED","   PLEASE TRY AGAIN.\n Field are Empty ")
    else:
         if admin_name == "Usaid&Rafay" and admin_password=="1325":
             
            messagebox.showinfo(" SUCCESSFULLY  LOGGED IN ! ", "  WELCOME     ")
            display()
          
         else:
            messagebox.showwarning("Password or username entered is wrong")    
#***********************FOR ADMIN*****************
def admin():
   global admin_e1,password_e1,frame1
   frame.destroy()
   frame1=Frame(root,bg="white")
   frame1.place(x=250,y=50,width=400,height=500)
   labeltext3=Label(frame1,
     text="Login \n In" ,
     font="Broadway 60 bold italic ",
     fg='brown',
     bg="white").place(x=60,y=90)
   
   #l1 for usernaame
   user_l1=Label(frame1,
   text='USERNAME:',
   bg="white",
   fg='brown')
   l=('Consolas',20)
   user_l1.config(font=l)
   user_l1.place(x=50,y=260)

   #e1 entry for username entry
   admin_e1=Entry(frame1,
   width=20,
   border=0,
   bg="#d49562",
   fg='brown')
   l=('Consolas',20)
   admin_e1.config(font=l)
   admin_e1.place(x=50,y=300)

    #l2 for password
   password_l1=Label(frame1,
   text='PASSWORD:',
   bg="white",
   fg='brown')
   l=('Consolas',20)
   password_l1.config(font=l)
   password_l1.place(x=50,y=350)

   #password_e1 entry for password entry
   password_e1=Entry(frame1,
   width=20,
   border=0,
   show='*',
   bg="#d49562",
   fg='brown')
   password_e1.config(font=l)
   password_e1.place(x=50,y=390)

   #*******_button3 for check**
   _button3 = Button(frame1,
   text="login in ",
   width=20,
   height=1,
   border=0,
   bg="white",
   fg='brown',
   activeforeground='brown',
   font="Algerian 30 italic underline ",
   activebackground="white",command=comp_fil).place(x=50,y=430)
###########################################################################################################
# # _______________________________________SPELLING BEE____________________________________________________________-

#**********************display result*****************
def result_1(score_1):
    frame8.destroy()
    global frame9
    
    frame9=Frame(root,bg="white")
    frame9.place(x=250,y=50,width=400,height=500)
    labelresulT=Label( frame9,
    text="SCORE!" ,
    font=" Algerian 40 bold italic ",
    fg='brown',
    bg="white").place(x=60,y=90) 
    labelresulttext = Label(
        frame9,
        font=("Algerian 25 italic" ),
        fg='brown',
        bg="white"
    )
    labelresulttext.place(x=60,y=190)
    if score_1 >= 80:
        # #img = PhotoImage(file="quiz3.png"),
        # labelimage.configure(image=img)
        # labelimage.image=img
        labelresulttext.configure(text="You are excellent")
        Label(frame9,text=f"YOUR SCORE IS:\n{score_1}" ,
        font=" Algerian 30 bold italic ",
        fg='brown',
        bg="white").place(x=60,y=350) 
    elif 10 <= score_1 < 50:
        # img = PhotoImage(file="quiz4.png"),
        # labelimage.configure(image=img)
        # labelimage.image=img
        labelresulttext.configure(text="You can be better")
        Label(frame9,text=f"YOUR SCORE IS:\n{score_1}" ,
        font=" Algerian 30 bold italic ",
        fg='brown',
        bg="white").place(x=60,y=350) 
    else:
        # img = PhotoImage(file="quiz5.png"),
        # labelimage.configure(image=img)
        # labelimage.image = img
        labelresulttext.configure(text="You can be better")
        Label(frame9,text=f"YOUR SCORE IS:\n{score_1}" ,
        font=" Algerian 30 bold italic ",
        fg='brown',
        bg="white").place(x=60,y=350) 
        
#******************************display_question_of_intelligence
#calulate the score
def  calculate_sp():
    score_1=0
    global ans__2,ans_1
    app=[]
    user_answer_sp.pop(0)
    for i in range(1,11):
        app.append(spellingbee_question[i][5])

    ans_1 = map(int, app) 
    ans__2 = list(ans_1)
    for i in range(len(user_answer_sp)):  
      if user_answer_sp[i]==ans__2[i]:
         score_1=score_1+10 
    result_1(score_1) 

#**********8
user_answer_sp=[]
sp_ques=1
def selected_1():
    global radiovar, user_answer_sp,y,ans__2,ans_1
    global lblquestion_1, a1,a2,a3,a4
    global sp_ques
    app=[]
    y = radiovar.get()
    user_answer_sp.append(y)
    radiovar.set(-1)
    # print(x)
    
    if sp_ques <=10 :
        
        lblquestion_1.config(text=spellingbee_question[sp_ques][0])
        a1['text'] =spellingbee_question[sp_ques][1]
        a2['text'] =spellingbee_question[sp_ques][2]
        a3['text'] =spellingbee_question[sp_ques][3]
        a4['text'] =spellingbee_question[sp_ques][4]
        sp_ques += 1
    else:
        calculate_sp()  

    
    
def  spellingbee():
 global spellingbee_question,answer,frame8
 sp_from_csv = []
 with open('spellingbee.csv', 'r') as csvfile:
    csvreader1 = csv.reader(csvfile)
    for row in csvreader1:
       #print(row)
       sp_from_csv.append(row)
 spellingbee_question=sp_from_csv

 frame7.destroy()
 frame8=Frame(root,bg="white")
 frame8.place(x=250,y=50,width=400,height=500)
 global lblquestion_1, a1, a2, a3, a4
 lblquestion_1 = Label(frame8,text= spellingbee_question[1][0],
        font=("Consolas", 14),
        width=500,
        justify="center",
        wraplength=400,
        background="#ffffff",
        fg='brown'

    )
 lblquestion_1.pack(pady=(100, 30))

 global radiovar
 radiovar = IntVar()
 radiovar.set(-1)

 a1 = Radiobutton(
        frame8,
        text=spellingbee_question[1][1],
        font=("Times", 12),
        value=1,
        variable=radiovar,
        command=selected_1,
        background="#ffffff",
        fg='brown',
    )
 a1.pack(pady=5)

 a2 = Radiobutton(
        frame8,
        text=spellingbee_question[1][2],
        font=('Times', 12),
        value=2,
        variable=radiovar,
        command=selected_1,
        background="#ffffff",
        fg='brown'

    )
 a2.pack(pady=5)

 a3 = Radiobutton(
        frame8,
        text=spellingbee_question[1][3],
        font=('Times', 12),
        value=3,
        variable=radiovar,
        command=selected_1,
        background="#ffffff",
        fg='brown'

    )  
 a3.pack(pady=5)

 a4 = Radiobutton(
        frame8,
        text=spellingbee_question[1][4],
        font=('Times', 12),
        value=4,
        variable=radiovar,
        command=selected_1,
        background="#ffffff",
        fg='brown'


    )
 a4.pack(pady=5)
###########################################################################################################

#**********************display result*****************
def result(score):
    frame8.destroy()
    global frame9
    
    frame9=Frame(root,bg="white")
    frame9.place(x=250,y=50,width=400,height=500)
    labelresulT=Label( frame9,text="SCORE!" ,
    font=" Algerian 40 bold italic ",
    fg='brown',
    bg="white").place(x=60,y=90) 

    labelresulttext = Label(
        frame9,
        font=("Algerian 25 italic" ),
        fg='brown',
        bg="white"
    )
    labelresulttext.place(x=60,y=190)
    if score >= 80:
        # #img = PhotoImage(file="quiz3.png"),
        # labelimage.configure(image=img)
        # labelimage.image=img
        labelresulttext.configure(text="You are excellent")
        Label(frame9,
        text=f"YOUR SCORE IS:\n{score}" ,
        font=" Algerian 30 bold italic ",
        fg='brown',
        bg="white").place(x=60,y=350) 
    elif 30 <= score ==50:
        # img = PhotoImage(file="quiz4.png"),
        # labelimage.configure(image=img)
        # labelimage.image=img
        labelresulttext.configure(text="You are good")
        Label(frame9,text=f"YOUR SCORE IS:\n{score}" ,
        font=" Algerian 30 bold italic ",
        fg='brown',
        bg="white").place(x=60,y=350) 
    else:
        # img = PhotoImage(file="quiz5.png"),
        # labelimage.configure(image=img)
        # labelimage.image = img
        labelresulttext.configure(text="You can be better")
        Label(frame9,text=f"YOUR SCORE IS:\n{score}" ,
        font=" Algerian 30 bold italic ",
        fg='brown',
        bg="white").place(x=60,y=350) 
        
#******************************display_question_of_intelligence
#calulate the score
def  calculate():
    global ans__2,ans_1
    app=[]
    user_answer.pop(0)
    for i in range(1,11):
        app.append(intelligence_question[i][5])

    ans_1 = map(int, app) 
    ans__2 = list(ans_1)


    
    score=0
    
    for i in range(len(user_answer)):  
      if user_answer[i]==ans__2[i]:
         score=score+10
      #y=y+1

    result(score) 

#**********calucaltion___________
user_answer=[]
ques=1
def selected():
    global radiovar, user_answer,x,ans__2,ans_1
    global lblquestion, r1, r2, r3, r4
    global ques
    app=[]
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    # print(x)
    
    if ques <=10 :
        
        lblquestion.config(text=intelligence_question[ques][0])
        r1['text'] =intelligence_question[ques][1]
        r2['text'] =intelligence_question[ques][2]
        r3['text'] =intelligence_question[ques][3]
        r4['text'] =intelligence_question[ques][4]
        ques += 1
    else:
        calculate()  

    
    
def intelligence():
 global intelligence_question,answer,frame8
 lists_from_csv = []
 with open('intelligence.csv', 'r') as csvfile:
    csvreader1 = csv.reader(csvfile)
    for row in csvreader1:
       #print(row)
       lists_from_csv.append(row)
 intelligence_question=lists_from_csv

 frame7.destroy()
 frame8=Frame(root,bg="white")
 frame8.place(x=250,y=50,width=400,height=500)
 global lblquestion, r1, r2, r3, r4
 lblquestion = Label(frame8,text= intelligence_question[1][0],
        font=("Consolas 14"),
        width=500,
        justify="center",
        wraplength=400,
        background="#ffffff",
        fg='brown')
 lblquestion.pack(pady=(100, 30))

 global radiovar
 radiovar = IntVar()
 radiovar.set(-1)
 r1 = Radiobutton(
        frame8,
        text=intelligence_question[1][1],
        font=("Times", 12),
        value=1,
        variable=radiovar,
        command=selected,
        background="#ffffff",
        fg='brown',
    )
 r1.pack(pady=5)

 r2 = Radiobutton(
        frame8,
        text=intelligence_question[1][2],
        font=('Times', 12),
        value=2,
        variable=radiovar,
        command=selected,
        background="#ffffff",
        fg='brown'

    )
 r2.pack(pady=5)

 r3 = Radiobutton(
        frame8,
        text=intelligence_question[1][3],
        font=('Times', 12),
        value=3,
        variable=radiovar,
        command=selected,
        background="#ffffff",
        fg='brown'

    )  
 r3.pack(pady=5)

 r4 = Radiobutton(
        frame8,
        text=intelligence_question[1][4],
        font=('Times', 12),
        value=4,
        variable=radiovar,
        command=selected,
        background="#ffffff",
        fg='brown'


    )
 r4.pack(pady=5)


    
#**************************for player domain*************

def player_domain():
    global frame7
    frame.destroy()
    frame7=Frame(root,bg="white")
    frame7.place(x=250,y=50,width=400,height=500)
    Label(frame7,  text="DOMAIN!" ,
    font=" Algerian 40 bold italic ",
    fg='brown',
    bg="white").place(x=60,y=90)  
    _button4 = Button(frame7,
    text="INTELLIGENCE",
    width=20,
    height=1,
    border=0,
    bg="white",
    fg='brown',
    activeforeground='brown',
    font="Algerian 30 italic  ",
    activebackground="white",justify=CENTER,command=intelligence).place(x=0,y=200)
    _button5 = Button(frame7,
   text="SPELLING\nBEE",
   width=20,
   height=1,
   border=0,
   bg="white",
   fg='brown',
   activeforeground='brown',
   font=" Algerian 30 italic  ",
   activebackground="white",command=spellingbee).place(x=0,y=310)  


   


#**************************MAIN WINDOW******************************
root=Tk()
root.title("QUIZ GAME")
root.geometry("800x700")
root.resizable(False,False)
img=PhotoImage(file="img_1.png")
image=Label(root,image=img).place(x=0,y=0 ,relheight=1,relwidth=1)
frame=Frame(root,bg="white")
frame.place(x=250,y=50,width=400,height=500)
Label(frame,  text="QUIZ" ,
font="Algerian 60 bold",
fg='brown',
bg="white").place(x=30,y=50)
Label(frame,  text="GAME" ,
font="Algerian 60 bold",
fg='brown',
bg="white").place(x=60,y=145)

_button1 = Button(frame,
   text="PLAYER",
   width=20,
   height=1,
   border=0,
   bg="white",
   fg='brown',
   activeforeground='brown',
   font="Algerian 30 italic underline ",
   activebackground="white",command=player_domain).place(x=20,y=255)

_button2 = Button(frame,
   text="ADMIN",
   width=20,
   height=1,
   border=0,
   bg="white",
   fg='brown',
   activeforeground='brown',
   font=" Algerian 30 italic underline ",
   activebackground="white",command=admin).place(x=20,y=325)  

root.mainloop()
