from tkinter import *;
import pymysql;
def ticketgen():
    name = t1.get()
    Age =int(t2.get())
    datej=t4.get()
    fr=t5.get()
    dest=t6.get()
    trainno=int(t7.get())
    clas=t8.get()
    con = pymysql.connect(host='localhost', user='root', passwd='Account1start', database='aritra')
    str= "select Departure,Arrival,dist from train where train_no='%d'"
    args=(trainno)
    str2="select max(pnr) from passengers1"
    cursor = con.cursor()
    cursor1 = con.cursor()
    cursor.execute(str % args)
    cursor1.execute(str2)
    rows=cursor.fetchone()
    pnr=cursor1.fetchone()
    print(pnr[0])
    pnr1=pnr[0]
    pnr1=pnr1+1
    departure=rows[0]
    arrival=rows[1]
    if rows  is not None:
        if clas=='First':
          perkm=6
        elif clas=='2AC':
            perkm=5
        elif clas=='3AC':
            perkm=4;
        elif clas=='Sleeper':
            perkm=3;
        else:
            perkm=2;
        price=rows[2]*perkm
        if Age >= 60:
            price=price*0.70
        str1="insert into passengers1 values('%d','%s','%d','%s','%d','%s','%s','%s','%d','%s','%s')"
        args=(pnr1,name,Age,datej,trainno,fr,dest,clas,price,departure,arrival)
        cursor = con.cursor()
        cursor.execute(str1 % args)
        try:
            con.commit()
            print('Value Interted')
        except:
            con.rollback()
    else:
        l9=Label(frame,text='Wrongtrainno')
        l9.place(x=280,y=500)


window=Tk()
window.title("Ticket Booking")
frame=Frame(window,height=1600,width=1600,bg='green')
l1=Label(frame,text='Name')
l2=Label(frame,text='Age')
l4=Label(frame,text='DOJ')
t4=Entry(frame,width=40)
t1=Entry(frame,width=40)
t2=Entry(frame,width=40)
l5=Label(frame,text='From')
t5=Entry(frame,width='40')
l6=Label(frame,text='Dest')
t6=Entry(frame,width='40')
l7=Label(frame,text='Trainno.')
t7=Entry(frame,width='40')
l8=Label(frame,text='Class')
t8=Entry(frame,width='40')
l1.place(x=200,y=200)
t1.place(x=250,y=200)
l2.place(x=200,y=250)
t2.place(x=250,y=250)
l4.place(x=200,y=300)
t4.place(x=250,y=300)
l5.place(x=200,y=350)
t5.place(x=250,y=350)
l6.place(x=200,y=400)
t6.place(x=250,y=400)
l7.place(x=200,y=500)
t7.place(x=250,y=500)
l8.place(x=200,y=550)
t8.place(x=250,y=550)
c1=Button(frame,height=2,width=40,text='Pay',bg='blue',command=ticketgen)
c1.place(x=250,y=600)
frame.pack()
window.mainloop()

