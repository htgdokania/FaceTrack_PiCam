import RPi.GPIO as GPIO          
from time import sleep
ypin = 26
xpin = 19

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(xpin,GPIO.OUT)
GPIO.setup(ypin,GPIO.OUT)

x=GPIO.PWM(xpin,50)
y=GPIO.PWM(ypin,50)

class servopos():
    def __init__(self):
        self.currentx,self.currenty=7,4
        x.start(self.currentx)
        y.start(self.currenty)
        sleep(1)
        x.ChangeDutyCycle(0)
        y.ChangeDutyCycle(0)
            
    def setposx(self,diffx):
        self.currentx+=diffx
        self.currentx=round(self.currentx,2)
        if(self.currentx<15 and self.currentx>0):
            x.ChangeDutyCycle(self.currentx)  
    def setposy(self,diffy):
        self.currenty+=diffy
        self.currenty=round(self.currenty,2)
        if(self.currenty<15 and self.currenty>0):
            y.ChangeDutyCycle(self.currenty)  
    def setdcx(self,dcx):
        x.ChangeDutyCycle(dcx)  
    def setdcy(self,dcy):
        y.ChangeDutyCycle(dcy)
