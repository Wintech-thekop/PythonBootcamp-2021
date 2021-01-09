# GUIbasic.py

# tkinter = tk interface
from tkinter import *
from tkinter import ttk #ttk is theme of tk
import csv

# main program
GUI = Tk() #Tk() คือหน้าหลักโปรแกรม
GUI.title('โปรแกรมของฉัน')
GUI.geometry('500x300') # กว้าง 500dp , สูง 30dp

# font
FONT1 = ('Angsana New',20,'bold')
FONT2 = ('Angsana New',20)

# Title
L1 = ttk.Label(GUI,text='หัวข้อ', font=FONT1, foreground='green')
L1.pack()  # นำ L1 ไปติดกับโปรแกรมหลัก

# Text box 1
v_title = StringVar() # StringVar คือ ตัวแปรพิเศษใช้กับ GUI เท่านั้น 
E1 = ttk.Entry(GUI,textvariable=v_title, font=FONT2, width=30)
E1.pack()

# detail
L2 = ttk.Label(GUI,text='รายละเอียด', font=FONT1, foreground='green')
L2.pack()  # นำ L2 ไปติดกับโปรแกรมหลัก

# Text box2
v_detail = StringVar() # StringVar คือ ตัวแปรพิเศษใช้กับ GUI เท่านั้น
E2 = ttk.Entry(GUI,textvariable=v_detail, font=FONT2, width=50)
E2.pack()

# CSV file
def WritetoCSV(data):
    with open('data.csv','a',newline='',encoding='utf-8') as file: # With ใช้กับพวกเปิดไฟล์ หรือ Database
        fw = csv.writer(file) # fw = file writer
        fw.writerow(data)
    print('บันทึกไฟล์สำเร็จ')

# Button save
def Savebutton(event=None):
    print('กำลังบันทึกข้อมูล....')
    print(v_title.get()) #.get() คือการดึงข้อมูลจาก StringVar()
    print(v_detail.get()) #.get() คือการดึงข้อมูลจาก StringVar()
    data = [v_title.get(),v_detail.get()]
    WritetoCSV(data)
    # เคลียร์ข้อมูลใน Entry
    v_title.set('')
    v_detail.set('')
    E1.focus() #การนำ Curser อยู่ใน Entry แรก
    
E2.bind('<Return>',Savebutton)
# E2.bind() คือ การเช็คในช่องกรอที่2 ว่ามีการกดปุ่ม Enter หรือไม่ หากกดให้ทำการเรียกฟังก์ชั่น Savebutton

B1 = ttk.Button(GUI,text='Save',command=Savebutton)
B1.pack(ipadx=30, ipady=20, pady=20)  # นำ B1 ไปติดกับโปรแกรมหลัก
# ipadx คือ ระยะห่างภายในปุ่ม แนวแกน x
# ipady คือ ระยะห่างภายในปุ่ม แนวแกน y
# pady คือ ระยะห่างภายนอกปุ่ม ทั้งบนและล่าง แนวแกน y
GUI.mainloop() # GUI.mainloop() จาก GUI จะทำให้โปรแกรมรันตลอด



