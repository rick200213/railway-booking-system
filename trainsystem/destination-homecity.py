from tkinter import *;
import pymysql;
def fromto():
    frm=t1.get()
    to=t2.get()
    con = pymysql.connect(host='localhost', user='root', passwd='Account1start', database='aritra')
    str="select * from train where fr='%s' and dest='%s' "
    args=(frm,to)
    cursor = con.cursor()
    cursor.execute(str%args)
    rows=cursor.fetchall()
    print(len(rows[0]))
    if rows is not None:
        for i in range(len(rows)):
            for j in range(len(rows[0])):
                e1 = Entry(frame, width=20, fg='blue', font=('arial', 16, 'bold'))
                e1.grid(row=i, column=j)
                e1.insert(END,rows[i][j])
                print(rows[i][j],end=' ')

    else:
        print('Invalid input')
window=Tk()
window.title("Ticket Booking")
frame=Frame(window,height=1600,width=1600,bg='green')
l1=Label(frame,text='From')
l2=Label(frame,text='To')
t1=Entry(frame,width=40)
t2=Entry(frame,width=40)
l1.place(x=200,y=200)
t1.place(x=250,y=200)
l2.place(x=200,y=250)
t2.place(x=250,y=250)
c1=Button(frame,height=2,width=40,text='Find',bg='blue',command=fromto)
c1.place(x=250,y=600)
frame.pack()
window.mainloop()

