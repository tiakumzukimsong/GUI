import pyautogui

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
    

    # pyautogui.click(nt)
    # a = searchbar()
    
    print(nt)
    # print(a)
    # print(nt)
    # print(gm)

# def gmail():
#     gm = pyautogui.locateCenterOnScreen("gmail.png",grayscale=True, confidence=0.9)
#     pyautogui.click(gm)
    # pyautogui.moveTo(gm)


def searchbar():
    search_bar = pyautogui.locateCenterOnScreen("search_bar.png", grayscale=False,confidence=0.7)
    # search_bar_center = pyautogui.center(search_bar)
    
    print(search_bar)
    # pyautogui.click(search_bar)

def google():
    gg = pyautogui.locateOnScreen("google.png", grayscale=True,confidence=0.9)
    
    pyautogui.click(gg)
    newtab()
    # print(gg)
    # gmail()
    
    

    
searchbar()
# google()
# newtab()
# file()

