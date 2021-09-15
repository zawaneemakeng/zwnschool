# นี่คือตัวอย่างสำหรับการเรียนOOP

### วิธีติดตั้ง

เปิด CMD / Terminal

```python
pip install zwnschool
```

### วิธีใช้งาน

เปิด IDLE ขึ้นมาแล้วพิมพ์...

```python
from zwnschool import Student,SpacialStudent
print('======= 1 Jan =======')
student0 = SpacialStudent('mark','elon')
student0.AskEXP()
student0.ShowEXP()

student1 = Student('Albert ')
print(student1.name)
student1.Hello()

student2 = Student('Tyuzu')
print(student2.name)
student2.Hello()
print('======= 2 Jan =======')
print('----Me : ใครอยากเรียนโค้ดดิ้งบ้าง----(10)----')
student1.AddEXP(10)
print('======= 3 Jan =======')
student1.name = 'Edward'#การเปลี่ยนชื่อ modifind attributes
print('ตอนนี้ exp ของเเต่ละคนได้เท่าไหร่กันเเล้ว')
print(student1.name,student1.exp)
print(student2.name,student2.exp)

print('======= 4 Jan =======')
for i in range(5):
    student2.Coding()
student1.ShowEXP()
student2.ShowEXP()

สำหรับการเรียนOOP

พัฒนาโดย: Zawanee Makeng
FB:https://www.facebook.com/z.zawanee |
