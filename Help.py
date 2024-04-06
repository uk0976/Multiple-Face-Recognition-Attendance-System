# importing required packages
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

# Defining a class 
class Help_Desk:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")        #geometry of the window
        self.root.title("Face Recognition System")

        #Title label of the project
        title_label = Label(self.root,text="HELP DESK",font=("Times new roman",35,"bold"),bg="sky blue",fg="black")
        title_label.place(x=0,y=0,width=1530,height=45)

        #Background Image
        BackgroundImg =Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        BackgroundImg = BackgroundImg.resize((1530,800))
        self.photoimage3 = ImageTk.PhotoImage(BackgroundImg)

        bg_img = Label(self.root,image=self.photoimage3)
        bg_img.place(x=0,y=50,width=1530,height=800)

        #Email Label
        email_lbl = Label(self.root,text="Email : umerkhandoctor1@gmail.com",font=("Times new roman",35,"bold"),bg="white",fg="black")
        email_lbl.place(x=250,y=80,width=1000,height=45)





if __name__ == "__main__":
    root=Tk()
    obj=Help_Desk(root)
    root.mainloop()               