'''
Created on Oct 30, 2013

author: Thomas

Python ver: 2.7
'''
import pyglet
import os

#global variables
defaultSoundDir = "C:/the/directory/for/sounds/" #just the foulder containing the sounds
songListDir = defaultSoundDir + "songList.txt" #or anything that you want to name the file


class newSong(object):#will eventually extend something
    def __init__(self, command, fileName, permission):
        self.command = command
        self.fileName = fileName
        self.permission = permission
        work = [self.command,self.fileName, self.permission]
        if not os.path.exists(songListDir):
            with open(songListDir, "w") as var:
                var.write(str(work) + "\n")
        elif os.path.exists(songListDir):
            self.initCheck()

    
    
    def initCheck(self):
        global songListDir
        searchResult = None
        work = [self.command,self.fileName, self.permission]
        #this is so redundent it gives me cancer
        #test = file(songListDir, "r")
        test = list(file(songListDir, "r"))
        print self.command 
        for line in test:
            line = line.replace('\n','')
            if line == str(work):
            #"['" + str(self.command) + "', '" + str(self.fileName) + "', '" + str(self.permission) + "']":
                searchResult = True
                self.playAsong()
        if searchResult == None:
            with open(songListDir, "a") as var:
                var.write(str(work) + "\n")
                
        #test.close()
        


    def playAsong(self):
        global songListDir
        variable = open(songListDir, "r")
        desiredSongCommand = '\'' + raw_input("What song would you like to play?") + "\'"
        line = variable.readlines()
        for thing in line:
            if thing[1:len(desiredSongCommand)+1] == desiredSongCommand:
                desiredSongFile = pyglet.media.load(self.fileName)
                desiredSongFile.play()
                pyglet.app.run()
                pyglet.app.end()


        variable.close()
