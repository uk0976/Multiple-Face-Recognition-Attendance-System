# importing required packages
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

# Defining a class 
class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")        #geometry of the window
        self.root.title("Face Recognition System")

        #Variables
        self.var_Department = StringVar()
        self.var_Course = StringVar()
        self.var_Year = StringVar()
        self.var_Semester = StringVar()
        self.var_Enrollment_No = StringVar()
        self.var_Class = StringVar()
        self.var_Student_Name = StringVar()
        self.var_Roll_No = StringVar()
        self.var_Date_Of_Birth = StringVar()
        self.var_Gender = StringVar()
        self.var_Contact_No = StringVar()
        self.var_Address = StringVar()
        self.var_Coordinator = StringVar()
        self.var_Email_ID = StringVar()

        #First Image 
        image =Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Images\smart-attendance.jpg")
        image = image.resize((500,130))
        self.photoimage = ImageTk.PhotoImage(image)

        first_label = Label(self.root,image=self.photoimage)
        first_label.place(x=0,y=0,width=500,height=130)

        #Second Image
        image1 =Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Images\face-recognition.png")
        image1 = image1.resize((500,130))
        self.photoimage1 = ImageTk.PhotoImage(image1)

        first_label = Label(self.root,image=self.photoimage1)
        first_label.place(x=500,y=0,width=550,height=130)

        #Third Image
        image2 =Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Images\hqdefault.jpg")
        image2 = image2.resize((500,130))
        self.photoimage2 = ImageTk.PhotoImage(image2)

        first_label = Label(self.root,image=self.photoimage2)
        first_label.place(x=1000,y=0,width=550,height=130)

        #Background Image
        BackgroundImg =Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Images\background.webp")
        BackgroundImg = BackgroundImg.resize((1530,710))
        self.photoimage3 = ImageTk.PhotoImage(BackgroundImg)

        bg_img = Label(self.root,image=self.photoimage3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        #Title label of the project
        title_label = Label(bg_img,text="STUDENTS DETAILS MANAGEMENT",font=("Times new roman",35,"bold"),bg="white",fg="black")
        title_label.place(x=0,y=0,width=1530,height=45)


        #Making a Frame
        main_frame = Frame(bg_img,bd=2,bg="sky blue")
        main_frame.place(x=0,y=46,width=1530,height=610)

        #Left Label Frame
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=5,y=10,width=720,height=580)

        image_left =Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Images\photos.jpg")
        image_left = image_left.resize((780,130))
        self.photoimage_left = ImageTk.PhotoImage(image_left)

        first_label = Label(left_frame,image=self.photoimage_left)
        first_label.place(x=0,y=0,width=720,height=100)

        #Current course Label Frame
        current_course = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Info",font=("times new roman",12,"bold"))
        current_course.place(x=6,y=100,width=700,height=125)

        #Department Label
        dept_lbl = Label(current_course,text="Department :",font=("times new roman",12,"bold"),bg="white")
        dept_lbl.grid(row=0,column=0,padx=10,sticky=W)

        dept_combo = ttk.Combobox(current_course,textvariable=self.var_Department,font=("times new roman",12,"bold"),width=20,state="readonly")
        dept_combo["values"]=("Select Department","Computer ENG","Mechatronics","AIML ENG","Mechanical ENG","Civil ENG","Robotics")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course Label 
        course_lbl = Label(current_course,text="Course :",font=("times new roman",12,"bold"),bg="white")
        course_lbl.grid(row=0,column=2,padx=10,sticky=W)

        course_combo = ttk.Combobox(current_course,textvariable=self.var_Course,font=("times new roman",12,"bold"),width=20,state="readonly")
        course_combo["values"]=("Select Course","FY","SY","DSY","TY")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year Label
        year_lbl = Label(current_course,text="Year :",font=("times new roman",12,"bold"),bg="white")
        year_lbl.grid(row=1,column=0,padx=10,sticky=W)

        year_combo = ttk.Combobox(current_course,textvariable=self.var_Year,font=("times new roman",12,"bold"),width=20,state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester Label
        sem_lbl = Label(current_course,text="Semester :",font=("times new roman",12,"bold"),bg="white")
        sem_lbl.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo = ttk.Combobox(current_course,textvariable=self.var_Semester,font=("times new roman",12,"bold"),width=20,state="readonly")
        sem_combo["values"]=("Select Semester","1st Sem","2nd Sem","3rd Sem","4th Sem","5th Sem","6th Sem")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class Student Information label frame
        class_stud = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Info",font=("times new roman",12,"bold"))
        class_stud.place(x=6,y=230,width=700,height=320)

        #Student ID Label
        stud_id = Label(class_stud,text="Student ID :",font=("times new roman",12,"bold"),bg="white")
        stud_id.grid(row=0,column=0,padx=10,sticky=W)

        stud_entry = ttk.Entry(class_stud,width=20,textvariable=self.var_Enrollment_No,font=("times new roman",12,"bold"))
        stud_entry.grid(row=0,column=1,padx=10,sticky=W)
        
        #Class Label
        class_lbl = Label(class_stud,text="Class :",font=("times new roman",12,"bold"),bg="white")
        class_lbl.grid(row=0,column=2,padx=10,sticky=W)

        class_entry = ttk.Entry(class_stud,width=20,textvariable=self.var_Class,font=("times new roman",12,"bold"))
        class_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Student Name Label
        stud_name = Label(class_stud,text="Student Name :",font=("times new roman",12,"bold"),bg="white")
        stud_name.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        stud_name_entry = ttk.Entry(class_stud,width=20,textvariable=self.var_Student_Name,font=("times new roman",12,"bold"))
        stud_name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Student Roll No Label
        roll_no = Label(class_stud,text="Roll No :",font=("times new roman",12,"bold"),bg="white")
        roll_no.grid(row=1,column=2,padx=10,sticky=W)

        roll_no_entry = ttk.Entry(class_stud,width=20,textvariable=self.var_Roll_No,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Sudent Gender Label
        stud_gender = Label(class_stud,text="Gender :",font=("times new roman",12,"bold"),bg="white")
        stud_gender.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo = ttk.Combobox(class_stud,textvariable=self.var_Gender,font=("times new roman",12,"bold"),width=18,state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Other..")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Date Of Birth Label
        stud_DOB = Label(class_stud,text="Date Of Birth :",font=("times new roman",12,"bold"),bg="white")
        stud_DOB.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        stud_DOB_entry = ttk.Entry(class_stud,width=20,textvariable=self.var_Date_Of_Birth,font=("times new roman",12,"bold"))
        stud_DOB_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Phone Number Label
        stud_phone = Label(class_stud,text="Contact No :",font=("times new roman",12,"bold"),bg="white")
        stud_phone.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        stud_phone_entry = ttk.Entry(class_stud,width=20,textvariable=self.var_Contact_No,font=("times new roman",12,"bold"))
        stud_phone_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Teacher Name Label
        teacher = Label(class_stud,text="Coordinator :",font=("times new roman",12,"bold"),bg="white")
        teacher.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        teacher_entry = ttk.Entry(class_stud,width=20,textvariable = self.var_Coordinator,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Address Label
        address = Label(class_stud,text="Address :",font=("times new roman",12,"bold"),bg="white")
        address.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry = ttk.Entry(class_stud,width=20,textvariable=self.var_Address,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Email Label
        email= Label(class_stud,text="Email ID :",font=("times new roman",12,"bold"),bg="white")
        email.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        email_entry = ttk.Entry(class_stud,width=20,textvariable=self.var_Email_ID,font=("times new roman",12,"bold"))
        email_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #Radio Buttons
        self.var_radio1 = StringVar()
        radio_btn1 = ttk.Radiobutton(class_stud,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radio_btn1.grid(row=5,column=0)

        radio_btn2 = ttk.Radiobutton(class_stud,variable=self.var_radio1,text="No Photo Sample",value="No")
        radio_btn2.grid(row=5,column=2)

        #Button Frame
        btn_frame=Frame(class_stud,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=2,y=200,width=690,height=50)

        #Save Button
        save_btn = Button(btn_frame,text="Save",command=self.add_data,width=18,font=("times new roman",12,"bold"),bg="sky blue")
        save_btn.grid(row=0,column=0)

        #Update Button
        update_btn = Button(btn_frame,text="Update",command=self.update_data,width=18,font=("times new roman",12,"bold"),bg="sky blue")
        update_btn.grid(row=0,column=1)

        #Delete Button
        delete_btn = Button(btn_frame,text="Delete",command=self.delete_data,width=18,font=("times new roman",12,"bold"),bg="sky blue")
        delete_btn.grid(row=0,column=2)

        #Reset Button
        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=18,font=("times new roman",12,"bold"),bg="sky blue")
        reset_btn.grid(row=0,column=3)

        #Another Frame
        btn_frame1=Frame(class_stud,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=2,y=240,width=690,height=40)


        #Take Photo Sample Button
        take_photo_btn = Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=37,font=("times new roman",12,"bold"),bg="sky blue")
        take_photo_btn.grid(row=0,column=0)

        #Update Photo Sample Button
        update_photo_btn = Button(btn_frame1,text="Update Photo Sample",width=37,font=("times new roman",12,"bold"),bg="sky blue")
        update_photo_btn.grid(row=0,column=1)


        #Right Label Frame
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=740,y=10,width=770,height=580)

        image_right =Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Images\attend.jpeg")
        image_right = image_right.resize((780,130))
        self.photoimage_right = ImageTk.PhotoImage(image_right)

        first_label1 = Label(right_frame,image=self.photoimage_right)
        first_label1.place(x=0,y=0,width=765,height=100)

        #_____________SEARCHING SYSTEM_____________#
        search_stud = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_stud.place(x=0,y=100,width=765,height=70)

        #Search Label
        search_lbl = Label(search_stud,text="Search By :",font=("times new roman",15,"bold"),bg="sky blue")
        search_lbl.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        #Combo Box Search
        search_combo = ttk.Combobox(search_stud,font=("times new roman",15,"bold"),width=12,state="readonly")
        search_combo["values"]=("Select","Roll_No","Contact_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #EntryFill
        entry_fill = ttk.Entry(search_stud,width=12,font=("times new roman",15,"bold"))
        entry_fill.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        #Search Buttons
        search_btn = Button(search_stud,text="Search",width=13,font=("times new roman",15,"bold"),bg="sky blue")
        search_btn.grid(row=0,column=3,padx=5)

        showall_btn = Button(search_stud,text="Show All",width=13,font=("times new roman",15,"bold"),bg="sky blue")
        showall_btn.grid(row=0,column=4,padx=5)
        
        #Table Frame
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=0,y=175,width=765,height=380)

        #Scroll Bars
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table  = ttk.Treeview(table_frame,columns=("Department","Course","Year","Semester","Student ID","Class","Student Name",
                                                                "Roll No","Date Of Birth","Gender","Contact No","Address","Coordinator","Email ID"),
                                                                xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        #Scrolling method
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        #Assigning the Headings
        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("Student ID",text="Student ID")
        self.student_table.heading("Class",text="Class")
        self.student_table.heading("Student Name",text="Student Name")
        self.student_table.heading("Roll No",text="Roll No")
        self.student_table.heading("Date Of Birth",text="Date Of Birth")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Contact No",text="Contact No")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Coordinator",text="Coordinator")
        self.student_table.heading("Email ID",text="Email ID")
        self.student_table["show"]="headings"

        #Setting width of each column
        self.student_table.column("Department",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("Student ID",width=100)
        self.student_table.column("Class",width=100)
        self.student_table.column("Student Name",width=100)
        self.student_table.column("Roll No",width=100)
        self.student_table.column("Date Of Birth",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Contact No",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Coordinator",width=100)
        self.student_table.column("Email ID",width=100)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    #Function Declaration
    def add_data(self):
        if self.var_Department.get()=="Select Department" or self.var_Student_Name.get()=="" or self.var_Enrollment_No.get()=="":
            messagebox.showerror("Error","All Fills Are Required",parent=self.root)
        else:
            try:            
                connection = mysql.connector.connect(host="localhost",username="root",password="13@Umerkhan",database="face_recognizer")
                my_cursor = connection.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (self.var_Department.get(),
                                 self.var_Course.get(),
                                 self.var_Year.get(),
                                 self.var_Semester.get(),
                                 self.var_Enrollment_No.get(),
                                 self.var_Class.get(),
                                 self.var_Student_Name.get(),
                                 self.var_Roll_No.get(),
                                 self.var_Date_Of_Birth.get(),
                                 self.var_Gender.get(),
                                 self.var_Contact_No.get(),
                                 self.var_Address.get(),
                                 self.var_Coordinator.get(),
                                 self.var_Email_ID.get()
                                ))
                
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo("Success","Students Details have been Added Successfully",parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    #FETCHING FUNCTION
    def fetch_data(self):
        connection = mysql.connector.connect(host="localhost",username="root",password="13@Umerkhan",database="face_recognizer")
        my_cursor = connection.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
             
            for i in data:
                self.student_table.insert("",END,values=i)
            connection.commit()
        connection.close()        


    #GET CURSOR Function
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_Department.set(data[0]),
        self.var_Course.set(data[1]),
        self.var_Year.set(data[2]),
        self.var_Semester.set(data[3]),
        self.var_Enrollment_No.set(data[4]),
        self.var_Class.set(data[5]),
        self.var_Student_Name.set(data[6]),
        self.var_Roll_No.set(data[7]),
        self.var_Date_Of_Birth.set(data[8]),
        self.var_Gender.set(data[9]),
        self.var_Contact_No.set(data[10]),
        self.var_Address.set(data[11]),
        self.var_Coordinator.set(data[12]),
        self.var_Email_ID.set(data[13])
            

    #UPDATE FUNCTION
    def update_data(self):
        if self.var_Department.get()=="Select Department" or self.var_Student_Name.get()=="" or self.var_Enrollment_No.get()=="":
            messagebox.showerror("Error","All Fills Are Required",parent=self.root)

        else:
            try:
                update = messagebox.askyesno("Update","Do you really want to update details",parent = self.root)
                if update > 0:
                    connection = mysql.connector.connect(host="localhost",username="root",password="13@Umerkhan",database="face_recognizer")
                    my_cursor = connection.cursor()
                    my_cursor.execute("UPDATE student set Department=%s,Course=%s,Year=%s,Semester=%s,Class=%s,Student_Name=%s,Roll_No=%s,Date_Of_Birth=%s,Gender=%s,Contact_No=%s,Address=%s,Coordinator=%s,Email_ID=%s where Enrollment_No=%s",
                                       self.var_Department.get(),
                                       self.var_Course.get(),
                                       self.var_Year.get(),
                                       self.var_Semester.get(),
                                       self.var_Class.get(),
                                       self.var_Student_Name.get(),
                                       self.var_Roll_No.get(),
                                       self.var_Date_Of_Birth.get(),
                                       self.var_Gender.get(),
                                       self.var_Contact_No.get(),
                                       self.var_Address.get(),
                                       self.var_Coordinator.get(),
                                       self.var_Email_ID.get(),
                                       self.var_Enrollment_No.get())

                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Details Updated Successfully",parent=self.root)
                connection.commit()
                self.fetch_data()
                connection.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)           

    #DELETE FUNCTION
    def delete_data(self):
        if self.var_Enrollment_No.get()=="":
            messagebox.showerror("Error","Enrollment No must be required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete","Do you want to delete the details",parent=self.root)
                if delete > 0:
                    connection = mysql.connector.connect(host="localhost",username="root",password="13@Umerkhan",database="face_recognizer")
                    my_cursor = connection.cursor()
                    sql = "delete from student where Enrollment_No=%s"
                    val = (self.var_Enrollment_No.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return    
                
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo("Delete","Details Deleted Succesfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)           

    #RESET FUNCTION
    def reset_data(self):
        self.var_Department.set("Select Department"),
        self.var_Course.set("Select Course"),
        self.var_Year.set("Select Year"),
        self.var_Semester.set("Select Semester"),
        self.var_Enrollment_No.set(""),
        self.var_Class.set(""),
        self.var_Student_Name.set(""),
        self.var_Roll_No.set(""),
        self.var_Date_Of_Birth.set(""),
        self.var_Gender.set("Select Gender"),
        self.var_Contact_No.set(""),
        self.var_Address.set(""),
        self.var_Coordinator.set(""),
        self.var_Email_ID.set("")

    #Generate Dataset and Take samples
    def generate_dataset(self):
        if self.var_Department.get()=="Select Department" or self.var_Student_Name.get()=="" or self.var_Enrollment_No.get()=="":
            messagebox.showerror("Error","All Fills Are Required",parent=self.root)

        else:
            try:
                connection = mysql.connector.connect(host="localhost",username="root",password="13@Umerkhan",database="face_recognizer")
                my_cursor = connection.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id+=1  
                my_cursor.execute("UPDATE student set Department=%s,Course=%s,Year=%s,Semester=%s,Class=%s,Student_Name=%s,Roll_No=%s,Date_Of_Birth=%s,Gender=%s,Contact_No=%s,Address=%s,Coordinator=%s,Email_ID=%s where Enrollment_No=%s",(
                                       self.var_Department.get(),
                                       self.var_Course.get(),
                                       self.var_Year.get(),
                                       self.var_Semester.get(),
                                       self.var_Class.get(),
                                       self.var_Student_Name.get(),
                                       self.var_Roll_No.get(),
                                       self.var_Date_Of_Birth.get(),
                                       self.var_Gender.get(),
                                       self.var_Contact_No.get(),
                                       self.var_Address.get(),
                                       self.var_Coordinator.get(),
                                       self.var_Email_ID.get(),
                                       self.var_Enrollment_No.get()==id+1
                                       ))
                connection.commit()
                self.fetch_data()
                self.reset_data()
                connection.close()


                #LOAD PRE DEFINED FRONTAL FACE OPENCV
                face_classifier = cv2.CascadeClassifier(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5) #Scaling factor=1.3 // Minimum neighbor=5

                    for(x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Data\user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data Set Completed!!!")

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)     

                        

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()         