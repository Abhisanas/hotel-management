from ast import Return
from logging import exception
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime



class room:
    def __init__(self,root):
        self.root=root
        self.root.title('Hotel Room')
        self.root.geometry('1210x620+145+73')
        
        #varialbles
        self.cust_contact=StringVar()
        self.check_indata=StringVar()
        self.check_outdata=StringVar()
        self.roomtype=StringVar()
        self.vailroom=StringVar()
        self.meal=StringVar()
        self.noofdays=StringVar()
        self.paidtax=StringVar()
        self.subtotal=StringVar()
        self.totalcost=StringVar()
        
        
        room_title_lbl=Label(self.root,text='Roombooking Details',font=('arail',20,'bold'),bg='white',fg='dark blue')
        room_title_lbl.place(x=0,y=1,relwidth=1)
        
        #label frame===================================
        label_frame=LabelFrame(self.root,text='Customer Detail',font=('arail',12,'bold'),padx=2)
        label_frame.place(x=5,y=40,width=430,height=575)
        
        cust_contact=Label(label_frame,text='Customer Contact',font=('arial',12,'bold'),padx=7,pady=9)
        cust_contact.grid(row=0,column=0,sticky=W)
        cust_contact_txt=ttk.Entry(label_frame,font=('arial',12,'bold'),width=20,textvariable=self.cust_contact)
        cust_contact_txt.grid(row=0,column=1,sticky=W)
        
        #button fetch data
        fetch_data_btn=Button(label_frame,text='Fetch Data',font=('arial',9,'bold'),command=self.fetch_data,bg='dark blue',fg='white',width=8)
        fetch_data_btn.place(x=350,y=6)
        
        check_indate=Label(label_frame,text='Check In Date',font=('arial',12,'bold'),padx=7,pady=9)
        check_indate.grid(row=1,column=0,sticky=W)
        check_indate_txt=ttk.Entry(label_frame,font=('arial',12,'bold'),width=25,textvariable=self.check_indata)
        check_indate_txt.grid(row=1,column=1)
        
        check_outdate=Label(label_frame,text='Check Out Date',font=('arial',12,'bold'),padx=7,pady=9)
        check_outdate.grid(row=2,column=0,sticky=W)
        check_outdate_txt=ttk.Entry(label_frame,font=('arial',12,'bold'),width=25,textvariable=self.check_outdata)
        check_outdate_txt.grid(row=2,column=1)
        
        room_type=Label(label_frame,text='Room Type',font=('arial',12,'bold'),padx=7,pady=9)
        room_type.grid(row=3,column=0,sticky=W)
        
        conn=mysql.connector.connect(host='localhost',username='root',password='R1234',database='hotel')
        mycursor=conn.cursor()
        mycursor.execute('select room_type from detail')
        rows1=mycursor.fetchall()
        
        room_type_txt=ttk.Combobox(label_frame,font=('arial',12,'bold'),state='readonly',width=23,textvariable=self.roomtype)
        room_type_txt['value']=rows1
        room_type_txt.grid(row=3,column=1)
        
        availabel_room=Label(label_frame,text='Available Room',font=('arial',12,'bold'),padx=7,pady=9)
        availabel_room.grid(row=4,column=0,sticky=W)
        #availabel_room_txt=ttk.Entry(label_frame,font=('arial',12,'bold'),width=25,textvariable=self.vailroom)
        #availabel_room_txt.grid(row=4,column=1)
        conn=mysql.connector.connect(host='localhost',username='root',password='R1234',database='hotel')
        mycursor=conn.cursor()
        mycursor.execute('select room_no from detail')
        rows=mycursor.fetchall()
        
        
        availabel_room_txt=ttk.Combobox(label_frame,font=('arial',12,'bold'),state='readonly',width=23,textvariable=self.vailroom)
        availabel_room_txt['value']=rows
        availabel_room_txt.grid(row=4,column=1)
        
        meal=Label(label_frame,text='Meal',font=('arial',12,'bold'),padx=7,pady=9)
        meal.grid(row=5,column=0,sticky=W)
        meal_txt=ttk.Entry(label_frame,font=('arial',12,'bold'),width=25,textvariable=self.meal)
        meal_txt.grid(row=5,column=1)
        
        noofdays=Label(label_frame,text='No Of Days',font=('arial',12,'bold'),padx=7,pady=9)
        noofdays.grid(row=6,column=0,sticky=W)
        noofdays_txt=ttk.Entry(label_frame,font=('arial',12,'bold'),width=25,textvariable=self.noofdays)
        noofdays_txt.grid(row=6,column=1)
        
        paidtax=Label(label_frame,text='Paid Tax',font=('arial',12,'bold'),padx=7,pady=9)
        paidtax.grid(row=7,column=0,sticky=W)
        paidtax_txt=ttk.Entry(label_frame,font=('arial',12,'bold'),width=25,textvariable=self.paidtax)
        paidtax_txt.grid(row=7,column=1)
        
        subtotal=Label(label_frame,text='Sub Total',font=('arial',12,'bold'),padx=7,pady=9)
        subtotal.grid(row=8,column=0,sticky=W)
        subtotal_txt=ttk.Entry(label_frame,font=('arial',12,'bold'),width=25,textvariable=self.subtotal)
        subtotal_txt.grid(row=8,column=1)
        
        totalcost=Label(label_frame,text='Total Cost',font=('arial',12,'bold'),padx=7,pady=9)
        totalcost.grid(row=9,column=0,sticky=W)
        totalcost_txt=ttk.Entry(label_frame,font=('arial',12,'bold'),width=25,textvariable=self.totalcost)
        totalcost_txt.grid(row=9,column=1)
        
        #bill button
        bill_btn=Button(label_frame,text='Bill',font=('arial',12,'bold'),command=self.total_data,bg='dark blue',fg='white',width=8)
        bill_btn.grid(row=10,column=0,sticky=W,padx=7,pady=9)
        
        
        #buttons------------------------------------------------------
        btn_frame=Frame(label_frame,bd=0,relief=RIDGE)
        btn_frame.place(x=0,y=470,width=422,height=60)
        
        add_btn=Button(btn_frame,text='Add',font=('arial',13,'bold'),command=self.add_data,bg='dark blue',fg='white',width=9)
        add_btn.grid(row=0,column=0,pady=6,padx=2)
        
        update_btn=Button(btn_frame,text='Update',font=('arial',13,'bold'),command=self.update_data,bg='dark blue',fg='white',width=9)
        update_btn.grid(row=0,column=1,pady=6,padx=2)
        
        delete_btn=Button(btn_frame,text='Delete',font=('arial',13,'bold'),command=self.delete_data,bg='dark blue',fg='white',width=9)
        delete_btn.grid(row=0,column=2,pady=6,padx=2)
        
        reset_btn=Button(btn_frame,text='Reset',font=('arial',13,'bold'),command=self.reset_data,bg='dark blue',fg='white',width=9)
        reset_btn.grid(row=0,column=3,pady=6,padx=2)
        
        #view details tabel ================================================
        tabel_frame=LabelFrame(self.root,text='View Details and Search Sytem',font=('arial',12,'bold'),padx=2)
        tabel_frame.place(x=440,y=280,width=765,height=335)
        
        searchby_lbl=Label(tabel_frame,text='Search By',bg='red',fg='white',font=('arial',13,'bold'))
        searchby_lbl.grid(row=0,column=0,padx=4,pady=9)
        
        #varialbles
        self.search_com=StringVar()
        self.search_txt=StringVar()
        
        search_com=ttk.Combobox(tabel_frame,font=('arial',13,'bold'),width=20,textvariable=self.search_com)
        search_com['value']=('Select','contact','avilabel_room')
        search_com.current(0)
        search_com.grid(row=0,column=1,padx=4,pady=9)
        
        search_txt=ttk.Entry(tabel_frame,font=('arial',13,'bold'),width=22,textvariable=self.search_txt)
        search_txt.grid(row=0,column=2,padx=4,pady=9)
        
        search_btn=Button(tabel_frame,text='Search By',font=('arial',12,'bold'),command=self.search_data,bg='dark blue',fg='white',width=10)
        search_btn.grid(row=0,column=3,padx=4,pady=9)
        
        searachall_btn=Button(tabel_frame,text='Search All',font=('arial',12,'bold'),command=self.fetch_datachildren,bg='dark blue',fg='white',width=10)
        searachall_btn.grid(row=0,column=4,padx=4,pady=9)
        
        #detail frame====================================
        detail_frame=Frame(tabel_frame,bd=3,relief=RIDGE,bg='white')
        detail_frame.place(x=7,y=45,width=740,height=260)
        
        scroll_x=ttk.Scrollbar(detail_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detail_frame,orient=VERTICAL)
        
        self.room_tabel=ttk.Treeview(detail_frame,columns=('cust contact','in date','out date','room type','avai room','meal','noofdays'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.room_tabel.xview)
        scroll_y.config(command=self.room_tabel.yview)
        
        self.room_tabel.heading('cust contact',text=' Contact')
        self.room_tabel.heading('in date',text='Check In Date')
        self.room_tabel.heading('out date',text='Check Out Date')
        self.room_tabel.heading('room type',text='Room Type')
        self.room_tabel.heading('avai room',text='Available Room')
        self.room_tabel.heading('meal',text='Meal')
        self.room_tabel.heading('noofdays',text='NO Of Days')
        #self.room_tabel.heading('paidtax',text='Paid Tax')
        #self.room_tabel.heading('subtotal',text='Sub Total')
        #self.room_tabel.heading('totalcost',text='Total Cost')
        
        self.room_tabel['show']='headings'
        
        self.room_tabel.column('cust contact',width=100)
        self.room_tabel.column('in date',width=100)
        self.room_tabel.column('out date',width=100)
        self.room_tabel.column('room type',width=100)
        self.room_tabel.column('avai room',width=100)
        self.room_tabel.column('meal',width=100)
        self.room_tabel.column('noofdays',width=100)
        #self.room_tabel.column('paidtax',width=100)
        #self.room_tabel.column('subtotal',width=100)
        #self.room_tabel.column('totalcost',width=100)
        
        self.room_tabel.pack(fill=BOTH,expand=1)
        self.room_tabel.bind('<ButtonRelease>',self.cursor_data)
        
        self.fetch_datachildren()
        
    #fetch data
    def fetch_data(self):
        if  self.cust_contact.get()=='':
            messagebox.showerror('Error','All Fields Are Required',parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='R1234',database='hotel')
            mycursor=conn.cursor()
            mycursor.execute('select cust_name from hotel where Mobile=%s',(self.cust_contact.get(),))
            row3=mycursor.fetchone()
            if row3==None:
                messagebox.showerror('Error','This Number Not Found',parent=self.root)
            else:
                conn.commit()
                conn.close()
                
                #show data frame
                showdataframe=Frame(self.root,bd=3,relief=RIDGE,bg='white')
                showdataframe.place(x=802,y=40,width=400,height=245)
                
                name_lbl=Label(showdataframe,text='Name',font=('arial',12,'bold'),bg='white')
                name_lbl.grid(row=0,column=0,padx=4,pady=6,sticky=W)
                name=Label(showdataframe,text=row3,font=('arial',12,'bold'),bg='white')
                name.grid(row=0,column=1,padx=4,pady=6)
                
                
                conn=mysql.connector.connect(host='localhost',username='root',password='R1234',database='hotel')
                mycursor=conn.cursor()
                mycursor.execute('select gender from hotel where Mobile=%s',(self.cust_contact.get(),))
                row3=mycursor.fetchone()
                
                gender_lbl=Label(showdataframe,text='Gender',font=('arial',12,'bold'),bg='white')
                gender_lbl.grid(row=1,column=0,padx=4,pady=6,sticky=W)
                gender=Label(showdataframe,text=row3,font=('arial',12,'bold'),bg='white')
                gender.grid(row=1,column=1,padx=4,pady=6)
               
                conn=mysql.connector.connect(host='localhost',username='root',password='R1234',database='hotel')
                mycursor=conn.cursor()
                mycursor.execute('select email from hotel where Mobile=%s',(self.cust_contact.get(),))
                row3=mycursor.fetchone()
                
                email_lbl=Label(showdataframe,text='Email',font=('arial',12,'bold'),bg='white')
                email_lbl.grid(row=2,column=0,padx=4,pady=6,sticky=W)
                email=Label(showdataframe,text=row3,font=('arial',12,'bold'),bg='white')
                email.grid(row=2,column=1,padx=4,pady=6)
                
                conn=mysql.connector.connect(host='localhost',username='root',password='R1234',database='hotel')
                mycursor=conn.cursor()
                mycursor.execute('select nationality from hotel where Mobile=%s',(self.cust_contact.get(),))
                row3=mycursor.fetchone()
                
                nationality_lbl=Label(showdataframe,text='Nationality',font=('arial',12,'bold'),bg='white')
                nationality_lbl.grid(row=3,column=0,padx=4,pady=6,sticky=W)
                nationality=Label(showdataframe,text=row3,font=('arial',12,'bold'),bg='white')
                nationality.grid(row=3,column=1,padx=4,pady=6)
                
                conn=mysql.connector.connect(host='localhost',username='root',password='R1234',database='hotel')
                mycursor=conn.cursor()
                mycursor.execute('select address from hotel where Mobile=%s',(self.cust_contact.get(),))
                row3=mycursor.fetchone()
                
                address_lbl=Label(showdataframe,text='Address',font=('arial',12,'bold'),bg='white')
                address_lbl.grid(row=4,column=0,padx=4,pady=6,sticky=W)
                address=Label(showdataframe,text=row3,font=('arial',12,'bold'),bg='white')
                address.grid(row=4,column=1,padx=4,pady=6)
                
                
    #add data
    def add_data(self):
         
        if self.cust_contact.get()=='' or self.check_indata.get()=='':
            messagebox.showerror('Error','All Field Are Required',parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='R1234',database='hotel')
                mycursor=conn.cursor()
                mycursor.execute('insert into roomb values(%s,%s,%s,%s,%s,%s,%s)',(
                
                                                        self.cust_contact.get(),
                                                        self.check_indata.get(),
                                                        self.check_outdata.get(),
                                                        self.roomtype.get(),
                                                        self.vailroom.get(),
                                                        self.meal.get(),
                                                        self.noofdays.get()
        
                
                
                                                                        ))
                conn.commit()
                self.fetch_datachildren()
                conn.close()
                messagebox.showinfo('Seccess','Data Added Succesfully',parent=self.root)
            
            except exception as e:
                messagebox.showwarning('Warning',f'Something went wrong:{str(e)}',parent=self.root)
                
    #fetch data
    def fetch_datachildren(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='R1234',database='hotel')
        mycursor=conn.cursor()
        mycursor.execute('select * from roomb')
        row1=mycursor.fetchall()
        
        if len(row1)!=0:
            self.room_tabel.delete(*self.room_tabel.get_children())
            for i in row1:
                self.room_tabel.insert('',END,values=i)
            conn.commit()
        conn.close()
        
    #cursor
    def cursor_data(self,event=''):
        data=self.room_tabel.focus()
        content1=self.room_tabel.item(data)
        row=content1['values']
        
        self.cust_contact.set(row[0])
        self.check_indata.set(row[1])
        self.check_outdata.set(row[2])
        self.roomtype.set(row[3])
        self.vailroom.set(row[4])
        self.meal.set(row[5])
        self.noofdays.set(row[6])
        
     #update data   
    def update_data(self):
        if self.cust_contact.get()=='' or self.check_indata.get()=='':
            messagebox.showerror('Error','All Field Are Required',parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='R1234',database='hotel')
                mycursor=conn.cursor()
                mycursor.execute('update roomb set  check_in=%s, check_out=%s, roomtype=%s, avilabel_room=%s, meal=%s, noofdays=%s where contact=%s',(
                  
                                                                                   
                                                                                    
                                                                                    self.check_indata.get(),
                                                                                    self.check_outdata.get(),
                                                                                    self.roomtype.get(),
                                                                                    self.vailroom.get(),
                                                                                    self.meal.get(),
                                                                                    self.noofdays.get(),
                                                                                    self.cust_contact.get()
              
                                                                                                                                                      ))
                conn.commit()
                self.fetch_datachildren()
                conn.close()
                messagebox.showinfo('Success','Your Data Update Succesfully')
            except exception as e:
                messagebox.showwarning('Warning',f'something went wrorng{str(e)}',parent=self.root)
                
    #delete data
    def delete_data(self):
        delete=messagebox.askyesno('YES OR NO','You Sure To Delete Data',parent=self.root)
        if delete>0:
            
                conn=mysql.connector.connect(host='localhost',username='root',password='R1234',database='hotel')
                mycursor=conn.cursor()
                mycursor.execute('delete from roomb where contact=%s',(self.cust_contact.get(),))
                
                conn.commit()
                self.fetch_datachildren()
                conn.close()
                messagebox.showinfo('Success','Your Data Succesfully Deleted')
        else:
            Return
            
                
    #reset data
    def reset_data(self):
    
        self.check_indata.set('')
        self.check_outdata.set('')
        self.roomtype.set('')
        self.vailroom.set('')
        self.meal.set('')
        self.noofdays.set('')
        self.cust_contact.set('')
        self.paidtax.set('')
        self.subtotal.set('')
        self.totalcost.set('')
        
    #search data
    def search_data(self):
        if self.search_com.get()=='' or self.search_txt.get()=='':
            messagebox.showerror('Error','All Fields Are Requuired')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='R1234',database='hotel')
                mycursor=conn.cursor()
                mycursor.execute('select * from roomb where ' +str(self.search_com.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
                row=mycursor.fetchall()
                if len(row)!=0:
                    self.room_tabel.delete(*self.room_tabel.get_children())
                    for i in row:
                        self.room_tabel.insert('',END,values=i)
                    conn.commit()
                conn.close()
                messagebox.showinfo('Success','Success')
            except exception as e:
                messagebox.showwarning('Warning',f'Something went Wrong{str(e)}',parent=self.root)
                
    #date atomatically count function creation
    def total_data(self):
        indate=self.check_indata.get()
        outdate=self.check_outdata.get()
        
        indate=datetime.strptime(indate,"%d/%m/%Y")
        outdate=datetime.strptime(outdate,"%d/%m/%Y")
        
        self.noofdays.set(abs(outdate-indate).days)
        
        if (self.meal.get()=='lunch' and self.roomtype.get()=='Luxary'):
            
            w1=float(300)
            w2=float(700)
            w3=float(self.noofdays.get())
            w4=(w1+w2+w3)
            
            paid='Rs.'+str("%.2f"%((w4)*0.09))
            
            sub="Rs."+str("%.2f"%((w4)))
            
            total="Rs."+str("%.2f"%(w4+((w4)*0.09)))
            
            self.paidtax.set(paid)
            self.subtotal.set(sub)
            self.totalcost.set(total)
            
        elif (self.meal.get()=='breakfast' and self.roomtype.get()=='Single'):
            
            w1=float(300)
            w2=float(500)
            w3=float(self.noofdays.get())
            w4=(w1+w2+w3)
            
            paid='Rs.'+str("%.2f"%((w4)*0.09))
            
            sub="Rs."+str("%.2f"%((w4)))
            
            total="Rs."+str("%.2f"%(w4+((w4)*0.09)))
            
            self.paidtax.set(paid)
            self.subtotal.set(sub)
            self.totalcost.set(total)
            
        elif (self.meal.get()=='breakfast' and self.roomtype.get()=='Double'):
            
            w1=float(500)
            w2=float(900)
            w3=float(self.noofdays.get())
            w4=(w1+w2+w3)
            
            paid='Rs.'+str("%.2f"%((w4)*0.09))
            
            sub="Rs."+str("%.2f"%((w4)))
            
            total="Rs."+str("%.2f"%(w4+((w4)*0.09)))
            
            self.paidtax.set(paid)
            self.subtotal.set(sub)
            self.totalcost.set(total)
        
        
                
                
                
                
            
        
        
        
        
        
        
        
        
        
if __name__=='__main__':
    root=Tk()
    obj=room(root)
    root.mainloop()