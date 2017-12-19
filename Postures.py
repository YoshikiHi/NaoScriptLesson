import time

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)
        #ALProxy("API Name","RobotIPAddr",RobotPort)
        self.posture = ALProxy("ALRobotPosture","localhost",56678)

    def onLoad(self):
        #put initialization code here
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self):
        # applyPosture is Blocking Call.
        # goToPosture is NonBlocking Call.
        self.posture.post.applyPosture("Sit",1.0)

        # Wait 1s
        time.sleep(1)
        
        self.posture.post.applyPosture("Stand",1.0) 
        pass

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box
