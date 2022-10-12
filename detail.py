from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from logging import exception


class detail:
    def __init__(self,root):
        self.root=root
        self.root.title('Hotel Room')
        self.root.geometry('1210x620+145+73')
        
        
        #variables
        self.var_floor=StringVar()
        self.var_roomno=StringVar()
        self.var_roomtype=StringVar()
        
        detail_title_lbl=Label(self.root,text=' Hotel Details',font=('arail',20,'bold'),bg='white',fg='dark blue')
        detail_title_lbl.place(x=0,y=1,relwidth=1)
        
        
        #label frame
        label_frame=LabelFrame(self.root,text='New Room Add',font=('arail',12,'bold'),padx=2)
        label_frame.place(x=5,y=40,width=470,height=470)
        
        
        floor=Label(label_frame,text='Floor',font=('arial',12,'bold'),padx=7,pady=9)
        floor.grid(row=0,column=0,sticky=W)
        floor_txt=ttk.Entry(label_frame,font=('arial',12,'bold'),width=25,textvariable=self.var_floor)
        floor_txt.grid(row=0,column=1)
        
        roomno=Label(label_frame,text='Room No',font=('arial',12,'bold'),padx=7,pady=9)
        roomno.grid(row=1,column=0,sticky=W)
        roomno_txt=ttk.Entry(label_frame,font=('arial',12,'bold'),width=25,textvariable=self.var_roomno)
        roomno_txt.grid(row=1,column=1)
        
        roomtype=Label(label_frame,text='Room Type',font=('arial',12,'bold'),padx=7,pady=9)
        roomtype.grid(row=2,column=0,sticky=W)
        roomtype_txt=ttk.Entry(label_frame,font=('arial',12,'bold'),width=25,textvariable=self.var_roomtype)
        roomtype_txt.grid(row=2,column=1)
        
        
        #button frame
        btn_frame=Frame(label_frame,bd=0,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=460,height=60)
        
        add_btn=Button(btn_frame,text='Add',font=('arial',13,'bold'),command=self.add_data,bg='dark blue',fg='white',width=9)
        add_btn.grid(row=0,column=0,pady=6,padx=6)
        
        update_btn=Button(btn_frame,text='Update',font=('arial',13,'bold'),command=self.update_data,bg='dark blue',fg='white',width=9)
        update_btn.grid(row=0,column=1,pady=6,padx=6)
        
        delete_btn=Button(btn_frame,text='Delete',font=('arial',13,'bold'),command=self.delete_data,bg='dark blue',fg='white',width=9)
        delete_btn.grid(row=0,column=2,pady=6,padx=6)
        
        reset_btn=Button(btn_frame,text='Reset',font=('arial',13,'bold'),command=self.reset_data,bg='dark blue',fg='white',width=9)
        reset_btn.grid(row=0,column=3,pady=6,padx=6)
        
        #show details
        detail_frame=LabelFrame(self.root,text='Show Room Detail',bd=3,relief=RIDGE,font=('arial',13,'bold'))
        detail_frame.place(x=500,y=45,width=520,height=470)
        
        scroll_x=ttk.Scrollbar(detail_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detail_frame,orient=VERTICAL)
        
        self.detail_tabel=ttk.Treeview(detail_frame,columns=('floor','roomno','roomtype'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.detail_tabel.xview)
        scroll_y.config(command=self.detail_tabel.yview)
        
        self.detail_tabel.heading('floor',text='Floor')
        self.detail_tabel.heading('roomno',text='Room Number')
        self.detail_tabel.heading('roomtype',text='Room Type')
        
        self.detail_tabel['show']='headings'
        
        self.detail_tabel.column('floor',width=100)
        self.detail_tabel.column('roomno',width=100)
        self.detail_tabel.column('roomtype',width=100)
        
        self.detail_tabel.pack(fill=BOTH,expand=1)
        self.detail_tabel.bind("<ButtonRelease>",self.cursor_data)
        self.fetch_datach()
        
    
        
        
    def add_data(self):
         
        if self.var_floor.get()=='' or self.var_roomno.get()=='':
            messagebox.showerror('Error','All Field Are Required',parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='R1234',database='hotel')
                mycursor=conn.cursor()
                mycursor.execute('insert into detail values(%s,%s,%s)',(
                
                                                        self.var_floor.get(),
                                                        self.var_roomno.get(),
                                                        self.var_roomtype.get()
        
                
                
                                                                        ))
                conn.commit()
                self.fetch_datach()
                conn.close()
                messagebox.showinfo('Seccess','Data Added Succesfully',parent=self.root)
            
            except exception as e:
                messagebox.showwarning('Warning',f'Something went wrong:{str(e)}',parent=self.root)
                
   
   #fetch data
    def fetch_datach(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='R1234',database='hotel')
        mycursor=conn.cursor()
        mycursor.execute('select * from detail')
        row1=mycursor.fetchall()
        
        if len(row1)!=0:
            self.detail_tabel.delete(*self.detail_tabel.get_children())
            for i in row1:
                self.detail_tabel.insert('',END,values=i)
            conn.commit()
        conn.close()
        
    #cursor
    def cursor_data(self,event=''):
        data=self.detail_tabel.focus()
        content1=self.detail_tabel.item(data)
        row=content1['values']
        
        self.var_floor.set(row[0])
        self.var_roomno.set(row[1])
        self.var_roomtype.set(row[2])
        
    def update_data(self):
        if self.var_floor.get()=='' or self.var_roomno.get()=='':
            messagebox.showerror('Error','All Field Are Required',parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='R1234',database='hotel')
                mycursor=conn.cursor()
                mycursor.execute('update detail set floor=%s, room_type=%s where room_no=%s',(
                  
                                                                                                                 
                                                        self.var_floor.get(),
                                                        self.var_roomtype.get(),
                                                        self.var_roomno.get()
              
                                                                                          ))
                conn.commit()
                self.fetch_datach()
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
                mycursor.execute('delete from detail where room_no=%s',(self.var_roomno.get(),))
                
                conn.commit()
                self.fetch_datach()
                conn.close()
                messagebox.showinfo('Success','Your Data Succesfully Deleted')
        else:
            return
            
                
    #reset data
    def reset_data(self):
    
        self.var_floor.set('')
        self.var_roomno.set('')
        self.var_roomtype.set('')
        
        
    
        
        
    
        
        
        
        
        
        
        
        
if __name__=='__main__':
    root=Tk()
    obj=detail(root)
    root.mainloop()