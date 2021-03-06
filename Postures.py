import time

# change your environment
ip_addr = "localhost"
port_num = 49408

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)
        #ALProxy("API Name","RobotIPAddr",RobotPort)
        self.posture = ALProxy("ALRobotPosture",ip_addr,port_num)

    def onLoad(self):
        #put initialization code here
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self):       
        # If Nao is not sitting ,Nao will sit down.
        if self.posture.getPosture() != "Sit":        
            self.posture.goToPosture("Sit",1.0)     

        # Wait 1 minutes
        time.sleep(1)        

        #StanUp
        self.posture.post.goToPosture("Stand",1.0)      
        pass

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box
