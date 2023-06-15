from pynput.keyboard import Key, Controller
import keyboard
import pyautogui as pg
import time

my_keyboard = Controller()

def Auto_Fighting_Style_Function():
	while True:
	    if keyboard.is_pressed("b"):
	        while True:
	            pg.click()
	            if keyboard.is_pressed("v"):
	                break
	    else:
	        pass

def Auto_Movemet_Fighting_Style_Function():
	while True:
		if keyboard.is_pressed("b"):
			while True:
				pg.click()
				time.sleep(1)
				if keyboard.is_pressed("v"):
					break