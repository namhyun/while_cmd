#-*- coding: utf-8-*-
import os
import sys
import time
import subprocess

e_count =0

class creteCmd():
    def __init__(self, commandName):
        self.commandName = commandName

    def cmdStarter(self):
        global e_count
        n_count = 0
        commandName = self.commandName
        try:
            self.openimg = subprocess.Popen(commandName, bufsize=2048, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            print  "create : " + commandName + "(" + str(e_count) + ")"
            e_count = e_count + 1
            n_count = e_count
            siteSave("create_cmd.log", commandName, n_count)
            
        except Exception as inst:
            exit(0)


def siteSave(filename, c_name, n_count):
    saveData =""
    try:
      with open(filename,'wb') as f:
          f.write(c_name+":"+ str(n_count))
          f.close()
                    
    except Exception as inst:         
        print inst
        pass

    
if __name__ == '__main__':
        start = time.time()
        argv = sys.argv
        timeOut = 0
        if len(argv) == 1:
            print "Please input data, (use : while_cmd.py calc 0)"
            exit(0)
        try:    
            execName = sys.argv[1]
            timeOut = int(sys.argv[2])
        except:
            pass

        while True:
            nsite = creteCmd(execName)
            nsite.cmdStarter()
            if timeOut > 0:
                time.sleep(timeOut)

        print "Elapsed Time: %s" % (time.time() - start)


