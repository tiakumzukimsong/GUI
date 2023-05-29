import pyautogui
import time
from PIL import Image

def click_menu():
	a = pyautogui.locateCenterOnScreen("menu.png",grayscale=True,confidence=0.85)

	pyautogui.click(a)
	# not_connected()
	wifi_off()


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
	off = pyautogui.locateCenterOnScreen("wifi_off.png",grayscale=True,confidence=.85)

	if off is not None:
		return True
	else:
		return False
	# print(off)



def main():
	if wifi_off():
		off_wifi = pyautogui.locateCenterOnScreen("wifi_off.png",grayscale=True,confidence=.85)
		


click_menu()