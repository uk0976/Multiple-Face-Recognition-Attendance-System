# importing required packages
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


my_data = []

# Defining a class 
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")        #geometry of the window
        self.root.title("Face Recognition System")

        #TEXT VARIABLES
        self.var_student_id=StringVar()
        self.var_name=StringVar()
        self.var_roll_no=StringVar()
        self.var_class=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_status=StringVar()
        

        #First Image 
        image =Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Images\smart-attendance.jpg")
        image = image.resize((800,200))
        self.photoimage = ImageTk.PhotoImage(image)

        first_label = Label(self.root,image=self.photoimage)
        first_label.place(x=0,y=0,width=760,height=200)

        #Second Image
        image1 =Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Images\iStock-182059956_18390_t12.jpg")
        image1 = image1.resize((800,200))
        self.photoimage1 = ImageTk.PhotoImage(image1)

        first_label = Label(self.root,image=self.photoimage1)
        first_label.place(x=770,y=0,width=760,height=200)

        #Background Image
        BackgroundImg =Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Images\bg1.jpg")
        BackgroundImg = BackgroundImg.resize((1530,720))
        self.photoimage3 = ImageTk.PhotoImage(BackgroundImg)

        bg_img = Label(self.root,image=self.photoimage3)
        bg_img.place(x=0,y=130,width=1530,height=720)

        #Title label of the project
        title_label = Label(bg_img,text="ATTENDANCE",font=("Times new roman",35,"bold"),bg="dark blue",fg="white")
        title_label.place(x=0,y=0,width=1530,height=45)

        #Making a Frame
        main_frame = Frame(bg_img,bd=2,bg="sky blue")
        main_frame.place(x=0,y=46,width=1530,height=610)

        #Left Label Frame
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="ATTENDANCE DETAILS ",font=("times new roman",12,"bold"))
        left_frame.place(x=0,y=0,width=760,height=600)

        image_left =Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Images\KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
        image_left = image_left.resize((800,150))
        self.photoimage_left = ImageTk.PhotoImage(image_left)

        first_label = Label(left_frame,image=self.photoimage_left)
        first_label.place(x=0,y=0,width=760,height=150)

        #Another Frame
        l_frame = Frame(bg_img,bd=2,relief=RIDGE,bg="light blue")
        l_frame.place(x=0,y=220,width=760,height=300)

        #Labels and Entry
        #Student ID
        Student_id = Label(l_frame,text="Student ID :",font=("times new roman",13,"bold","underline"),bg="light blue")
        Student_id.grid(row=0,column=0,padx=15,pady=10)

        Student_entry = ttk.Entry(l_frame,width=20,textvariable=self.var_student_id,font=("times new roman",13,"bold"))
        Student_entry.grid(row=0,column=1,padx=15,pady=10)

        #Name Label
        name_id = Label(l_frame,text="Name :",font=("times new roman",13,"bold","underline"),bg="light blue")
        name_id.grid(row=0,column=2,padx=15,pady=10)

        name_entry = ttk.Entry(l_frame,width=20,textvariable=self.var_name,font=("times new roman",13,"bold"))
        name_entry.grid(row=0,column=3,padx=15,pady=10)

        #Roll No Label
        roll_id = Label(l_frame,text="Roll No :",font=("times new roman",13,"bold","underline"),bg="light blue")
        roll_id.grid(row=1,column=0,padx=15,pady=10)

        roll_entry = ttk.Entry(l_frame,width=20,textvariable=self.var_roll_no,font=("times new roman",13,"bold"))
        roll_entry.grid(row=1,column=1,padx=15,pady=10)

        #Class Label
        class_id = Label(l_frame,text="Class :",font=("times new roman",13,"bold","underline"),bg="light blue")
        class_id.grid(row=1,column=2,padx=15,pady=10)

        class_entry = ttk.Entry(l_frame,width=20,textvariable=self.var_class,font=("times new roman",13,"bold"))
        class_entry.grid(row=1,column=3,padx=15,pady=10)

        #Time Label
        time_id = Label(l_frame,text="Time :",font=("times new roman",13,"bold","underline"),bg="light blue")
        time_id.grid(row=2,column=0,padx=15,pady=10)

        time_entry = ttk.Entry(l_frame,width=20,textvariable=self.var_time,font=("times new roman",13,"bold"))
        time_entry.grid(row=2,column=1,padx=15,pady=10)

        #Date Label
        date_id = Label(l_frame,text="Date :",font=("times new roman",13,"bold","underline"),bg="light blue")
        date_id.grid(row=2,column=2,padx=15,pady=10)

        date_entry = ttk.Entry(l_frame,width=20,textvariable=self.var_date,font=("times new roman",13,"bold"))
        date_entry.grid(row=2,column=3,padx=15,pady=10)

        #Status Combo Box
        status_lbl = Label(l_frame,text="Attendance Status :",font=("times new roman",13,"bold","underline"),bg="light blue")
        status_lbl.grid(row=3,column=0,padx=10,pady=10)

        self.status_combo = ttk.Combobox(l_frame,font=("times new roman",12,"bold"),width=20,textvariable=self.var_status,state="readonly")
        self.status_combo["values"]=("Select Status","Present","Absent")
        self.status_combo.current(0)
        self.status_combo.grid(row=3,column=1,padx=1,pady=10)

        #Button Frame
        btn_frame=Frame(l_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=755,height=90)

        #Import Button
        import_btn = Button(btn_frame,text="Import-csv",width=40,command=self.import_csv,font=("times new roman",12,"bold"),bg="sky blue",fg="black")
        import_btn.grid(row=0,column=0,padx=2,pady=4)

        #Export Button
        export_btn = Button(btn_frame,text="Export-csv",width=40,command=self.export_csv,font=("times new roman",12,"bold"),bg="sky blue",fg="black")
        export_btn.grid(row=0,column=1,padx=2,pady=4)

        #Update Button
        update_btn = Button(btn_frame,text="Update",width=40,font=("times new roman",12,"bold"),bg="sky blue",fg="black")
        update_btn.grid(row=1,column=0,padx=2,pady=4)

        #Reset Button
        reset_btn = Button(btn_frame,text="Reset",width=40,command=self.reset_data,font=("times new roman",12,"bold"),bg="sky blue",fg="black")
        reset_btn.grid(row=1,column=1,padx=2,pady=4)

        #Down Image
        image_down =Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Images\university.jpg")
        image_down = image_down.resize((800,150))
        self.photoimage_down = ImageTk.PhotoImage(image_down)

        first_label = Label(left_frame,image=self.photoimage_down)
        first_label.place(x=0,y=450,width=760,height=150)


        #Right Label Frame
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="ATTENDANCE",font=("times new roman",12,"bold"))
        right_frame.place(x=760,y=0,width=760,height=600)

        #Table Frame
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="light blue")
        table_frame.place(x=0,y=0,width=755,height=450)

        #Down Image
        image_down1 =Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\Mega Project\Images\Team-Management-Software-Development.jpg")
        image_down1 = image_down1.resize((800,150))
        self.photoimage_down1 = ImageTk.PhotoImage(image_down1)

        first_label1 = Label(right_frame,image=self.photoimage_down1)
        first_label1.place(x=0,y=450,width=760,height=150)

        
        #Scroll Bar and Table
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReport_table = ttk.Treeview(table_frame,column=("Student ID","Name","Roll No","Class","Date","Time","Attendance Status"),
                                                   xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReport_table.xview)
        scroll_y.config(command=self.AttendanceReport_table.yview)
        
        #Headings
        self.AttendanceReport_table.heading("Student ID",text="Student ID")
        self.AttendanceReport_table.heading("Name",text="Student Name")
        self.AttendanceReport_table.heading("Roll No",text="Roll No")
        self.AttendanceReport_table.heading("Class",text="Class")
        self.AttendanceReport_table.heading("Time",text="Time")
        self.AttendanceReport_table.heading("Date",text="Date")
        self.AttendanceReport_table.heading("Attendance Status",text="Attendance")
        self.AttendanceReport_table["show"]="headings"

        #Settings Width
        self.AttendanceReport_table.column("Student ID",width=100)
        self.AttendanceReport_table.column("Name",width=100)
        self.AttendanceReport_table.column("Roll No",width=100)
        self.AttendanceReport_table.column("Class",width=100)
        self.AttendanceReport_table.column("Time",width=100)
        self.AttendanceReport_table.column("Date",width=100)
        self.AttendanceReport_table.column("Attendance Status",width=100)

        self.AttendanceReport_table.pack(fill=BOTH,expand=1)
        self.AttendanceReport_table.bind("<ButtonRelease>",self.get_cursor)

    #FETCH DATA FUNCTION 
    def fetchData(self,rows):
        self.AttendanceReport_table.delete(*self.AttendanceReport_table.get_children())
        for i in rows:
            self.AttendanceReport_table.insert("",END,values=i)

    #IMPORT CSV FUNCTION FOR BUTTON
    def import_csv(self):
        global my_data
        my_data.clear()
        filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=filetypes, parent=self.root)
        with open(fln) as my_file:
            csv_read = csv.reader(my_file,delimiter=",")
            for i in csv_read:
                my_data.append(i)

            self.fetchData(my_data)    
    
    #EXPORT CSV FUNCTION FOR BUTTON
    def export_csv(self):
        try:
            if len(my_data)<1:
                messagebox.showerror("ERROR","No Data Found To Export",parent=self.root)
                return False
            filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=filetypes, parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in my_data:
                    exp_write.writerow(i)
                messagebox.showinfo("RESULT","Data Exported to "+os.path.basename(fln)+"Successfully")

        except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    #showing attributes
    def get_cursor(self,event=""):
        cursor_row = self.AttendanceReport_table.focus()
        content = self.AttendanceReport_table.item(cursor_row)
        rows = content["values"]
        self.var_student_id.set(rows[0])
        self.var_name.set(rows[1])
        self.var_roll_no.set(rows[2])
        self.var_class.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_status.set(rows[6])

    #RESET FUNCTION FOR BUTTON
    def reset_data(self):
        self.var_student_id.set("")
        self.var_name.set("")
        self.var_roll_no.set("")
        self.var_class.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_status.set("")


if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()         