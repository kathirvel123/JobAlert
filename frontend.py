
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import backend

root =tk.Tk()
root.geometry('1000x600')
root.title('JOB-ALERT')
root.resizable(False,False)
#=======================================================Images=========================================================================
img1 = PhotoImage(file='login.png')
img2 = PhotoImage(file='uiux-design.png')
img3=PhotoImage(file='ui (2).png')
img4=PhotoImage(file='verification-removebg-preview.png')
roundentry=PhotoImage(file='verification-removebg-preview.png') 
img5=PhotoImage(file='BeFunky-design.png')
img6=PhotoImage(file='NEW ONE.png')
background=PhotoImage(file='EMPLOYEE001.png')
img9=PhotoImage(file='employer.png')
img10=PhotoImage(file='email_verifier.png')
img7=PhotoImage(file='password profile png.png')
img8=PhotoImage(file='usernameid show.png')
img11=PhotoImage(file='mail get.png')
swn=PhotoImage(file='something went.png')
img12=PhotoImage(file='forgot_password_page1.png')
#========================================================x===========================================================================
def stw():
    fp=Label(root,bg='white',image=swn)
    fp.place(x=0,y=0)
def sign_inpage():
    window=Label(root,bg='white',height=600,width=1000).place(x=0,y=0)
    Label(window,image=img1,bg='white').place(x=40,y=110)
    def sign_in():
        username=user.get()
        password=user1.get()
        if username in ['Username',''] or password in ['Password','']:
            Frame(frame,width=390,height=2,bg='red').place(x=30,y=130)
            Frame(frame,width=390,height=2,bg='red').place(x=30,y=210)
            messagebox.showerror(f'error','fill it properly')
           
        else:
            res=backend.sign_in_db(username,password)
            if res=='employer':
                root.destroy()
                employee_120(username)
            elif res=='employee':
                root.destroy()
                employer_120(username)
            elif res=='invalid password':
                Frame(frame,width=390,height=2,bg='red').place(x=30,y=210)
                messagebox.showerror(f'WRONG PASSWORD','ERROR')
            elif res== 'user name not found':
                Frame(frame,width=390,height=2,bg='red').place(x=30,y=130)
                Frame(frame,width=390,height=2,bg='red').place(x=30,y=210)
                messagebox.showerror(f'user name','user name not found')


    frame=Frame(window,width=450,height=500,bg='white')
    frame.place(x=480,y=70)

    heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI light',30,'bold'))
    heading.place(x=150,y=5)
    #------------------------------------------------------------------------------------------------------------------------------
    def on_entry(e):
        name1=user.get()
        if name1=='Username':
            user.delete(0,END)
    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')
        else:
            Frame(frame,width=390,height=2,bg='black').place(x=30,y=130)


    user = Entry(frame,width=35,fg='black',border=0,bg='white',font=('Microsoft YaHei UI light',15))
    user.place(x=30,y=100)
    user.insert(0,'Username')
    user.bind('<FocusIn>',on_entry)
    user.bind('<FocusOut>',on_leave)
    Frame(frame,width=390,height=2,bg='black').place(x=30,y=130)

#----------------------------------------------------------------------------------------------
    def on_entry(e):
        name1=user1.get()
        #Frame(frame,width=390,height=3,bg='red').place(x=30,y=130)
        if name1=='Password':
            user1.delete(0,END)
    def on_leave(e):
        name=user1.get()
        if name=='':
            user1.insert(0,'Password')
        else:
            Frame(frame,width=390,height=2,bg='black').place(x=30,y=210)
    user1 = Entry(frame,width=35,fg='black',border=0,bg='white',font=('Microsoft YaHei UI light',15))
    user1.place(x=30,y=180)
    user1.insert(0,'Password')
    user1.bind('<FocusIn>', on_entry)
    user1.bind('<FocusOut>', on_leave)
    Frame(frame,width=390,height=2,bg='black').place(x=30,y=210)


    ####################################################################
    Button(frame,width=49,pady=10,text='Sign in',bg='#57a1f8',fg='white',border=0,command=sign_in).place(x=40,y=259)
    label0=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI light',10,'bold'))
    label0.place(x=75,y=320)
    Button(frame,text='sign up',border=0,bg='white',fg='#57a1f8',font=('Microsoft YaHei UI light',8,'bold'),cursor='hand2',command=sign_up).place(x=250,y=321)
    Button(frame,text='Forgot Password?',border=0,bg='white',fg='#57a1f8',font=('Microsoft YaHei UI light',10,'bold'),cursor='hand2',command=forgatpass).place(x=130,y=345)
'''--------------------------------------------------------------------------------------------------------------'''
def change_pass(po):
    def next1_od():
        if len(np.get())>=8:
            if np.get()==cp.get():
                backend.update_pass(po,np.get())
                sign_inpage()
            else:
                Frame(f1,bg='red',width=360,height=2).place(x=35,y=305)
        else:
            Frame(f1,bg='red',width=360,height=2).place(x=35,y=185)
    w7=Label(root,height=600,width=1000,bg='white')
    w7.place(x=0,y=0)
    Label(w7,image=img7,bg='white').place(x=50,y=50)
    f1=Frame(w7,bg='white',height=530,width=430)
    f1.place(x=530,y=40)
    Label(f1,bg='white',fg='#57a1f8',font=('Microsoft YaHei UI light',30,'bold'),text='New password').place(x=50,y=30)
    np=Entry(f1,bg='white',fg='black',width=21,font=('Segoe UI',23),border=0)
    np.place(x=35,y=140)
    Frame(f1,bg='black',width=360,height=2).place(x=35,y=185)
    cp=Entry(f1,bg='white',fg='black',width=21,font=('Segoe UI',23),border=0)
    cp.place(x=35,y=260)
    Frame(f1,bg='black',width=360,height=2).place(x=35,y=305)
    Button(f1,bg='#57a1f8',fg='white',font=('Segoe UI',15),border=0,text='Next',width=20,command=next1_od).place(x=100,y=380)
    def on_entry1(e):
        if np.get() == 'Password':
            np.delete(0,'end')
    def on_leave1(e):
        if np.get()=='':
            np.insert(0,'Password')

    def on_entry(e):
        if cp.get() == 'Confirm Password':
            cp.delete(0,'end')
    def on_leave(e):
        if cp.get()=='':
            cp.insert(0,'Confirm Password')
    np.insert(0,'Password')
    cp.insert(0,'Confirm Password')
    cp.bind('<FocusIn>',on_entry)
    cp.bind('<FocusOut>',on_leave)
    np.bind('<FocusIn>',on_entry1)
    np.bind('<FocusOut>',on_leave1)
