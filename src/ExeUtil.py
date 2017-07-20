#!/usr/bin/python
# -*- coding: UTF-8 -*-
# --------------------------
# Author fzl
# Date 2017/2/25 15:13
# EMAIL fangjalylong@qq.com
# Desc 
# --------------------------


import os, os.path, sys
import win32process, win32event




class ExeUtil:
    def __init__(self, filePath, fileName):
        self.filePath = filePath
        self.fileName = fileName

    def openExe(self):
        try :
            handle = win32process.CreateProcess(os.path.join(self.filePath, self.fileName),
                '', None, None, 0,
                win32process.CREATE_NO_WINDOW,
                None ,
                self.filePath,
                win32process.STARTUPINFO())
            running = True
        except Exception, e:

            print "Create Error!"
            handle = None
            running = False

        while running :
         rc = win32event.WaitForSingleObject(handle[0], 1000)
         if rc == win32event.WAIT_OBJECT_0:
                running = False
    #end while
                print "GoodBye"