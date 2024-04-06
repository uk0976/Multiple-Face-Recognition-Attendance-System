# importing required packages
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from Student import Student
from Train import Train
from Face_Detector import Face_Recognition
from Attendance import Attendance
from Developer import Developer
from Help import Help_Desk
import os
from time import strftime
from datetime import datetime

# Defining a class 
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")        #geometry of the window
        self.root.title("Face Recognition System")
        
        #First Image 
        image =Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Images\firstimage.jpeg")
        image = image.resize((530,130))
        self.photoimage = ImageTk.PhotoImage(image)

        first_label = Label(self.root,image=self.photoimage)
        first_label.place(x=0,y=0,width=530,height=130)

        #Second Image
        image1 =Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Images\second.jpeg")
        image1 = image1.resize((500,130))
        self.photoimage1 = ImageTk.PhotoImage(image1)

        first_label = Label(self.root,image=self.photoimage1)
        first_label.place(x=500,y=0,width=500,height=130)

        #Third Image
        image2 =Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Images\face_recog.jpeg")
        image2 = image2.resize((540,130))
        self.photoimage2 = ImageTk.PhotoImage(image2)

        first_label = Label(self.root,image=self.photoimage2)
        first_label.place(x=1000,y=0,width=540,height=130)

        #Background Image
        BackgroundImg =Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Images\background.webp")
        BackgroundImg = BackgroundImg.resize((1530,710))
        self.photoimage3 = ImageTk.PhotoImage(BackgroundImg)

        bg_img = Label(self.root,image=self.photoimage3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        #Title label of the project
        title_label = Label(bg_img,text="MULTIPLE FACE RECOGNITION ATTENDANCE SYSTEM",font=("Times new roman",35,"bold"),bg="light blue",fg="black")
        title_label.place(x=0,y=0,width=1530,height=45)

        #TIME LABEL
        def time():
            string = strftime("%H:%M:%S %p")
            lbl.config(text = string)
            lbl.after(1000, time)
        
        lbl = Label(title_label,font=("Times new roman",14,"bold"),bg="light blue",fg="black")
        lbl.place(x=0,y=0,width=110,height=40)
        time()

        #Student Button
        image3 = Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Images\stud_details.png")
        image3 = image3.resize((220,220))
        self.photoimage4 = ImageTk.PhotoImage(image3)

        btn1 = Button(bg_img,image=self.photoimage4,command=self.student_data,cursor="hand2")
        btn1.place(x=200,y=100,width=220,height=220)

        btn1_1 = Button(bg_img,text="Student Details",command=self.student_data,cursor="hand2",font=("Times new roman",15,"bold"),bg="light blue",fg="black")
        btn1_1.place(x=200,y=320,width=220,height=40)

        #Face Detection Button
        image4 = Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Images\face_detector.jpeg")
        image4 = image4.resize((220,220))
        self.photoimage5 = ImageTk.PhotoImage(image4)

        btn1 = Button(bg_img,image=self.photoimage5,cursor="hand2",command=self.fetch_data)
        btn1.place(x=500,y=100,width=220,height=220)

        btn1_1 = Button(bg_img,text="Face Detector",cursor="hand2",command=self.fetch_data,font=("Times new roman",15,"bold"),bg="light blue",fg="black")
        btn1_1.place(x=500,y=320,width=220,height=40)

        #Attendance Button
        image5 = Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Images\attendance.jpeg")
        image5 = image5.resize((220,220))
        self.photoimage6 = ImageTk.PhotoImage(image5)

        btn1 = Button(bg_img,image=self.photoimage6,cursor="hand2",command=self.attendance_data)
        btn1.place(x=800,y=100,width=220,height=220)

        btn1_1 = Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("Times new roman",15,"bold"),bg="light blue",fg="black")
        btn1_1.place(x=800,y=320,width=220,height=40)

        #Help Desk Button
        image6 = Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Images\help.jpeg")
        image6 = image6.resize((220,220))
        self.photoimage7 = ImageTk.PhotoImage(image6)

        btn1 = Button(bg_img,image=self.photoimage7,cursor="hand2",command=self.help_data)
        btn1.place(x=1100,y=100,width=220,height=220)

        btn1_1 = Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("Times new roman",15,"bold"),bg="light blue",fg="black")
        btn1_1.place(x=1100,y=320,width=220,height=40)

        #Training Button
        image7 = Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Images\trainm.jpeg")
        image7 = image7.resize((220,220))
        self.photoimage8 = ImageTk.PhotoImage(image7)

        btn1 = Button(bg_img,image=self.photoimage8,cursor="hand2",command=self.train_data)
        btn1.place(x=200,y=380,width=220,height=220)

        btn1_1 = Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("Times new roman",15,"bold"),bg="light blue",fg="black")
        btn1_1.place(x=200,y=600,width=220,height=40)

        #Photos Button
        image8 = Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Images\photos.jpg")
        image8 = image8.resize((220,220))
        self.photoimage9 = ImageTk.PhotoImage(image8)

        btn1 = Button(bg_img,image=self.photoimage9,cursor="hand2",command=self.open_image)
        btn1.place(x=500,y=380,width=220,height=220)

        btn1_1 = Button(bg_img,text="Student Photos",cursor="hand2",command=self.open_image,font=("Times new roman",15,"bold"),bg="light blue",fg="black")
        btn1_1.place(x=500,y=600,width=220,height=40)

        #Developer Button
        image9 = Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Images\developer_img.png")
        image9 = image9.resize((220,220))
        self.photoimage10 = ImageTk.PhotoImage(image9)

        btn1 = Button(bg_img,image=self.photoimage10,cursor="hand2",command=self.developer_data)
        btn1.place(x=800,y=380,width=220,height=220)

        btn1_1 = Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("Times new roman",15,"bold"),bg="light blue",fg="black")
        btn1_1.place(x=800,y=600,width=220,height=40)
        
        #Exit Button
        image10 = Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Images\exit_img.png")
        image10 = image10.resize((220,220))
        self.photoimage11 = ImageTk.PhotoImage(image10)

        btn1 = Button(bg_img,image=self.photoimage11,cursor="hand2",command=self.exit)
        btn1.place(x=1100,y=380,width=220,height=220)

        btn1_1 = Button(bg_img,text="Exit",cursor="hand2",command=self.exit,font=("Times new roman",15,"bold"),bg="light blue",fg="black")
        btn1_1.place(x=1100,y=600,width=220,height=40)

    def open_image(self):
        os.startfile(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Data")

    def exit(self):
        user_response=messagebox.askyesno("Face Recognition","Are You Sure To Exit The Project",parent=self.root)
        if user_response > 0:
            self.root.destroy()
        else:
            return    

    #FUNCTIONS BUTTONS
    def student_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    #FUNCTIONS BUTTONS
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    #FUNCTIONS BUTTONS
    def fetch_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window) 

    #FUNCTIONS BUTTONS
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    #FUNCTIONS BUTTONS
    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)                

    #FUNCTIONS BUTTONS
    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help_Desk(self.new_window) 



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()    