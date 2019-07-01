from pygame import mixer
import time
def sound():
    mixer.init()
    mixer.music.load(r'C:\Users\Snehal dalvi\Desktop\python\emergency_contact.wav')

def alarm():
    hour=int(input("HOURS:"))
    minute=int(input("MINUTES:"))
    second=int(input("SECONDS:"))

    n=5
    print("alarm sert for:",str(hour),str(minute),str(second))

    while(True):
        if(time.localtime().tm_hour==hour and time.localtime().tm_min==minute and time.localtime().tm_sec==second):
            print("hey!!! wake up")
            break
    sound()
    while(n>0):
        mixer.music.play()
        time.sleep(2)

    snehal=str(raw_input("press S for snooze"))
    if(snehal=='S'):
        n=3
        time.sleep(100)
        while(n>0):
            mixer.music.play()
            time.sleep(2)
    else:
        exit()
        


