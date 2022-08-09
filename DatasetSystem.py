import re
from Dataset import Dataset
from Gui import Gui

class DatasetSystem(Gui,Dataset):
	def __init__(self):
		Dataset.__init__(self)
		Gui.__init__(self)	# Gui初始化时会调用mainloop发生阻塞，初始化顺序Dateset-Gui
	
	def search(self):
		self.clear()
		text = self.entry1.get()
		for title in self.dataset.keys():
			result = re.match(text+'.*',title)
			if result:
				title = result.group()
				self.showData(title,self.dataset[title])

if __name__ == "__main__":
	mySys = DatasetSystem()