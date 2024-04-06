# importing required packages
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from cv2 import CascadeClassifier

# Defining a class 
class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")        #geometry of the window
        self.root.title("Face Recognition System")

        #Title label of the project
        title_label = Label(self.root,text="TRAIN DATA SET",font=("Times new roman",35,"bold"),bg="sky blue",fg="black")
        title_label.place(x=0,y=0,width=1530,height=45)

        #Top Image
        image_top =Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Images\photos.jpg")
        image_top = image_top.resize((1530,325))
        self.photoimage_top = ImageTk.PhotoImage(image_top)

        first_label = Label(self.root,image=self.photoimage_top)
        first_label.place(x=0,y=50,width=1530,height=325)

        #Bottom Image
        image_bottom =Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Images\smart-attendance.jpg")
        image_bottom = image_bottom.resize((1530,370))
        self.photoimage_bottom = ImageTk.PhotoImage(image_bottom)

        first_label = Label(self.root,image=self.photoimage_bottom)
        first_label.place(x=0,y=420,width=1530,height=370)

        #Train Data Button
        btn1_1 = Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("Times new roman",20,"bold"),bg="grey",fg="black")
        btn1_1.place(x=0,y=375,width=1530,height=45)

    #Defining the class for training data with algorithm    
    def train_classifier(self):
        data_dir = (r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert("L")   #GRAY SCALE IMAGE CONVERSION
            image_np = np.array(img,"uint8")
            id = int(os.path.split(image)[1].split('.')[1])


            faces.append(image_np)
            ids.append(id)
            cv2.imshow("Training ",image_np)
            cv2.waitKey(1)==13
        
        ids = np.array(ids)
        
        #TRAIN THE CLASSIFIER AND SAVE
        clf = cv2.face_LBPHFaceRecognizer.create()
        clf.train(faces,ids)
        clf.write(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Train.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Results","Training Completed!!")




if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()     