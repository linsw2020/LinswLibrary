#coding=utf-8

import xlwings as xw

class TestExcel:
	"""
	Example:
        | Library | LinswLibrary |
  
  """      
	def __init__(self):
		self.wb = None
		self.app = None
		self.wsheet = None
		self.nsheet = None
		self.list1 = None
		self.danyuanvalue = None
		self.rcolsheet = None
		self.rrowsheet = None
		pass
	
	def OpenExcel(self,url):
		"""
    打开excel表
		Author linsw

    参数：文件路径+文件名
    
    返回值：无

    Example:
    		| *Keywords* 	|
        | open excel 	| C:\\TEST\\1.xls |
		
    """
		self.app = xw.App(visible = True, add_book = False)
		self.wb = self.app.books.open(url)
	
	def LastCol(self,sheetname):
		"""
    读取excel表的最长的行，返回最长行的值
		Author linsw

    参数：表名
    
    返回值：行的总数

    Example:
    		| *Keywords* 	|
        | Last Col  	| SheetName |
		
    """
		self.rcolsheet = self.wb.sheets(sheetname)
		info = self.rcolsheet.used_range
		nrows = info.last_cell.row
		return nrows
		
	def LastRow(self,sheetname):
		"""
    读取excel表的最长的列,返回最长列的值
		Author linsw

    参数：表名
    
    返回值：列的总数

    Example:
    		| *Keywords* 	|
        | Last Row  	| SheetName |
		
    """
		self.rcolsheet = self.wb.sheets(sheetname)
		info = self.rcolsheet.used_range
		ncolumns = info.last_cell.column
		return ncolumns
	
	def ReadSheet(self,sheetname,shuju):
		"""
    读取excel中表内数据
		Author linsw

		参数：表名，单元格（A1 或者 A1:B3）
		
		返回值：单元格里的所有值
		
    Example:
    		| *Keywords*   	|     
        | read sheet 	 	| Sheet1 |	A1:B3  |
		
		"""
		self.wsheet = self.wb.sheets(sheetname)
		self.wb.sheets.active
		self.list1 = []
		self.list1 = self.wsheet.range(shuju).value
		return self.list1
	
	def NewSheet(self,sheetname):
		"""
    新增表并引用该活动的表
		Author linsw

		参数：表名
		
		返回值：无
		
    Example:
    		| *Keywords*   	|     
        | new sheet 	 	| Sheet12 |
		
		"""		
		self.nsheet = self.wb.sheets.add(sheetname,before=None,after=None)
		self.wb.sheets.active
			
	def SaveCloseExcel(self):
		"""
    保存excel在原路径并关闭excel活动
		Author linsw

		参数：无
		
		返回值：无
		
    Example:
    		| *Keywords*         	|
        | save close excel 	 	|
		
		"""
		self.wb.save()
		self.wb.close()
		self.app.quit()
	
	def NewSheetValue(self,sheetname,shuju,danyuanvalue):
		"""
    在excel的单元格赋值
		Author linsw

		参数：表名，单元格，值
		
		返回值：无
		
    Example:
    		| *Keywords*       	|
        | new sheet value	 	| Sheet1 	|	A1 	| test 	|
		
		"""
		self.danyuanvalue = danyuanvalue
		self.wb.sheets[sheetname].range(shuju).value = self.danyuanvalue
	
	def SaveOtherExcel(self,url):
		"""
    另存文件
		Author linsw

		参数：文件路径+新文件名
		
		返回值：无
		
    Example:
    		| *Keywords*       	|
        | save other excel 	| C:\\TEST\\2.xls    |
		
		"""
		self.wb.save(url)
		self.wb.close()
		self.app.quit()
		
	def CloseExcel(self):
		"""
    关闭excel
		Author linsw

		参数：无
		
		返回值：无
		
    Example:
    		| *Keywords*  	|
        | close excel 	|    
		
		"""
		self.wb.close()
		self.app.quit()
		
	def JingFan(self,value1):
		"""
    镜像翻转，将字符倒装
		Author linsw

		参数：输入的值（eg:华中爱我）
		
		返回值：翻转后的值（eg:我爱中华）
		
    Example:
    		| *Keywords* |
        | Jing Fan 	 | 123456789 |  
        得到的值
        987654321
		"""
		strval = str(value1)
		Jingval = strval[::-1]
		return Jingval