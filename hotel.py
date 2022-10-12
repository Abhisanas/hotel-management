from  tkinter import *
from PIL import Image,ImageTk
from customer import customer_win
from room import room
from detail import detail



class hotelmanagementsystem:
    def __init__(self,root):
        self.root=root
        self.root.title('Hotel Management System')
        self.root.geometry('1400x710+0+0')
    
        
        title_lbl=Label(self.root,text='Hotel Management System',font=('areal',25,'bold'),bg='white',fg='blue',bd=4,relief=RIDGE)
        title_lbl.place(x=0,y=0,relwidth=1)
        
        #main frame
        main_frame=Frame(self.root,bd=2,relief=RIDGE)
        main_frame.place(x=0,y=45,width=1367,height=660)
        
        img1=Image.open('view.jpg')
        img1=img1.resize((1220,652),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)
        img1_lbl=Label(main_frame,image=self.photo1,bd=2,relief=RIDGE)
        img1_lbl.place(x=150,y=2,width=1220,height=652)
        
        #button frame
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE,bg='white')
        btn_frame.place(x=0,y=2,width=150,height=650)
        
        customer_btn=Button(btn_frame,text='Customer',font=('arial',14,'bold'),command=self.customer_data,bg='blue',fg='white',bd=0,cursor='hand2',width=11)
        customer_btn.grid(row=0,column=0,pady=10,padx=3)
        
        customer_btn=Button(btn_frame,text='Room',font=('arial',14,'bold'),command=self.room_data,bg='blue',fg='white',bd=0,cursor='hand2',width=11)
        customer_btn.grid(row=1,column=0,pady=10,padx=3)
        
        customer_btn=Button(btn_frame,text='Details',font=('arial',14,'bold'),command=self.detail_data,bg='blue',fg='white',bd=0,cursor='hand2',width=11)
        customer_btn.grid(row=2,column=0,pady=10,padx=3)
        
        customer_btn=Button(btn_frame,text='Report',font=('arial',14,'bold'),bg='blue',fg='white',bd=0,cursor='hand2',width=11)
        customer_btn.grid(row=3,column=0,pady=10,padx=3)
        
        customer_btn=Button(btn_frame,text='Logout',font=('arial',14,'bold'),command=self.logout,bg='blue',fg='white',bd=0,cursor='hand2',width=11)
        customer_btn.grid(row=4,column=0,pady=10,padx=3)
        
        
    #customer
    def customer_data(self):
        self.new_win=Toplevel(self.root)
        self.app=customer_win(self.new_win)
        
    #room
    def room_data(self):
        self.new_win1=Toplevel(self.root)
        self.app1=room(self.new_win1)
        
    #detail
    def detail_data(self):
        self.new_win2=Toplevel(self.root)
        self.app2=detail(self.new_win2)
        
    #logout
    def logout(self):
        root.destroy()
        
       
        
        
        
if __name__=='__main__':
    root=Tk()
    obj=hotelmanagementsystem(root)
    root.mainloop()