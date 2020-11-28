import RPi.GPIO as GPIO

class Moter:
    def __init__(self,Ena,in1,in2):
        # in1= input 1 forward
        # in2=input 2 backward
        self.Ena=Ena
        self.in1=in1
        self.in2=in2
        
        GPIO.setup(self.in1,GPIO.OUT)
        GPIO.setup(self.in2,GPIO.OUT)
        GPIO.setup(self.Ena,GPIO.OUT)
        self.p=GPIO.PWM(Ena,1000)
    def movef(self,s=30):
        try:
            self.p.ChangeDutyCycle(s)
            # GPIO.PWM(self.Ena,1000).ChangeDutyCycle(s)
            GPIO.output(self.in1,True)
            GPIO.output(self.in2,False)
        except:
            print("failed")
    def ChangeSpeed(self,s=30):
        try:
            self.p.ChangeDutyCycle(s)
        except :
            print("failed")
            
       
    def Stop(self):
        try:
            GPIO.output(self.in1,False)
            GPIO.output(self.in2,False)
            self.p.ChangeDutyCycle(0)
        except:
            print("failed")
    def moveB(self,s=30):
        try:
            self.p.ChangeDutyCycle(s)
            GPIO.output(self.in1,False)
            GPIO.output(self.in2,True)
        except:
            print("failed")
    def q(self):
        GPIO.cleanup()
