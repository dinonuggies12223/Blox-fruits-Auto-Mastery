from tkinter import *
from tkinter import ttk
import Auto_fighting_style

def back_button_s():

	window = Tk()
	window.title("AutoMasteryFarm")
	window.geometry("500x200")

	setting_icon = PhotoImage(file = "setting_icon.png")
	back_icon = PhotoImage(file = "back_icon.png")

	def fighting_style():
	    Fighting_Style_button.destroy()
	    Blox_Fruit_button.destroy()
	    Settings_button.destroy()

	    def back_button_fun():
	        window.destroy()
	        back_button_.back_button_s()

	    def nmfs_fun():
	        Non_movement_figthing_style_button.destroy()
	        Movement_fighting_style_button.destroy()

	        info_nmfs_text = Label(window, text = "Press 'B' to start and press 'V' to stop.", font = ("Consolas", 20))
	        info_nmfs_text.pack()

	        Auto_fighting_style.Auto_Fighting_Style_Function()


	    Non_movement_figthing_style_button = Button(text = "Non Movement Fighting Styles\n ex - Combat, water kunfu", command = nmfs_fun)
	    Movement_fighting_style_button = Button(text = "Movement Fighting Styles\n ex - Electic Claw, Dragon Breath")
	    Back_button = Button(image = back_icon, command = back_button_fun)

	    Non_movement_figthing_style_button.place(x = 10, y = 50)
	    Movement_fighting_style_button.place(x = 250, y = 50)
	    Back_button.place(x = 440, y = 150)

	def blox_fruit():
	    pass # Coming

	def settings():
	    Fighting_Style_button.destroy()
	    Blox_Fruit_button.destroy()
	    Settings_button.destroy()

	    info_text = Label(text = "COMING SOON!",
	                      font = ("Consolas", 20))

	    info_text.pack()

	Fighting_Style_button = Button(text = "Fighting Styles",
	                               padx = 5, pady = 5,
	                               command = fighting_style)

	Blox_Fruit_button = Button(text = "Blox Fruits (Coming Soon)",
	                           padx = 10, pady = 5,
	                           command = blox_fruit)

	Settings_button = Button(image = setting_icon,
	                         command = settings)

	Fighting_Style_button.place(x = 50, y = 50)
	Blox_Fruit_button.place(x = 250, y = 50)
	Settings_button.place(x = 440, y = 130)
	window.mainloop()