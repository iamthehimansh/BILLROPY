from RPi import GPIO
import time

TRIG=7
ECHO=8
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG, False)
while True:
    time.sleep(0.25)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
        starttime=time.time()
    while GPIO.input(ECHO)==1:
        stoptime=time.time()
    d_cm=(stoptime-starttime)*34300
    print(str(d_cm)+" cm")
    
