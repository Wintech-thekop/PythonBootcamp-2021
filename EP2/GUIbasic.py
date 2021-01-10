# GUIbasic.py

# tkinter = tk interface
from tkinter import *
from tkinter import ttk, messagebox #ttk is theme of tk
import csv
import random


# main program
GUI = Tk() #Tk() คือหน้าหลักโปรแกรม
GUI.title('โปรแกรมของฉัน')
GUI.geometry('700x700') # กว้าง 700dp , สูง 700dp

# font
FONT1 = ('Angsana New',20,'bold')
FONT2 = ('Angsana New',20)
FONT3 = ('Angsana New',16)


# Tab Menu
Tab = ttk.Notebook(GUI)

T1 = Frame(Tab)
T2 = Frame(Tab)

Tab.add(T1,text='Add')
Tab.add(T2,text='Flash Card')

Tab.pack(fill=BOTH, expand=1)


'''&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& Tab1 Area &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'''

# Title
L1 = ttk.Label(T1,text='หัวข้อ', font=FONT1, foreground='green')
L1.pack()  # นำ L1 ไปติดกับโปรแกรมหลัก

# Text box 1
v_title = StringVar() # StringVar คือ ตัวแปรพิเศษใช้กับ T1 เท่านั้น 
E1 = ttk.Entry(T1,textvariable=v_title, font=FONT2, width=30)
E1.pack()

# detail
L2 = ttk.Label(T1,text='รายละเอียด', font=FONT1, foreground='green')
L2.pack()  # นำ L2 ไปติดกับโปรแกรมหลัก

# Text box2
v_detail = StringVar() # StringVar คือ ตัวแปรพิเศษใช้กับ T1 เท่านั้น
E2 = ttk.Entry(T1,textvariable=v_detail, font=FONT2, width=50)
E2.pack()

# CSV file
def WritetoCSV(data):
    with open('data.csv','a',newline='',encoding='utf-8') as file: # With ใช้กับพวกเปิดไฟล์ หรือ Database
        fw = csv.writer(file) # fw = file writer
        fw.writerow(data)
    print('บันทึกไฟล์สำเร็จ')

def ReadCSV():
    with open('data.csv',newline='',encoding='utf-8') as file:
        fr = csv.reader(file) # fr = file reader
        data = list(fr)
    print('อ่านไฟล์สำเร็จ')    
    return data    

# สร้างฟังก์ชั่นอัพเดท Table
def Updatetable():
    table.delete(*table.get_children()) # เคลียร์ข้อมูลชุดเก่าก่อนจำอัพเดทชุดใหม่เข้าไป
    alldata = ReadCSV()
    for row in alldata:
        table.insert('','end',value=row) 

# Button save
def Savebutton(event=None):
    print('กำลังบันทึกข้อมูล....')
    print(v_title.get()) #.get() คือการดึงข้อมูลจาก StringVar()
    print(v_detail.get()) #.get() คือการดึงข้อมูลจาก StringVar()
    
    if v_title.get() != '' and v_detail.get() != '':  
        data = [v_title.get(),v_detail.get()]
        WritetoCSV(data)
        v_title.set('') # เคลียร์ข้อมูลใน Entry Title
        v_detail.set('') # เคลียร์ข้อมูลใน Entry Detail
        E1.focus() #การนำ Curser อยู่ใน Entry แรก
        Updatetable() 
        global allquestion
        allquestion = ReadCSV()
    
E2.bind('<Return>',Savebutton)
# E2.bind() คือ การเช็คในช่องกรอที่2 ว่ามีการกดปุ่ม Enter หรือไม่ หากกดให้ทำการเรียกฟังก์ชั่น Savebutton

B1 = ttk.Button(T1,text='Save',command=Savebutton)
B1.pack(ipadx=30, ipady=20, pady=20)  # นำ B1 ไปติดกับโปรแกรมหลัก
# ipadx คือ ระยะห่างภายในปุ่ม แนวแกน x
# ipady คือ ระยะห่างภายในปุ่ม แนวแกน y
# pady คือ ระยะห่างภายนอกปุ่ม ทั้งบนและล่าง แนวแกน y

# table

# setting font for Table
style = ttk.Style()
style.configure('Treeview.Heading',font=('Angsana New',20))
style.configure('Treeview',font=('Angsana New',18),rowheight=30)



header = ['Title','Detail']

table = ttk.Treeview(T1,height=10,column=header,show='headings')
#table.place(x=20,y=280)
table.pack()

