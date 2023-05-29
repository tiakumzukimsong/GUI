import pyautogui
import time
from PIL import Image

def click_menu():
	a = pyautogui.locateCenterOnScreen("menu.png",grayscale=True,confidence=0.5)

	pyautogui.click(a)
	# not_connected()
	# wifi_off()
	# main()

def not_connected():
	# reference_image = Image.open('/home/tia/Desktop/gui/wifi/wifi_not_connected.png')
	# dimensions = Image.open('/home/tia/Desktop/gui/wifi/wifi_not_connected.png')
	# width,height = dimensions.size
	# x,y = nc_region

	# search_region = (x,y,width,height)
	# match = pyautogui.locateCenterOnScreen(reference_image,region=search_region,grayscale=True,confidence=.85)


	# if 

	# if match is not None:
	# 	print("Wifi is not Connected")
	# else:
	# 	print("Wifi is already Connected")


	# print(x,y)
	# print(nc_region)
	# print(width,height)
	# print(match)
	time.sleep(2)

	nc_region = pyautogui.locateCenterOnScreen("wifi_not_connected.png", grayscale=True, confidence=0.95)

	if nc_region is not None:
		return True
	else:
		return False


def wifi_off():
	off = pyautogui.locateCenterOnScreen("wifi_off.png",grayscale=True,confidence=.1)

	if off is not None:
		return True
	else:
		return False
	# print(off)

def wifi_connected():
	connected  = pyautogui.locateCenterOnScreen("wifi_connected.png", grayscale=True, confidence=.85)
	if connected is not None:
		return True	
	else:
		return False

	# print(connected)

def onconnecting():
	onconnecting = pyautogui.locateCenterOnScreen("wifi_connecting.png",grayscale=True,confidence=.85)
	if onconnecting is not None:
		return True	
	else:
		return False

def main():

	click_menu()

	if wifi_off():
		settings = pyautogui.locateCenterOnScreen("settings.png",grayscale=True,confidence=.85)
		pyautogui.click(settings)
		time.sleep(2)
		turnon = pyautogui.locateCenterOnScreen("turnon.png", grayscale=True, confidence=.85)
		pyautogui.click(turnon)
		time.sleep(10)
		

	elif onconnecting():
		pass


	elif not_connected():

		settings = pyautogui.locateCenterOnScreen("settings.png",grayscale=True,confidence=.85)


		pyautogui.click(settings)
		time.sleep(2)

		tiakumzuk_wifi = pyautogui.locateCenterOnScreen("tiakumzuk.png",grayscale=True,confidence=.85)

		pyautogui.click(tiakumzuk_wifi)
		time.sleep(10)
		


	elif wifi_connected():
		pass

	
		

# click_menu()
main()
# wifi_off()