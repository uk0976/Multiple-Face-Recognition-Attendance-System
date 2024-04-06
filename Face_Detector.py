# importing required packages
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime
from cv2 import CascadeClassifier
import csv

# Defining a class 
class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")        #geometry of the window
        self.root.title("Face Recognition System")

        #Title label of the project
        title_label = Label(self.root,text="FACE RECOGNITION",font=("Times new roman",35,"bold"),bg="sky blue",fg="black")
        title_label.place(x=0,y=0,width=1530,height=45)

        #Images--1
        image_top =Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Images\face_detector1.jpg")
        image_top = image_top.resize((650,730))
        self.photoimage_top = ImageTk.PhotoImage(image_top)

        first_label = Label(self.root,image=self.photoimage_top)
        first_label.place(x=0,y=50,width=650,height=730)

        #images--2
        image_bottom =Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Images\facedetection.jpg")
        image_bottom = image_bottom.resize((950,730))
        self.photoimage_bottom = ImageTk.PhotoImage(image_bottom)

        first_label = Label(self.root,image=self.photoimage_bottom)
        first_label.place(x=650,y=50,width=950,height=730)


        # Button
        btn1_1 = Button(first_label,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("Times new roman",18,"bold"),bg="grey",fg="black")
        btn1_1.place(x=375,y=640,width=200,height=40)
    
    #ATTENDANCE FUNCTION
    def mark_attendance(self,v,i,r,c):
        with open(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Attendance.csv","r+",newline="\n") as f:
            mydataList = f.readlines()
            name_list = []
            for line in mydataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if((v not in name_list) and (i not in name_list) and (r not in name_list) and (c not in name_list)): 
                now = datetime.now()
                date_str = now.strftime("%d/%m/%Y")
                d1 = now.strftime("%H:%M:%S")   
                f.writelines(f"\n{v},{i},{r},{c},{date_str},{d1},Present")


    #Face Recognition Fuction
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors) 

            coordinates = []

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300))) 

                connection = mysql.connector.connect(host="localhost",username="root",password="13@Umerkhan",database="face_recognizer")
                my_cursor = connection.cursor()

                try:
                    my_cursor.execute("select Student_Name from student where Enrollment_No="+str(id))
                    i = my_cursor.fetchone()
                    if i:
                        i = "+".join(str(value) for value in i)
                    else:
                        i = "N/A"  # Provide a default value if no result is found
                except mysql.connector.Error as e:
                    print(f"Database Error: {e}")
                

                try:
                    my_cursor.execute("select Class from student where Enrollment_No="+str(id))
                    c = my_cursor.fetchone()
                    if c:
                        c = "+".join(str(value) for value in c)
                    else:
                        c = "N/A"  # Provide a default value if no result is found
                except mysql.connector.Error as e:
                    print(f"Database Error: {e}")
                

                try:
                    my_cursor.execute("select Roll_No from student where Enrollment_No="+str(id))
                    r = my_cursor.fetchone()
                    if r:
                        r = "+".join(str(value) for value in r)
                    else:
                        r = "N/A"  # Provide a default value if no result is found
                except mysql.connector.Error as e:
                    print(f"Database Error: {e}")

                try:
                    my_cursor.execute("select Enrollment_No from student where Enrollment_No="+str(id))
                    v = my_cursor.fetchone()
                    if v:
                        v = "+".join(str(value) for value in v)
                    else:
                        v = "N/A"  # Provide a default value if no result is found
                except mysql.connector.Error as e:
                    print(f"Database Error: {e}")    
                


                if confidence > 75:
                    cv2.putText(img,f"Student_ID : {v}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    cv2.putText(img,f"Student_Name : {i}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    cv2.putText(img,f"Roll_No : {r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    cv2.putText(img,f"Class : {c}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    self.mark_attendance(v,i,r,c)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coordinates = [x,y,w,h]

            return coordinates

        def recognize(img,clf,faceCascade):
            coordinates = draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade = cv2.CascadeClassifier(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Train.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)
            
            if cv2.waitKey(1)==13:
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()           
