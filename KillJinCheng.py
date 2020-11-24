#coding=utf-8
import os
import sys
import string
import psutil
import signal

class KillJinCheng(object):
    def __init__(self):
	    pass

    def KillChromeDriver(self):
        """ 杀死谷歌驱动进程 
        
        Author linsw
        
        参数：无
        
        返回值：无
        
        Example:
        	| *Keywords* 					|
        	| Kill Chrome Driver 	|
        """
        pid_dict = {}
        pids = psutil.pids()
        for pid in pids:
            p = psutil.Process(pid)
            pid_dict[pid] = p.name()
        for t in pid_dict.keys():
            if pid_dict[t] == "chromedriver.exe":
                try:
                    kill_pid = os.kill(t, signal.SIGABRT)
                except Exception as e:
                    pass