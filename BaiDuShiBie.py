#coding=utf-8
#介于python3.x，需要改动
import sys
#import urllib2
import urllib
from aip import AipOcr
import re
import sys


class BaiDuShiBie(object):
	def __init__(self):
		pass

	def GetDownload(self,url1,imgurl):		
		"""
    从百度中将图片下载下来并保存在c盘的a.jpg
		Author linsw

    参数：目标路径、保存路径

    Example:
    		| *Keywords* 			|
        | get down load 	| http://www.baidu.com |	c:\\a.jpg	|
		
		"""
		headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
		#request = urllib2.Request(url1,headers=headers)
		request = urllib.Request(url1,headers=headers)
		#repronse = urllib2.urlopen(request)
		repronse = urllib.urlopen(request)

		type = sys.getfilesystemencoding()

		with open(imgurl,"wb") as f:
			f.write(repronse.read())
	
	def ShiBieDd(self,API_ID,API_KEY,SECRECT_KEY,url):
		"""
    在"http://ai.baidu.com/"查找自己的信息
    
    使用自己在百度云控制台注册的用户填入id、key等, getAPI_ID,API_KEY,SECRECT_KEY
    
		Author linsw

    参数：用户id,用户key,识别key,本地图片路径

    Example:
    		| *Keywords* 		|
        | shi bie bd  	| API_ID |	API_KEY	|	SECRECT_KEY	|	c:\\a.jpg	|
		
		"""		
		reload(sys)

		sys.setdefaultencoding('utf8')
		
		client = AipOcr(API_ID,API_KEY,SECRECT_KEY)
		i=open(url,"rb")
		img=i.read()
		message=client.basicGeneral(img)
		return message
		
	def splitVerifyCode(self,verifyCode):
		#verifyCode={"log_id": 4413325641531023902, "words_result_num": 1, "words_result": [{"words": "H ,.5LC"}]}
		"""splitVerifyCode verifyCode  Format verification code识别和切割验证码	Author txf"""
		str= verifyCode["words_result"][0]["words"]
		splitstr="";
		for x in str:
			if(x.isdigit() or x.isalpha()):
				splitstr+=x
		return splitstr