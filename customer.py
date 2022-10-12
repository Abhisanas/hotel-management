from importlib.resources import contents
from logging import exception
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import random


class customer_win:
    def __init__(self,root):
        
        self.root=root
        self.root.title('CUSTOMER')
        self.root.geometry('1210x620+145+73')
        
        self.cust_ref=StringVar()
        x=random.randint(1000,9999)
        self.cust_ref.set(str(x))
        
        
        self.cust_name=StringVar()
        self.mother_name=StringVar()
        self.gender=StringVar()
        self.post_code=StringVar()
        self.mobile=StringVar()
        self.email=StringVar()
        self.nationality=StringVar()
        self.id_proof=StringVar()
        self.id_no=StringVar()
        self.address=StringVar()
        
        
        cust_title_lbl=Label(self.root,text='Add Customer Details',font=('arail',20,'bold'),bg='white',fg='dark blue')
        cust_title_lbl.place(x=0,y=1,relwidth=1)
        
        #label frame=========================================
        label_frame=LabelFrame(self.root,text='Customer Detail',font=('arail',12,'bold'),padx=2)
        label_frame.place(x=5,y=40,width=430,height=575)
        
        cust_ref=Label(label_frame,text='Customer Ref',font=('arial',12,'bold'),padx=7,pady=9)
        cust_ref.grid(row=0,column=0,sticky=W)
        cust_ref_txt=ttk.Entry(label_frame,width=25,font=('arial',12,'bold'),textvariable=self.cust_ref,state='readonly')
        cust_ref_txt.grid(row=0,column=1)
        
        cust_name=Label(label_frame,text='Customer Name',font=('arial',12,'bold'),padx=7,pady=9)
        cust_name.grid(row=1,column=0,sticky=W)
        cust_name_txt=ttk.Entry(label_frame,width=25,font=('arial',12,'bold'),textvariable=self.cust_name)
        cust_name_txt.grid(row=1,column=1)
        
        mother_name=Label(label_frame,text='Mother Name',font=('arial',12,'bold'),padx=7,pady=9)
        mother_name.grid(row=2,column=0,sticky=W)
        mother_name_txt=ttk.Entry(label_frame,width=25,font=('arial',12,'bold'),textvariable=self.mother_name)
        mother_name_txt.grid(row=2,column=1)
        
        gender=Label(label_frame,text='Gender',font=('arial',12,'bold'),padx=7,pady=9)
        gender.grid(row=3,column=0,sticky=W)
        gender_com=ttk.Combobox(label_frame,width=23,font=('arial',12,'bold'),state='readonly',textvariable=self.gender)
        gender_com['value']=('Select Gender','Male','Female')
        gender_com.current(0)
        gender_com.grid(row=3,column=1)
        
        postcode=Label(label_frame,text='Post Code',font=('arial',12,'bold'),padx=7,pady=9)
        postcode.grid(row=4,column=0,sticky=W)
        postcode_txt=ttk.Entry(label_frame,width=25,font=('arial',12,'bold'),textvariable=self.post_code)
        postcode_txt.grid(row=4,column=1)
        
        mobile=Label(label_frame,text='Mobile No',font=('arial',12,'bold'),padx=7,pady=9)
        mobile.grid(row=5,column=0,sticky=W)
        mobile_txt=ttk.Entry(label_frame,width=25,font=('arial',12,'bold'),textvariable=self.mobile)
        mobile_txt.grid(row=5,column=1)
        
        email=Label(label_frame,text='Email',font=('arial',12,'bold'),padx=7,pady=9)
        email.grid(row=6,column=0,sticky=W)
        email_txt=ttk.Entry(label_frame,width=25,font=('arial',12,'bold'),textvariable=self.email)
        email_txt.grid(row=6,column=1)
        
        nationality=Label(label_frame,text='Nationality',font=('arial',12,'bold'),padx=7,pady=9)
        nationality.grid(row=7,column=0,sticky=W)
        nationality_com=ttk.Combobox(label_frame,width=23,font=('arial',12,'bold'),state='readonly',textvariable=self.nationality)
        nationality_com['value']=('Select Nationality','India','United Kingdom','America','Russia','Japan')
        nationality_com.current(0)
        nationality_com.grid(row=7,column=1)
        
        id_proof_type=Label(label_frame,text='ID Proof Type',font=('arial',12,'bold'),padx=7,pady=9)
        id_proof_type.grid(row=8,column=0,sticky=W)
        id_proof_com=ttk.Combobox(label_frame,width=23,font=('arial',12,'bold'),state='readonly',textvariable=self.id_proof)
        id_proof_com['value']=('Select ID Proof','Adhar Card','Drawing License','Passport')
        id_proof_com.current(0)
        id_proof_com.grid(row=8,column=1)
        
        id_no=Label(label_frame,text='ID Number',font=('arial',12,'bold'),padx=7,pady=9)
        id_no.grid(row=9,column=0,sticky=W)
        id_not_xt=ttk.Entry(label_frame,width=25,font=('arial',12,'bold'),textvariable=self.id_no)
        id_not_xt.grid(row=9,column=1)
        
        address=Label(label_frame,text='address',font=('arial',12,'bold'),padx=7,pady=9)
        address.grid(row=10,column=0,sticky=W)
        address_txt=ttk.Entry(label_frame,width=25,font=('arial',12,'bold'),textvariable=self.address)
        address_txt.grid(row=10,column=1)
        
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
        
        #tabel frame==========================================================
        tabel_frame=LabelFrame(self.root,text='View Details and Search Sytem',font=('arial',12,'bold'),padx=2)
        tabel_frame.place(x=440,y=40,width=765,height=575)
        
        searchby_lbl=Label(tabel_frame,text='Search By',bg='red',fg='white',font=('arial',13,'bold'))
        searchby_lbl.grid(row=0,column=0,padx=4,pady=9)
        
        #varialbles
        self.search_com=StringVar()
        self.search_txt=StringVar()
        
        search_com=ttk.Combobox(tabel_frame,font=('arial',13,'bold'),width=20,textvariable=self.search_com)
        search_com['value']=('Select','Mobile','Refrence')
        search_com.current(0)
        search_com.grid(row=0,column=1,padx=4,pady=9)
        
        search_txt=ttk.Entry(tabel_frame,font=('arial',13,'bold'),width=22,textvariable=self.search_txt)
        search_txt.grid(row=0,column=2,padx=4,pady=9)
        
        search_btn=Button(tabel_frame,text='Search By',font=('arial',12,'bold'),command=self.search_data,bg='dark blue',fg='white',width=10)
        search_btn.grid(row=0,column=3,padx=4,pady=9)
        
        searach_btn=Button(tabel_frame,text='Search All',font=('arial',12,'bold'),command=self.fetch_data,bg='dark blue',fg='white',width=10)
        searach_btn.grid(row=0,column=4,padx=4,pady=9)
        
        #detail frame====================================
        detail_frame=Frame(tabel_frame,bd=3,relief=RIDGE,bg='white')
        detail_frame.place(x=7,y=55,width=740,height=490)
        
        scroll_x=ttk.Scrollbar(detail_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detail_frame,orient=VERTICAL)
        self.customer_tabel=ttk.Treeview(detail_frame,columns=('Cust ref','cust name','mother name','gender','post code','mobile no','email','nationality','id proof','id no','address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.customer_tabel.xview)
        scroll_y.config(command=self.customer_tabel.yview)
        
        self.customer_tabel.heading('Cust ref',text='Customer Ref')
        self.customer_tabel.heading('cust name',text='Customer Name')
        self.customer_tabel.heading('mother name',text='Mother Name')
        self.customer_tabel.heading('gender',text='Gender')
        self.customer_tabel.heading('post code',text='Post Code')
        self.customer_tabel.heading('mobile no',text='Mobile NO')
        self.customer_tabel.heading('email',text='Email')
        self.customer_tabel.heading('nationality',text='Nationality')
        self.customer_tabel.heading('id proof',text='Id Proof')
        self.customer_tabel.heading('id no',text='ID Number')
        self.customer_tabel.heading('address',text='Address')
        
        self.customer_tabel['show']='headings'
        
        self.customer_tabel.column('Cust ref',width=100)
        self.customer_tabel.column('cust name',width=100)
        self.customer_tabel.column('mother name',width=100)
        self.customer_tabel.column('gender',width=100)
        self.customer_tabel.column('post code',width=100)
        self.customer_tabel.column('mobile no',width=100)
        self.customer_tabel.column('email',width=100)
        self.customer_tabel.column('nationality',width=100)
        self.customer_tabel.column('id proof',width=100)
        self.customer_tabel.column('id no',width=100)
        self.customer_tabel.column('address',width=100)
        
        self.customer_tabel.pack(fill=BOTH,expand=1)
        self.customer_tabel.bind('<ButtonRelease>',self.cursor_data)
        self.fetch_data()
        
    #add data
    def add_data(self):
        if self.mobile.get()=='' or self.cust_name.get()=='':
            messagebox.showerror('Error','All Field Are Required',parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='R1234',database='hotel')
                mycursor=conn.cursor()
                mycursor.execute('insert into hotel values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                
                                                      self.cust_ref.get(),
                                                      self.cust_name.get(),
                                                      self.mother_name.get(),
                                                      self.gender.get(),
                                                      self.post_code.get(),
                                                      self.mobile.get(),
                                                      self.email.get(),
                                                      self.nationality.get(),
                                                      self.id_proof.get(),
                                                      self.id_no.get(),
                                                      self.address.get()
                
                
                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Seccess','Data Added Succesfully',parent=self.root)
            except exception as e:
                messagebox.showwarning('Warning',f'Something went wrong:{str(e)}',parent=self.root)
                
    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='R1234',database='hotel')
        mycursor=conn.cursor()
        mycursor.execute('select * from hotel')
        row=mycursor.fetchall()
        if len(row)!=0:
            self.customer_tabel.delete(*self.customer_tabel.get_children())
            for i in row:
                self.customer_tabel.insert('',END,values=i)
            conn.commit()
        conn.close()
        
    #get cursor
    def cursor_data(self,event=''):
        cursor_row=self.customer_tabel.focus()
        data=self.customer_tabel.item(cursor_row)
        row1=data['values']
        
        self.cust_ref.set(row1[0])
        self.cust_name.set(row1[1])
        self.mother_name.set(row1[2])
        self.gender.set(row1[3])
        self.post_code.set(row1[4])
        self.mobile.set(row1[5])
        self.email.set(row1[6])
        self.nationality.set(row1[7])
        self.id_proof.set(row1[8])
        self.id_no.set(row1[9])
        self.address.set(row1[10])
        
    #update data
    def update_data(self):
        if self.mobile.get()=='' or self.cust_name.get()=='':
            messagebox.showerror('Error','All Field Are Required',parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='R1234',database='hotel')
                mycursor=conn.cursor()
                mycursor.execute('update hotel set cust_name=%s, mothe_name=%s, gender=%s, post_code=%s, Mobile=%s, email=%s, nationality=%s, id_proof=%s, id_no=%s, address=%s where Refrence=%s',(
                  
                                                                                   
                                                                                     self.cust_name.get(),
                                                                                     self.mother_name.get(),
                                                                                     self.gender.get(),
                                                                                     self.post_code.get(),
                                                                                     self.mobile.get(),
                                                                                     self.email.get(),
                                                                                     self.nationality.get(),
                                                                                     self.id_proof.get(),
                                                                                     self.id_no.get(),
                                                                                     self.address.get(),
                                                                                     self.cust_ref.get()
              
                                                                                                                                                                              ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Your Data Update Succesfully')
            except exception as e:
                messagebox.showwarning('Warning',f'something went wrorng{str(e)}',parent=self.root)
                
    #delete data
    def delete_data(self):
        if self.mobile.get()=='' or self.cust_name.get()=='':
            messagebox.showerror('Error','All Field Are Required',parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='R1234',database='hotel')
                mycursor=conn.cursor()
                mycursor.execute('delete from hotel where Refrence=%s',(self.cust_ref.get(),))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Your Data Succesfully Deleted')
            except exception as e:
                messagebox.showwarning('Warning',f'Something Went Wrong{str(e)}',parent=self.root)
                
    #reset data
    def reset_data(self):
        
        x=random.randint(1000,9999)
        self.cust_ref.set(str(x))
        
        self.cust_name.set('')
        self.mother_name.set('')
        self.gender.set('Select Gender')
        self.post_code.set('')
        self.mobile.set('')
        self.email.set('')
        self.nationality.set('Select Nationality')
        self.id_proof.set('Select Id Proof')
        self.id_no.set('')
        self.address.set('')
        
    #search data
    def search_data(self):
        if self.search_com.get()=='' or self.search_txt.get()=='':
            messagebox.showerror('Error','All Fields Are Requuired')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='R1234',database='hotel')
                mycursor=conn.cursor()
                mycursor.execute('select * from hotel where ' +str(self.search_com.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
                row=mycursor.fetchall()
                if len(row)!=0:
                    self.customer_tabel.delete(*self.customer_tabel.get_children())
                    for i in row:
                        self.customer_tabel.insert('',END,values=i)
                    conn.commit()
                conn.close()
                messagebox.showinfo('Success','Success')
            except exception as e:
                messagebox.showwarning('Warning',f'Something went Wrong{str(e)}',parent=self.root)
                        
            
        
        
        
            
       
        
                      
if __name__=='__main__':
    root=Tk()
    obj=customer_win(root)
    root.mainloop()