def forgatpass():
    k=[]
    def changepass():
        if int(user1.get()) in k:
            change_pass(user.get())
        else:
            Frame(w9,height=2,width=340,bg='red').place(x=590,y=322)
    def backgo():
        sign_inpage()
    def on_entry1(e):
        a=user.get()
        if a=='USER NAME':
            user.delete(0,'end')
    def on_leave1(e):
        a=user.get()
        if a=='':
            user.insert(0,'USER NAME')
        else:
            m=backend.forgat_pass(a)
            if m:
                p='Your no'+m[0]+'*****'+m[8]+m[9]
                o=Label(w9,text=p,bg='white',fg='black',font=('Microsoft YaHei UI light',18))
                o.place(x=590,y=240)
                k.append(backend.send_now(m))
    w9=Label(root,image=img12,height=600,width=1000,bg='black')
    w9.place(x=0,y=0)
    user=Entry(w9,width=16,fg='black',border=0,bg='white',font=('Microsoft YaHei UI light',28))
    user.place(x=590,y=170)
    Frame(w9,height=2,width=340,bg='black').place(x=590,y=214)
    user1=Entry(w9,width=16,fg='black',border=0,bg='white',font=('Microsoft YaHei UI light',28))
    user1.place(x=590,y=280)
    Frame(w9,height=2,width=340,bg='black').place(x=590,y=322)
    user.insert(0,'USER NAME')
    Button(w9,text='Next',bg='#57a1f8',fg='white',border=0,font=('Microsoft YaHei UI light',21,'bold'),width=8,activebackground='white',command=changepass).place(x=790,y=370)
    Button(w9,text='Back',bg='#57a1f8',fg='white',border=0,font=('Microsoft YaHei UI light',21,'bold'),width=8,activebackground='white',command=backgo).place(x=590,y=370)

    user.bind('<FocusIn>',on_entry1)
    user.bind('<FocusOut>',on_leave1)


    
