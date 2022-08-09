from abc import abstractmethod
from re import search
from tkinter import *

class Gui:

	def __init__(self):
		# 成员变量self.root|self.entry1|self.button1|self.row|self.column|self.componentList
		self.root = Tk()
		self.root.geometry('600x480+500+200')
		# 在(x, y)=(500, 200)的位置生成一个600x480的窗口
		self.root.title('标题检索系统')

		# 检索
		row1 = 1
		column1 = 1
		self.entry1 = Entry(self.root)
		self.entry1.grid(row=row1, column=column1)

		self.button1 = Button(self.root, text="搜索", command=self.search)
		self.button1.grid(row=row1, column=column1+1)
		
		def enterEvent(event):
			self.search()
		self.root.bind("<Return>", enterEvent)	# 回车和按钮都触发搜索功能

		# 消息展示
		self.row = 3
		self.column = 1

		self.componentList = []	# 集中存放临时组件

		self.root.mainloop()

	# 展示一条数据
	def showData(self, title, inf):
		# 显示标题
		label = Label(self.root, text=title, font=('黑体', 25, "bold"))
		label.grid(row=self.row, column=self.column)
		self.row+=1
		self.componentList.append(label)

		# 显示内容
		for temp in inf:
			label = Label(self.root, text=temp, font=('黑体', 15))
			label.grid(row=self.row, column=self.column)
			self.row+=1
			self.componentList.append(label)

	# 清空临时组件
	def clear(self):
		self.row = 3
		for component in self.componentList:
			component.destroy()
		self.componentList = []

	@abstractmethod
	# 获取检索栏的字符串，搜索标题，返回开头相同的信息
	def search(self):
		pass

	# def add(self)


