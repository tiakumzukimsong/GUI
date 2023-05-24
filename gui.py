import pyautogui
import time

def file():
    file = pyautogui.locateCenterOnScreen("file.png",grayscale=True, confidence=.8)
    
    pyautogui.click(file)
    # print(file)
    # print("hello")
    
def view():
    view = pyautogui.locateCenterOnScreen("view.png",grayscale=True, confidence=.8)
    
    pyautogui.click(view)
    # print(view)
    
def newtab():
    nt = pyautogui.locateCenterOnScreen("newtab.png",grayscale=True, confidence=.8)
    

    pyautogui.click(nt)
    
    
  
    instagram()

def instagram():
    text = "instagram.com"
    pyautogui.typewrite(text)
    pyautogui.press("enter")
    
    instagram_message()

def instagram_message():
    time.sleep(5)
    messages = pyautogui.locateCenterOnScreen("instagram_messages.png", grayscale=True,confidence=0.85)
    pyautogui.click(messages)
    imlikumla()

def imlikumla():
    time.sleep(5)
    im = pyautogui.locateCenterOnScreen("imlikumla_message.png", grayscale=True, confidence=.85)
    pyautogui.click(im)
    message_imli()

def message_imli():
    time.sleep(5)
    text_imli = pyautogui.locateCenterOnScreen("instagram_inside_message.png", grayscale=True,confidence=.85)
    pyautogui.click(text_imli)
    text= "I'm texting using my automatic texting machine HUHUHUHUHUHUHU"
    pyautogui.typewrite(text)
    pyautogui.press("enter")
    

    
# searchbar()
# google()
newtab()
# file()







# def gmail():
 
    
#     text = "gmail.com"
#     pyautogui.typewrite(text)
#     pyautogui.press("enter")


    
# def whatsapp():
#     text = "web.whatsapp.com"
#     pyautogui.typewrite(text)
#     pyautogui.press("enter")


# def google():
#     gg = pyautogui.locateOnScreen("google.png", grayscale=True,confidence=0.9)
    
#     pyautogui.click(gg)
#     newtab()
#     # print(gg)
#     # gmail()