'''-----------------------------------------------------------------------------------------------------------------'''
def sign_up():
    window1=Label(root,bg='white',height=600,width=1000).place(x=0,y=0)
    Label(window1,image=img2,bg='white').place(x=0,y=20)
    frame=Frame(window1,width=400,height=520,bg='white')
    frame.place(x=580,y=50)
    heading=Label(frame,text='Sign up',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI light',30,'bold'))
    heading.place(x=125,y=5)
    #------------------------------------------------------------------------------------------------
    def on_entry1(e):
        name1=user.get()
        if name1=='Your name':
            user.delete(0,'end')
    def on_leave1(e):
        name=user.get()
        if name=='':
            user.insert(0,'Your name')
            return False
        elif name.isalpha():
            Frame(frame,width=341,height=2,bg='black').place(x=30,y=140)
            return True
        else:
            Frame(frame,width=341,height=2,bg='red').place(x=30,y=140)
            return False

                
    user = Entry(frame,width=31,fg='black',border=0,bg='white',font=('Microsoft YaHei UI light',15))
    user.place(x=30,y=110)
    user.insert(0,'Your name')
    user.bind('<FocusIn>',on_entry1)
    user.bind('<FocusOut>',on_leave1)
    Frame(frame,width=341,height=2,bg='black').place(x=30,y=140)

#==================================================================================================================
    def on_entry2(e):
        name1=mm.get()
        if name1=='   MM':
            mm.delete(0,'end')
    def on_leave2(e):
        name=mm.get()
        if name=='':
            mm.insert(0,'   MM')
            return False
        elif len(name)<=2 and len(name)>=1 and name.isdigit() and int(name) in [1,2,3,4,5,6,7,8,9,10,11,12]:
            Frame(frame,width=79,height=2,bg='black').place(x=30,y=200)
            return True
                
        else:
            Frame(frame,width=79,height=2,bg='red').place(x=30,y=200)
            return False

    
    #age
    mm=Entry(frame,width=7,fg='black',border=0,bg='white',font=('Microsoft YaHei UI light',15))
    mm.place(x=30,y=170)
    mm.insert(0,'   MM')
    mm.bind('<FocusIn>',on_entry2)
    mm.bind('<FocusOut>',on_leave2)
    Frame(frame,width=79,height=2,bg='black').place(x=30,y=200)
    #----------------------------------------------------------------------------------------------------------------------------------------------------------
    def on_entry3(e):
        name1=dd.get()
        if name1=='    DD':
            dd.delete(0,'end')
    def on_leave3(e):
        name=dd.get()
        if name=='':
            dd.insert(0,'    DD')
            return False
        if len(name)<=2 and len(name)>=1 and name.isdigit():
            n1=mm.get()
            if int(n1)==2:
                if int(name)>=1 and int(name)<=29:
                    Frame(frame,width=79,height=2,bg='black').place(x=150,y=200)
                    return True
                else:
                    Frame(frame,width=79,height=2,bg='red').place(x=150,y=200)
                    return False
                    
            elif int(n1) in [1,3,5,7,8,10,12]:
                if int(name)>=1 and int(name)<=31:
                    Frame(frame,width=79,height=2,bg='black').place(x=150,y=200)
                    return True
                else:
                    Frame(frame,width=79,height=2,bg='red').place(x=150,y=200)
                    return False
            elif int(n1) in [4,6,9,11]:
                if int(name)>=1 and int(name)<=30:
                    Frame(frame,width=79,height=2,bg='black').place(x=150,y=200)
                    return True
                else:
                    Frame(frame,width=79,height=2,bg='red').place(x=150,y=200)
                    return False
        else:
            Frame(frame,width=79,height=2,bg='red').place(x=150,y=200)
            return False

    dd=Entry(frame,width=7,fg='black',border=0,bg='white',font=('Microsoft YaHei UI light',15))
    dd.place(x=150,y=170)
    dd.insert(0,'    DD')
    dd.bind('<FocusIn>',on_entry3)
    dd.bind('<FocusOut>',on_leave3)
    Frame(frame,width=79,height=2,bg='black').place(x=150,y=200)
    #---------------------------------------------------------------------------------------------------------------------------------------------
    def on_entry4(e):
        name1=yy.get()
        if name1=='  YYYY':
            yy.delete(0,'end')
    def on_leave4(e):
        name=yy.get()
        if name=='':
            yy.insert(0,'  YYYY')
            return False
        if len(name)==4 and name.isdigit():
            Frame(frame,width=79,height=2,bg='black').place(x=270,y=200)
            return True
        else:
            Frame(frame,width=79,height=2,bg='red').place(x=270,y=200)
            return False
    yy=Entry(frame,width=7,fg='black',border=0,bg='white',font=('Microsoft YaHei UI light',15))
    yy.place(x=270,y=170)
    yy.insert(0,'  YYYY')
    yy.bind('<FocusIn>',on_entry4)
    yy.bind('<FocusOut>',on_leave4)
    Frame(frame,width=79,height=2,bg='black').place(x=270,y=200)
    #------------------------------------------------------------------------------------------------------------------------------------------
    def on_entry5(e):
        name1=gender.get()
        name1=name1.rstrip()
        name1=name1.lstrip()
        if name1=='Male or Female':
            gender.delete(0,'end')
    def on_leave5(e):
        name=gender.get()
        if name=='':
            gender.insert(0,'Male or Female')
        elif name.lower() in ['male','female']:
             Frame(frame,width=341,height=2,bg='black').place(x=30,y=276)
             return True
        else:
             Frame(frame,width=341,height=2,bg='red').place(x=30,y=276)
             return False
    gender=Entry(frame,width=31,bg='white',border=0,font=('Microsoft YaHei UI light',14))
    gender.place(x=30,y=250)
    gender.insert(0,'Male or Female')
    gender.bind('<FocusIn>',on_entry5)
    gender.bind('<FocusOut>',on_leave5)
    Frame(frame,width=341,height=2,bg='black').place(x=30,y=276)
    #=====================================================================================================================================================
    def on_entry6(e):
        name1=phonenumber.get()
        if name1=='Phone number':
            phonenumber.delete(0,'end')
    def on_leave6(e):
        name=phonenumber.get()
        if name=='':
            phonenumber.insert(0,'Phone number')
        elif name.isdigit() and len(name)==10:
            Frame(frame,width=341,height=2,bg='black').place(x=30,y=338)
            return True
        else:
            Frame(frame,width=341,height=2,bg='red').place(x=30,y=338)
            return False

    phonenumber=Entry(frame,width=31,bg='white',border=0,font=('Microsoft YaHei UI light',14))
    phonenumber.place(x=30,y=310)
    phonenumber.insert(0,'Phone number')
    phonenumber.bind('<FocusIn>',on_entry6)
    phonenumber.bind('<FocusOut>',on_leave6)
    Frame(frame,width=341,height=2,bg='black').place(x=30,y=338)

    def check_next():
        if on_leave1(1):
            if on_leave2(2):
                if on_leave3(3):
                    if on_leave4(4):
                        if on_leave5(5):
                            if on_leave6(6):
                                backend.md_append(user.get())
                                backend.md_append(dd.get()+'/'+mm.get()+'/'+yy.get())
                                backend.md_append(gender.get())
                                backend.md_append(phonenumber.get())
                                otp_verification(phonenumber.get())
    Button(frame,text='Back',border=0,bg='#57a1f8',fg='white',width=10,command=sign_inpage,font=('Microsoft YaHei UI light',11),cursor='hand2').place(x=30,y=410)
    Button(frame,text='Next',border=0,bg='#57a1f8',fg='white',width=10,font=('Microsoft YaHei UI light',11),cursor='hand2',command=check_next).place(x=269,y=410)
   

def otp_verification(n):
    otp_this=backend.send_now(n)
    if otp_this==False:
        backend.maindata.clear()
        stw()
    else:
        def verify_otp():
            if on_leave(0):
                a=otp.get()
                if int(a)==otp_this:
                    backend.md_append('')
                    welcome()


        window2=Label(root,bg='white',height=600,width=1000).place(x=0,y=0)
        Label(window2,image=img4,bg='white').place(x=10,y=70)
        frame=Frame(window2,width=400,height=520,bg='white')
        frame.place(x=550,y=50)
        heading=Label(frame,text='OTP verification',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI light',30,'bold'))
        heading.place(x=40,y=5)
        Label(frame,text='Verify your',fg='black',bg='white',font=('Century',20,'bold')).place(x=115,y=70)
        Label(frame,text='Phone number',fg='black',bg='white',font=('Century',20,'bold')).place(x=95,y=110)
        def on_leave(e):
            a=otp.get()
            if a.isdigit() and len(a)==6:
                Frame(frame,height=2,width=290,bg='black',border=0).place(x=61,y=237)
                return True
            else:
                Frame(frame,height=2,width=290,bg='red',border=0).place(x=61,y=237)
                return False
        def resend_otp():
            otp_verification(n)

        Label(frame,text='Enter your OTP code here',fg='black',bg='white',font=('Segoe UI',11,),border=0).place(x=115,y=152)
        otp=Entry(frame,width=22,bg='white',border=0,font=('Segoe UI',19,))
        otp.place(x=61,y=199)
        otp.bind('<FocusOut>',on_leave)
        Frame(frame,height=2,width=290,bg='black',border=0).place(x=61,y=237)
        Label(frame,text='Didn,t receive the OTP?',fg='black',bg='white',font=('Segoe UI',10,),border=0).place(x=75,y=250)
        Button(frame,text='RESEND OTP',bg='white',fg='#57a1f8',border=0,font=('Segoe UI',10,'bold'),cursor='hand2',command=resend_otp).place(x=220,y=249)
        Button(frame,text='Verify',font=('Microsoft YaHei UI light',19),bg='#57a1f8',fg='white',cursor='hand2',border=0,width=20,command=verify_otp).place(x=50,y=310)


def welcome():
    def employee():
        backend.md_pop()
        backend.md_append('employee')
        employee_page()
    def employer():
        backend.md_pop()
        backend.md_append('employer')
        employer_page()
    window3=Label(root,bg='white',height=600,width=1000).place(x=0,y=0)
    Button(window3,image=img6,bg='white',border=0,command=employee).place(x=70,y=50)
    Button(window3,image=img5,bg='white',border=0,command=employer).place(x=550,y=50)

def employee_page():
    def check_next():
        if degree.get()=='':
            backend.md_append('None')
        else:
            backend.md_append(degree.get())
        if skills.get()=='':
            backend.md_append('None')
        else:
            backend.md_append(skills.get())
        if qulification.get()=='':
            backend.md_append('None')
        else:
            backend.md_append(qulification.get())
        if workexp.get()=='':
            backend.md_append('None')
        else:
            backend.md_append(workexp.get())
        createpass_word()



    window4=Label(root,height=600,width=1000,image=background).place(x=0,y=0)
    Button(window4,bg='white',fg='#57a1f8',width=11,text='Back',font=('Segoe UI',13,'bold'),border=0,command=welcome,activebackground='white').place(x=552,y=523)
    Label(window4,bg='white').place(x=50,y=50)
    degree=Entry(window4,width=20,bg='white',font=('Segoe UI',21,),border=0)
    degree.place(x=605,y=75)
    skills=Entry(window4,width=20,bg='white',font=('Segoe UI',21,),border=0)
    skills.place(x=605,y=190)
    qulification=Entry(window4,width=20,bg='white',font=('Segoe UI',21,),border=0)
    qulification.place(x=605,y=305)
    workexp=Entry(window4,width=20,bg='white',font=('Segoe UI',21,),border=0)
    workexp.place(x=605,y=419)
    Button(window4,text='Next',bg='white',font=('Segoe UI',13,'bold'),width=11,border=0,fg='#57a1f8',activebackground='white',command=check_next).place(x=850,y=525)

def employer_page():
    def go_nextpage():
        a=cname.get()
        b=city.get()
        c=gstid.get()
        d=domain.get()
        if a=='Company name' or a=='':
            backend.md_append('None')
        else:
            backend.md_append(a)
        if b=='City' or b=='':
            backend.md_append('None')
        else:
            backend.md_append(b)
        if c=='GSTID' or c=='':
            backend.md_append('None')
        else:
            backend.md_append(c)
        if d=='Domain' or d=='':
            backend.md_append('None')
        else:
            backend.md_append(d)
        get_mail()
    def on_entry1(e):
        a=cname.get()
        if a=='Company name':
            cname.delete(0,END)
    def on_leave1(e):
        a=cname.get()
        if a=='':
            cname.insert(0,'Company name')
#==================================================================================================================
    def on_entry2(e):
        a=city.get()
        if a=='City':
            city.delete(0,END)
    def on_leave2(e):
        a=city.get()
        if a.isalpha():
            if a=='':
                city.insert(0,'City')
        else:
            city.delete(0,END)
            city.insert(0,'City')
#======================================================================================================================
    def on_entry3(e):
        a=gstid.get()
        if a=='GSTID':
            gstid.delete(0,END)
    def on_leave3(e):
        a=gstid.get()
        if a.isalnum():
            if a=='':
                gstid.insert(0,'GSTID')
        else:
            gstid.delete(0,END)
            gstid.insert(0,'GSTID') 
#=========================================================================================================================
    def on_entry4(e):
        a=domain.get()
        if a.lower()=='domain':
            domain.delete(0,END)
    def on_leave4(e):
        a=domain.get()
        if a=='':
            domain.insert(0,'Domain')
        
    window5=Label(root,height=600,width=1000,image=img9)
    window5.place(x=0,y=0)
    cname=Entry(window5,bg='white',font=('Segoe UI',25,),border=0,width=19)
    cname.place(x=580,y=70)
    city=Entry(window5,bg='white',font=('Segoe UI',25,),border=0,width=19)
    city.place(x=580,y=185)
    gstid=Entry(window5,bg='white',font=('Segoe UI',25,),border=0,width=19)
    gstid.place(x=580,y=295)
    domain=Entry(window5,bg='white',font=('Segoe UI',25,),border=0,width=19)
    domain.place(x=580,y=410)
    cname.insert(0,'Company name')
    city.insert(0,'City')
    gstid.insert(0,'GSTID')
    domain.insert(0,'Domain')
    cname.bind('<FocusIn>',on_entry1)
    cname.bind('<FocusOut>',on_leave1)
    city.bind('<FocusIn>',on_entry2)
    city.bind('<FocusOut>',on_leave2)
    gstid.bind('<FocusIn>',on_entry3)
    gstid.bind('<FocusOut>',on_leave3)
    domain.bind('<FocusIn>',on_entry4)
    domain.bind('<FocusOut>',on_leave4)
    Button(window5,bg='white'
    ,fg='black',text='Back',
    font=('Segoe UI',20,),
    width=7,border=0,
    activebackground='white',
    command=welcome).place(x=560,y=515)
    Button(window5,bg='white',
    fg='black'
    ,text='Next',
    font=('Segoe UI',20,),width=7,border=0,activebackground='white',
    command=go_nextpage).place(x=835,y=515)

def email_verifiction(o):
    a=backend.emailsender(o)
    if a==False:
        ssod()
    def ok_page():
        if str(a)==otp.get():
            backend.maindata.append(o)
            createpass_word()
        else:
            Frame(f1,bg='red',height=2,width=362).place(x=25,y=237)
    window6=Label(root,image=img10,bg='white')
    window6.place(x=0,y=0)
    f1=Frame(window6,bg='white',height=500,width=400)
    f1.place(x=550,y=50)
    Label(f1,text='Mail verification',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI light',30,'bold')).place(x=50,y=10)
    Label(f1,text='Verify your mail',fg='black',bg='white',font=('Century',20,'bold')).place(x=85,y=70)
    Label(f1,text='Gmail can show as spam',fg='black',bg='white',font=('Century',20,'bold')).place(x=35,y=120)
    otp=Entry(f1,width=19,bg='white',border=0,font=('Segoe UI',27))
    Frame(f1,bg='black',height=2,width=362).place(x=25,y=237)
    otp.place(x=25,y=185)
    #Label(f1,text='Didn,t receive the OTP?',fg='black',bg='white',font=('Segoe UI',15,),border=0).place(x=45,y=250)
    #Button(f1,text='Resend OTP',bg='white',fg='#57a1f8',font=('Segoe UI',14,),border=0,activebackground='white',command=resend_on).place(x=255,y=245)
    Button(f1,text='NEXT',bg='#57a1f8',fg='white',activebackground='#57a1f8',activeforeground='white',font=('Microsoft YaHei UI light',20,'bold'),width=8,border=0,command=ok_page).place(x=230,y=360)
    Button(f1,text='BACK',bg='#57a1f8',fg='white',activebackground='#57a1f8',activeforeground='white',font=('Microsoft YaHei UI light',20,'bold'),command=get_mail,width=8,border=0).place(x=40,y=360)
    
def get_mail():
    def next_1():
        Label(window7,text='Mail verification',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI light',30,'bold')).place(x=350,y=120)
        Label(window7,text='Enter your mail',fg='black',bg='white',font=('Century',20,'bold')).place(x=380,y=175)
        a=mail.get()
        if a!='' or a!='example@domine.com' and len(a)>10:
            if a[-4]=='.' and a.count('@')==1:
                email_verifiction(a)
            else:
                Frame(window7,bg='red',height=2,width=417).place(x=290,y=297)
        else:
                Frame(window7,bg='red',height=2,width=417).place(x=290,y=297)
    def on_entry(e):
        a=mail.get()
        if a=='example@domine.com':
            mail.delete(0,END)  
    window7=Label(root,image=img11,bg='#57a1f8')
    window7.place(x=0,y=0)
    Label(window7,text='Mail verification',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI light',30,'bold')).place(x=350,y=120)
    mail=Entry(window7,width=19,bg='white',border=0,font=('Segoe UI',30))
    mail.place(x=290,y=240)
    Label(window7,text='Enter your mail',fg='black',bg='white',font=('Century',20,'bold')).place(x=380,y=175)
    Frame(window7,bg='black',height=2,width=417).place(x=290,y=297)
    mail.insert(0,'example@domine.com')
    Button(window7,text='NEXT',bg='#57a1f8',fg='white',activebackground='#57a1f8',activeforeground='white',font=('Microsoft YaHei UI light',30,'bold'),width=10,border=0,command=next_1).place(x=370,y=350)
    mail.bind('<FocusIn>',on_entry)
def createpass_word():
    def next1_od():
        if len(np.get())>=8:
            if np.get()==cp.get():
                backend.md_append(np.get())
                ssod()
            else:
                Frame(f1,bg='red',width=360,height=2).place(x=35,y=305)
        else:
            Frame(f1,bg='red',width=360,height=2).place(x=35,y=185)
           
    w7=Label(root,height=600,width=1000,bg='white')
    w7.place(x=0,y=0)
    Label(w7,image=img7,bg='white').place(x=50,y=50)
    f1=Frame(w7,bg='white',height=530,width=430)
    f1.place(x=530,y=40)
    Label(f1,bg='white',fg='#57a1f8',font=('Microsoft YaHei UI light',30,'bold'),text='Create password').place(x=50,y=30)
    np=Entry(f1,bg='white',fg='black',width=21,font=('Segoe UI',23),border=0)
    np.place(x=35,y=140)
    Frame(f1,bg='black',width=360,height=2).place(x=35,y=185)
    cp=Entry(f1,bg='white',fg='black',width=21,font=('Segoe UI',23),border=0)
    cp.place(x=35,y=260)
    Frame(f1,bg='black',width=360,height=2).place(x=35,y=305)
    Button(f1,bg='#57a1f8',fg='white',font=('Segoe UI',15),border=0,text='Next',width=20,command=next1_od).place(x=100,y=380)
    def on_entry1(e):
        if np.get() == 'Password':
            np.delete(0,'end')
    def on_leave1(e):
        if np.get()=='':
            np.insert(0,'Password')

    def on_entry(e):
        if cp.get() == 'Confirm Password':
            cp.delete(0,'end')
    def on_leave(e):
        if cp.get()=='':
            cp.insert(0,'Confirm Password')
    np.insert(0,'Password')
    cp.insert(0,'Confirm Password')
    cp.bind('<FocusIn>',on_entry)
    cp.bind('<FocusOut>',on_leave)
    np.bind('<FocusIn>',on_entry1)
    np.bind('<FocusOut>',on_leave1)
def dataupdate():
    backend.new_data()
    sign_inpage()
def ssod():
    def see():
        print(backend.maindata)
        dataupdate()
    w8=Label(root,height=600,width=1000,bg='white',image=img8)
    w8.place(x=0,y=0)
    ttp='Hello '+backend.maindata[0]+' this is your username'
    usname=backend.create_username()
    Label(w8,text=ttp,font=('Microsoft YaHei UI light',30,'bold'),bg='#57a1f8').place(x=150,y=120)
    Label(w8,text=usname,font=('Microsoft YaHei UI light',50,'bold'),bg='#57a1f8',fg='white').place(x=270,y=290)
    Button(w8,text='>>>'
    ,font=('Microsoft YaHei UI light',40,'bold')
    ,bg='#57a1f8'
    ,fg='white'
    ,border=0
    ,activebackground='#57a1f8'
    ,command=see).place(x=600,y=440)
o1=PhotoImage(file='mainpage001.png')
def employee_120(ok):
    root1=tk.Tk()
    root1.geometry('1300x650')
    root1.resizable(False,False)
    o1=PhotoImage(file='mainpage001.png')
    k=[0]
    l=backend.randomchoi()
    def mm_001():
        def page1():
            mm_002(l[k[0]])
        def page2():
            mm_002(l[k[0]+1])
        def page3():
            mm_002(l[k[0]+2])
        def page4():
            mm_002(l[k[0]+3])
    
        def searchnew():
            m=search.get()
            if m=='':
                pass
            else:
                if m[0]=='#':
                    pass
                else:
                    l=backend.searchbar(m)
                    mm_001()

        def logout():
            root1.destroy()
        def rerpage():
            request_page(ok)
        window001=Label(root1,image=o1,bg='white')
        window001.place(x=0,y=0)
        search=Entry(window001,font=('Microsoft YaHei UI light',35,'bold'),width=16,bg='white',border=0)
        search.place(x=51,y=17)
        Button(window001,width=8,font=('Microsoft YaHei UI light',20,'bold'),bg='red',fg='white',text='Logout',border=0,activebackground='white',command=logout).place(x=1130,y=30)
        Button(window001,width=6,font=('Microsoft YaHei UI light',20,'bold'),bg='white',fg='#57a1f8',text='Search',border=0,activebackground='white',command=searchnew).place(x=536,y=17)
        Button(window001,width=8,font=('Microsoft YaHei UI light',20,'bold'),bg='red',fg='white',text='request',border=0,activebackground='white',command=rerpage).place(x=830,y=30)
        def backpage():
            if k==0:
                pass
            else:
                k[0]-=4
                mm_001()
        def nextpage():
            k[0]+=4
            mm_001()
        try:

            Frame(window001,width=1090,height=2,bg='black').place(x=11,y=110)
            Label(window001,text=l[k[0]][1],font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white').place(x=51,y=120)
            Label(window001,text=l[k[0]][3],font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white').place(x=501,y=120)
            Label(window001,text=str(l[k[0]][2]),font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white').place(x=51,y=180)
            Label(window001,text=l[k[0]][5],font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white').place(x=501,y=180)
            Label(window001,text=l[k[0]][0],font=('Microsoft YaHei UI light',25,'bold'),bg='#57a1f8',fg='black').place(x=751,y=150)
            Frame(window001,width=1090,height=2,bg='black').place(x=11,y=230)

            Button(window001,width=8,font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white',text='See More',border=0,activebackground='white',command=page1).place(x=1130,y=130)


            Label(window001,text=l[k[0]+1][1],font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white').place(x=51,y=120*2)
            Label(window001,text=l[k[0]+1][3],font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white').place(x=501,y=120*2)
            Label(window001,text=str(l[k[0]+1][2]),font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white').place(x=51,y=120*2+60)
            Label(window001,text=l[k[0]+1][5],font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white').place(x=501,y=120*2+60)
            Label(window001,text=l[k[0]+1][0],font=('Microsoft YaHei UI light',25,'bold'),bg='#57a1f8',fg='black').place(x=751,y=120*2+20)
            Frame(window001,width=1090,height=2,bg='black').place(x=11,y=230*2-110)
            Button(window001,width=8,font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white',text='See More',border=0,activebackground='white',command=page2).place(x=1130,y=130*2)

            Label(window001,text=l[k[0]+2][1],font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white').place(x=51,y=120*3)
            Label(window001,text=l[k[0]+2][3],font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white').place(x=501,y=120*3)
            Label(window001,text=str(l[k[0]+2][2]),font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white').place(x=51,y=120*3+60)
            Label(window001,text=l[k[0]+2][5],font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white').place(x=501,y=120*3+60)
            Label(window001,text=l[k[0]+2][0],font=('Microsoft YaHei UI light',25,'bold'),bg='#57a1f8',fg='black').place(x=751,y=120*3+20)
            Frame(window001,width=1090,height=2,bg='black').place(x=11,y=230*3-220)
            Button(window001,width=8,font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white',text='See More',border=0,activebackground='white',command=page3).place(x=1130,y=130*3)

            Label(window001,text=l[k[0]+3][1],font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white').place(x=51,y=120*4)
            Label(window001,text=l[k[0]+3][3],font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white').place(x=501,y=120*4)
            Label(window001,text=str(l[k[0]+3][2]),font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white').place(x=51,y=120*4+60)
            Label(window001,text=l[k[0]+3][5],font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white').place(x=501,y=120*4+60)
            Label(window001,text=l[k[0]+3][0],font=('Microsoft YaHei UI light',25,'bold'),bg='#57a1f8',fg='black').place(x=751,y=120*4+20)
            Button(window001,width=8,font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white',text='See More',border=0,activebackground='white',command=page4).place(x=1130,y=130*4-20)
        except:
            pass
        


        Button(window001,width=8,font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white',text='Next',border=0,activebackground='white',command=nextpage).place(x=1130,y=130*4+50)
        Button(window001,width=8,font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='black',text='Back',border=0,activebackground='#57a1f8',command=backpage).place(x=950,y=130*4+50)
    def mm_002(see):
        def backloop():
            mm_001()
        window002=Label(root1,bg='#57a1f8',width=1300,height=650)
        window002.place(x=0,y=0)
        empid='EMPID:'+see[0]
        name='NAME:'+see[1]
        dob='DOB:'+str(see[2])
        gender='GENDER:'+see[3]
        mobileno='MOBILENO:'+str(see[4])
        degree='DEGREE:'+see[5]
        qulifi='SPECIALATION:'+see[6]
        skills='SKILLS:'+see[7]
        working='WORKING EXP:'+see[8]

        Label(window002,text=empid,font=('Microsoft YaHei UI light',30,'bold'),bg='#57a1f8',fg='black').place(x=30,y=50)
        Label(window002,text=name,font=('Microsoft YaHei UI light',30,'bold'),bg='#57a1f8',fg='white').place(x=651,y=50)
        Label(window002,text=dob,font=('Microsoft YaHei UI light',30,'bold'),bg='#57a1f8',fg='white').place(x=30,y=180)
        Label(window002,text=gender,font=('Microsoft YaHei UI light',30,'bold'),bg='#57a1f8',fg='white').place(x=651,y=180)
        Label(window002,text=mobileno,font=('Microsoft YaHei UI light',30,'bold'),bg='#57a1f8',fg='white').place(x=30,y=310)
        Label(window002,text=degree,font=('Microsoft YaHei UI light',30,'bold'),bg='#57a1f8',fg='red').place(x=651,y=310)
        Label(window002,text=qulifi,font=('Microsoft YaHei UI light',30,'bold'),bg='#57a1f8',fg='white').place(x=30,y=440)
        Label(window002,text=skills,font=('Microsoft YaHei UI light',30,'bold'),bg='#57a1f8',fg='white').place(x=651,y=440)
        Label(window002,text=working,font=('Microsoft YaHei UI light',30,'bold'),bg='#57a1f8',fg='white').place(x=30,y=580)
        


        
        Button(window002,width=8,font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='black',text='Back',border=0,activebackground='#57a1f8',command=backloop).place(x=1130,y=130*4+50)

    def request_page(see):
        def deleterec():
            if (ql.get(),) in p:
                backend.deleteone(ql.get())
                request_page(see)
        def crtrec():
            if job.get()!='Job' and job.get()!='':
                if qulif.get()!='Degree' and qulif.get()!='':
                    if salary.get()!='Salary' and salary.get()!='' and salary.get().isdigit():
                        backend.createrequest(job.get(),qulif.get(),int(salary.get()),ok)
                        job.delete(0,'end')
                        qulif.delete(0,'end')
                        salary.delete(0,'end')
                        request_page(see)
                    else:
                        messagebox.showerror(f'error','fill it properly')
                        Frame(window003,width=545,height=2,bg='red').place(x=700,y=441+30+2)
                else:
                    messagebox.showerror(f'error','fill it properly')
                    Frame(window003,width=545,height=2,bg='red').place(x=700,y=312+30+1)
            else:
                Frame(window003,width=545,height=2,bg='red').place(x=700,y=183+30)
        def back_now():
            mm_001()


        
        p=backend.show_req(see)
        window003=Label(root1,bg='#141414',width=1300,height=650)
        window003.place(x=0,y=0)
        Label(window003,text='Job',font=('Microsoft YaHei UI light',20,'bold'),bg='#141414',fg='white').place(x=700,y=100)
        job=Entry(window003,font=('Microsoft YaHei UI light',35,'bold'),width=20,bg='white',border=0)
        job.place(x=700,y=120+30)
        Frame(window003,width=545,height=2,bg='#57a1f8').place(x=700,y=183+30)
        Label(window003,text='Qualification',font=('Microsoft YaHei UI light',20,'bold'),bg='#141414',fg='white').place(x=700,y=230)
        qulif=Entry(window003,font=('Microsoft YaHei UI light',35,'bold'),width=20,bg='white',border=0)
        qulif.place(x=700,y=250+30)
        Frame(window003,width=545,height=2,bg='#57a1f8').place(x=700,y=312+30+1)
        salary=Entry(window003,font=('Microsoft YaHei UI light',35,'bold'),width=20,bg='white',border=0)
        salary.place(x=700,y=380+30)
        Label(window003,text='Salary',font=('Microsoft YaHei UI light',20,'bold'),bg='#141414',fg='white').place(x=700,y=360)
        Frame(window003,width=545,height=2,bg='#57a1f8').place(x=700,y=441+30+2)
        Label(window003,text='Request page',font=('Microsoft YaHei UI light',35,'bold'),bg='#141414',fg='#57a1f8').place(x=830,y=10)



        ql=Entry(window003,font=('Microsoft YaHei UI light',35,'bold'),width=10,bg='white',border=0)
        ql.place(x=100,y=50)
        Button(window003,width=9,font=('Microsoft YaHei UI light',21,'bold'),bg='red',fg='white',text='Delete',command=deleterec,border=0,activebackground='#57a1f8').place(x=400,y=50)

        Button(window003,width=8,font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='black',text='back',border=0,activebackground='#57a1f8',command=back_now).place(x=700,y=490+30)
        Button(window003,width=8,font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='black',text='create',border=0,activebackground='#57a1f8',command=crtrec).place(x=1110,y=490+30)
        Frame(window003,width=2,height=700,bg='white').place(x=650,y=0)


        mk=Frame(window003,height=400,width=500,bg='white',border=3)
        mk.place(x=50,y=150)
        kko=backend.show_req(see)
        for i in range(1,len(kko)+1):
            Label(mk,text=kko[i-1],bg='white',fg='black',font=('Microsoft YaHei UI light',20,'bold')).place(x=20,y=40*i)
    







    mm_001()
    root1.mainloop()

def employer_120(ok):
    root2=tk.Tk()
    root2.geometry('1300x650')
    root2.resizable(False,False)
    
    k=[0]
    l=backend.employer_see()
    def mm_001():
        def page1():
            pass
        def page2():
            pass
        def page3():
            pass
        def page4():
            pass
    
        def searchnew():
            m=search.get()
            if m=='':
                pass
            else:
                l=backend.searchjob(m)
                mm_001()

        def logout():
            root2.destroy()
        def rerpage():
            request_page(ok)
        window001=Label(root2,width=1300,bg='#57a1f8',height=650)
        window001.place(x=0,y=0)
        search=Entry(window001,font=('Microsoft YaHei UI light',35,'bold'),width=16,bg='white',border=0)
        search.place(x=51,y=17)
        Button(window001,width=8,font=('Microsoft YaHei UI light',20,'bold'),bg='red',fg='white',text='Logout',border=0,activebackground='white',command=logout).place(x=1130,y=30)
        Button(window001,width=6,font=('Microsoft YaHei UI light',20,'bold'),bg='white',fg='#57a1f8',text='Search',border=0,activebackground='white',command=searchnew).place(x=536,y=17)
        Button(window001,width=8,font=('Microsoft YaHei UI light',20,'bold'),bg='red',fg='white',text='Resume',border=0,activebackground='white',command=rerpage).place(x=830,y=30)
        def backpage():
            if k==0:
                pass
            else:
                k[0]-=4
                mm_001()
        def nextpage():
            k[0]+=4
            mm_001()
        try:
            Frame(window001,width=1090,height=2,bg='black').place(x=11,y=110)
            Label(window001,text=l[k[0]][0],font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white').place(x=51,y=120)
            Label(window001,text=l[k[0]][1],font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white').place(x=501,y=120)
            Label(window001,text=str(l[k[0]][2]),font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white').place(x=51,y=180)
            Label(window001,text=l[k[0]][3],font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white').place(x=501,y=180)
            Label(window001,text=l[k[0]][4],font=('Microsoft YaHei UI light',25,'bold'),bg='#57a1f8',fg='black').place(x=751,y=150)
            Frame(window001,width=1090,height=2,bg='black').place(x=11,y=230)

            Button(window001,width=8,font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white',text='-Apply-',border=0,activebackground='white',command=page1).place(x=1130,y=130)


            Label(window001,text=l[k[0]+1][0],font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white').place(x=51,y=120*2)
            Label(window001,text=l[k[0]+1][1],font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white').place(x=501,y=120*2)
            Label(window001,text=str(l[k[0]+1][2]),font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white').place(x=51,y=120*2+60)
            Label(window001,text=l[k[0]+1][3],font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white').place(x=501,y=120*2+60)
            Label(window001,text=l[k[0]+1][4],font=('Microsoft YaHei UI light',25,'bold'),bg='#57a1f8',fg='black').place(x=751,y=120*2+20)
            Frame(window001,width=1090,height=2,bg='black').place(x=11,y=230*2-110)
            Button(window001,width=8,font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white',text='-Apply-',border=0,activebackground='white',command=page2).place(x=1130,y=130*2)

            Label(window001,text=l[k[0]+2][0],font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white').place(x=51,y=120*3)
            Label(window001,text=l[k[0]+2][1],font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white').place(x=501,y=120*3)
            Label(window001,text=str(l[k[0]+2][2]),font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white').place(x=51,y=120*3+60)
            Label(window001,text=l[k[0]+2][3],font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white').place(x=501,y=120*3+60)
            Label(window001,text=l[k[0]+2][4],font=('Microsoft YaHei UI light',25,'bold'),bg='#57a1f8',fg='black').place(x=751,y=120*3+20)
            Frame(window001,width=1090,height=2,bg='black').place(x=11,y=230*3-220)
            Button(window001,width=8,font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white',text='-Apply-',border=0,activebackground='white',command=page3).place(x=1130,y=130*3)

            Label(window001,text=l[k[0]+3][0],font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white').place(x=51,y=120*4)
            Label(window001,text=l[k[0]+3][1],font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white').place(x=501,y=120*4)
            Label(window001,text=str(l[k[0]+3][2]),font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white').place(x=51,y=120*4+60)
            Label(window001,text=l[k[0]+3][3],font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white').place(x=501,y=120*4+60)
            Label(window001,text=l[k[0]+3][4],font=('Microsoft YaHei UI light',25,'bold'),bg='#57a1f8',fg='black').place(x=751,y=120*4+20)
            Button(window001,width=8,font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white',text='-Apply-',border=0,activebackground='white',command=page4).place(x=1130,y=130*4-20)
        except:
            pass
        


        Button(window001,width=8,font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='white',text='Next',border=0,activebackground='white',command=nextpage).place(x=1130,y=130*4+50)
        Button(window001,width=8,font=('Microsoft YaHei UI light',20,'bold'),bg='#57a1f8',fg='black',text='Back',border=0,activebackground='#57a1f8',command=backpage).place(x=950,y=130*4+50)
    
    def request_page(see):
        def goback():
            mm_001()
        def nextpage():
            m=[]
            m.append(fath.get())
            m.append(nat.get())
            m.append(rel.get())
            m.append(lan.get())
            m.append(refer.get('1.0','end'))
            m.append(addr.get('1.0','end'))
            m.append(edu.get('1.0','end'))
            m.append(email.get())
            backend.lastmission(m,see)
            messagebox.showerror(f'SUCCESFULLY','SAVED')

        win=Label(root2,bg='#57a1f8',height=650,width=1300)
        win.place(x=0,y=0)
        fath=Entry(win,width=25,font=('Microsoft YaHei UI light',23,'bold'),border=2,bg='#57a1f8',fg='white')
        fath.place(x=50,y=50)
        nat=Entry(win,width=25,font=('Microsoft YaHei UI light',23,'bold'),border=2,bg='#57a1f8',fg='white')
        nat.place(x=50,y=150)
        rel=Entry(win,width=25,font=('Microsoft YaHei UI light',23,'bold'),border=2,bg='#57a1f8',fg='white')
        rel.place(x=50,y=150+100)
        lan=Entry(win,width=25,font=('Microsoft YaHei UI light',23,'bold'),border=2,bg='#57a1f8',fg='white')
        lan.place(x=50,y=150+200)

        refer=Text(win,width=45,font=('Microsoft YaHei UI light',13,'bold',),height=8,border=2,bg='#57a1f8',fg='white')
        refer.place(x=50,y=440)
        Label(win,text='FATHERNAME',font=('Microsoft YaHei UI light',21,'bold'),border=0,bg='#57a1f8',fg='black').place(x=50,y=10)
        Label(win,text='NATIONATILY',font=('Microsoft YaHei UI light',21,'bold'),border=0,bg='#57a1f8',fg='black').place(x=50,y=10+100)
        Label(win,text='RELIGION',font=('Microsoft YaHei UI light',21,'bold'),border=0,bg='#57a1f8',fg='black').place(x=50,y=10+200)
        Label(win,text='LANGUAGES KNOW',font=('Microsoft YaHei UI light',21,'bold'),border=0,bg='#57a1f8',fg='black').place(x=50,y=10+300)
        Label(win,text='REFERENCES',font=('Microsoft YaHei UI light',21,'bold'),border=0,bg='#57a1f8',fg='black').place(x=50,y=400)
        Frame(win,width=30,height=670,bg='white').place(x=600,y=0)
        Frame(win,width=30,height=670,bg='#57a1f8').place(x=630,y=0)
        Frame(win,width=30,height=670,bg='white').place(x=650,y=0)
        Label(win,text='ADDRESS',font=('Microsoft YaHei UI light',21,'bold'),border=0,bg='#57a1f8',fg='black').place(x=750,y=10)
        addr=Text(win,width=45,font=('Microsoft YaHei UI light',13,'bold'),border=2,bg='#57a1f8',fg='white',height=5)
        addr.place(x=750,y=50)
        Label(win,text='EDUCATION-QUALIFICATION',font=('Microsoft YaHei UI light',21,'bold'),border=0,bg='#57a1f8',fg='black').place(x=750,y=10+200)
        edu=Text(win,width=45,font=('Microsoft YaHei UI light',13,'bold'),border=2,bg='#57a1f8',fg='white',height=7)
        edu.place(x=750,y=250)
        Label(win,text='Email',font=('Microsoft YaHei UI light',21,'bold'),border=0,bg='#57a1f8',fg='black').place(x=750,y=30+400)
        email=Entry(win,width=25,font=('Microsoft YaHei UI light',23,'bold'),border=2,bg='#57a1f8',fg='white')
        email.place(x=750,y=150+320)


        Button(win,text='SAVE',width=7,font=('Microsoft YaHei UI light',21,'bold'),border=0,bg='#57a1f8',fg='white',activebackground='#57a1f8',command=nextpage).place(x=1150,y=560)
        Button(win,text='BACK',width=7,font=('Microsoft YaHei UI light',21,'bold'),border=0,bg='#57a1f8',fg='white',activebackground='#57a1f8',command=goback).place(x=750,y=560)

        







    mm_001()
    root2.mainloop()




sign_inpage()
employee_120()
root.mainloop()


