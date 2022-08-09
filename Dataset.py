import re

class Dataset:

	def __init__(self):
		# 成员变量self.dataset
		self.dataset = {}
		self.__load__()
	
	def __load__(self):
		self.dataset = {}
		
		filePath = 'save.md'
		with open(filePath,encoding='utf-8') as fileObj:
			
			for line in fileObj:
				if not line.isspace():
					result = re.search('(?<=\*{2}).+(?=\*{2})',line)
					# 这里用match不行，用search行，不知道每一行前面还有什么
					if not result is None:
					# 是标题
						title = result.group()
						self.dataset[title] = []
					else:
					# 是内容
						self.dataset[title].append(line)


	# 读取并打印指定标题的信息（测试用）
	def print(self,str):
		if self.dataset is None:
			print('数据库为空！')
		elif not str in self.dataset.keys():
			print('没有指定的标题！')
		else:
			print('标题:'+str)
			for temp in self.dataset[str]:
				print(temp)








