class Student:
	def __init__(self,name):
		self.name = name
		self.exp = self.lesson = 0
	def Hello (self):
		print('สวัสดีจ้าา เราชื่อ{}'.format(self.name))
	def Coding(self):
		print('{}: กำลังเขียนโปรเเกรม'.format(self.name))
		self.exp += 5
		self.lesson += 1

	def ShowEXP (self):
		print('ตอนนี้{} มีประสบการณ์ {} exp\n'.format(self.name,self.exp))
		print('เรียนไป{} ครั้งเเล้ว'.format(self.lesson))
		
	def AddEXP(self,scoer):
		self.exp += scoer
		self.lesson +=1
	  
class SpacialStudent(Student):
	def __init__(self, name, father):
		super().__init__(name)
		self.father = father
		mafia = ['Bill','elon']
		if father in mafia:
			self.exp += 100

	def AddEXP(self, scoer):
		self.exp += (scoer * 3)
		self.lesson += 1

	def AskEXP(self, score = 10):
		print('ครู !! ขอคะเเนนพิเศษให้หนูหน่อยสิ {}EXP '.format(score))
		self.AddEXP(score)


if __name__ == '__main__':

	print('======= 1 Jan =======')
	student0 = SpacialStudent('mark','elon')
	student0.AskEXP()
	student0.ShowEXP()

	student1 = Student('Albert ')
	print(student1.name)
	student1.Hello()

	student2 = Student('tyuzu')
	print(student2.name)
	student2.Hello()
	print('======= 2 Jan =======')
	print('----uncle : ใครอยากเรียนโค้ดดิ้งบ้าง----(10)----')
	student1.AddEXP(10)
	print('======= 3 Jan =======')
	student1.name = 'Edward'#การเปลี่ยนชื่อ modifind atttributes
	print('ตอนนี้ exp ของเเต่ละคนได้เท่าไหร่กันเเล้ว')
	print(student1.name,student1.exp)
	print(student2.name,student2.exp)

	print('======= 4 Jan =======')
	for i in range(5):
		student2.Coding()
	student1.ShowEXP()
	student2.ShowEXP()


