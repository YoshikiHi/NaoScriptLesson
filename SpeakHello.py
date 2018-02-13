# change your environment
ip_addr = "localhost"
port_num = 49408

class MyClass(GeneratedClass):    
    def __init__(self):
        GeneratedClass.__init__(self)
        #ALProxy("API Name","RobotIPAddr",RobotPort)
        self.speak = ALProxy("ALTextToSpeech",ip_addr,port_num)

    def onLoad(self):
        #put initialization code here
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self):
        self.speak.post.say("HelloWorld")
        pass

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box
