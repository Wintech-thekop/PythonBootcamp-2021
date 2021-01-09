# writecsv.py

import csv

def WritetoCSV(data):
    with open('test.csv','a',newline='',encoding='utf-8') as file: # With ใช้กับพวกเปิดไฟล์ หรือ Database
        fw = csv.writer(file) # fw = file writer
        fw.writerow(data)
    print('บันทึกไฟล์สำเร็จ')

data = ['print() คืออะไร?','คำสั่ง print() คือ คำสั่งในการแสดงผลข้อความ']
WritetoCSV(data)

    
