import time

# change your environment
ip_addr = "localhost"
port_num = 49408


class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)
        #ALProxy("API Name","RobotIPAddr",RobotPort)
        self.speechProxy = ALProxy("ALTextToSpeech",ip_addr,port_num)
        self.faceProxy = ALProxy("ALFaceDetection",ip_addr,port_num)

    def onLoad(self):
        #put initialization code here
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self):               
        success = self.faceProxy.learnFace("ほげほげ君")
        if(success==True):
            self.speechProxy.say("君の顔を覚えたよ！")        
        pass

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box