table.heading('Title',text='หัวข้อ') # โชว์คำว่า"หัวข้อ"ที่คอลัมน์ Title
table.column('Title',width=200) # ปรับความกว้าง
table.heading('Detail',text='รายละเอียด') # โชว์คำว่า"รายละเอียด"ที่คอลัมน์ Title
table.column('Detail',width=460) # ปรับความกว้าง

'''
# Test insert data
row = ['GUI คืออะไร??', 'GUI is Graphical User Interface']
table.insert('','end',value=row) # end คือการ append ที่บันทัดสุดท้าย(last index)ของ Table นั้น

row = ['.insert() คืออะไร??', '.insert() คือการใส่ข้อมูลเข้าไป']
table.insert('',0,value=row) # 0 คือการ append ที่บันทัดแรก (first index)ของ Table นั้น
'''

def DeleteQuestion(event=None):
    select = table.selection() # ฃ่วยหน่อยว่ามีการเลือกคำถามข้อไหน?
    data = table.item(select)
    print(data['values'])
    allquestion.remove(data['values'])
    print('Count:',len(allquestion))
    
    # กรณีที่ต้องการลบเฉพาะค่าในโปรแกรม
    table.delete(*table.get_children()) # เคลียร์ข้อมูลชุดเก่าก่อนจำอัพเดทชุดใหม่เข้าไป
    alldata = allquestion
    for row in alldata:
        table.insert('','end',value=row) 

table.bind('<Delete>',DeleteQuestion)  

def SaveQuestion(event=None):
    check = messagebox.askquestion('ยืนยันการบันทึกข้อมูล','คุณต้องการบันทึกข้อมูลล่าสุดใช่หรือไม่? ข้อมูลเก่าจะหายหมด')

    if check == 'yes':
        with open('data.csv','w',newline='',encoding='utf-8') as file: # 'w' Replace to current file
            fw = csv.writer(file) # fw = file writer
            fw.writerows(allquestion)  # allquestion ล่าสุดจะถูกบันทึกแทน [['1+1=?','2'],['2+2=?','4']]
        print('บันทึกไฟล์สำเร็จ')
        # from tkinter import ttk, messagebox # ต้องการโชว์ป๊อปอัพต้องดึง messagebox
        messagebox.showinfo('Saving...','บันทึกข้อมูลสำเร็จ')    
    else:
        Updatetable() 

GUI.bind('<F1>',SaveQuestion)
L = ttk.Label(T1,text='หากต้องการบันทึกค่าล่าสุด กรุณากดปุ่ม <F1>',font=FONT3, foreground='blue')
L.pack()


'''&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& Tab2 Area &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'''

v_question = StringVar()  # ใช้สำหรับเก็บคำถาม
v_question.set('-----------------คำถาม (กดปุ่ม Next เพื่อเริ่ม)-----------------')
R1 = ttk.Label(T2,textvariable=v_question,font=FONT1)
R1.pack(pady=20)  


v_answer = StringVar()  # ใช้สำหรับเก็บคำตอบ
v_answer.set('----------------กดปุ่ม Show เพื่อแสดงคำตอบ)----------------')
R2 = ttk.Label(T2,textvariable=v_answer,font=FONT1)
R2.pack(pady=20)  



# Button
BF1 = Frame(T2) # BF คือ Button Frame
BF1.pack(pady=100)

allquestion = ReadCSV()
v_current_ans = StringVar()


def Next():
    q = random.choice(allquestion)
    v_question.set(q[0])
    v_current_ans.set(q[1])
    v_answer.set('----------------กดปุ่ม Show เพื่อแสดงคำตอบ)----------------')
    BC3['state'] = 'enable'

def Show():
    v_answer.set(v_current_ans.get())    # ดึงคำตอบล่าสุดจากบันทัด 149

# โชว์คะแนนที่ได้
score = 0
v_score = StringVar()
v_score.set('Score:{}'.format(score))
Score = ttk.Label(T2,textvariable=v_score,font=('Impact',30))
Score.place(x=20,y=20)

def ScoreUp():
    global score
    score += 1
    v_score.set('Score:{}'.format(score))
    BC3['state'] = 'disabled'




BC1 = ttk.Button(BF1,text='Next',command=Next)
BC2 = ttk.Button(BF1,text='Show',command=Show)
BC3 = ttk.Button(BF1,text='Score +1',command=ScoreUp)

BC1.grid(row=0,column=0,ipadx=20,ipady=30)
BC2.grid(row=0,column=1,ipadx=20,ipady=30)
BC3.grid(row=0,column=2,ipadx=20,ipady=30)

# โหลดข้อมูลจาก CSV เข้าไปในโปรแกรม
Updatetable() 


GUI.mainloop() # GUI.mainloop() จาก GUI จะทำให้โปรแกรมรันตลอด



