import time
class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)
        #ALProxy("API Name","RobotIPAddr",RobotPort)
        self.motionProxy = ALProxy("ALMotion","localhost",49408)
        self.speechProxy = ALProxy("ALTextToSpeech","localhost",49408)

    def onLoad(self):
        #put initialization code here
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self):
        # Setting wakeup mode
        self.motionProxy.wakeUp()       

        # Adjustment of right arm position(Up)
        self.motionProxy.setAngles(["RShoulderPitch","RShoulderRoll"],[0.5,0.0],0.1)     

        # OpenHand
        self.motionProxy.openHand("RHand")

        time.sleep(3)
        
        # Adjustment of right arm position(Down)
        self.motionProxy.setAngles(["RShoulderPitch","RShoulderRoll"],[1.5,0.0],0.1)     

        # CloseHand
        self.motionProxy.closeHand("RHand")
        
        self.speechProxy.say("Thank you！")
                  
        pass

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box
