from tkinter import *
from tkinter import ttk
import back_button_
import Auto_fighting_style
import time

window = Tk()
window.title("AutoMasteryFarm")
window.geometry("500x200")

setting_icon = PhotoImage(file = "setting_icon.png")
back_icon = PhotoImage(file = "back_icon.png")
god_human_icon = PhotoImage(file = "god_human_icon.png")

window.iconphoto(True, god_human_icon)

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

        window.destroy()

        window1 = Tk()

        info_nmfs_text = Label(window1, text = "Press 'B' to start and press 'V' to stop.", font = ("Consolas", 20))
        info_nmfs_text.pack()

        Auto_fighting_style.Auto_Fighting_Style_Function()

        window1.mainloop()

    def mfs_fun():
        Non_movement_figthing_style_button.destroy()
        Movement_fighting_style_button.destroy()

        window.destroy()

        window1 = Tk()

        info_nmfs_text = Label(window1, text = "Press 'B' to start and press 'V' to stop.", font = ("Consolas", 20))
        info_nmfs_text.pack()

        Auto_fighting_style.Auto_Movemet_Fighting_Style_Function()

        window1.pack()



    Non_movement_figthing_style_button = Button(text = "Non Movement Fighting Styles\n ex - Combat, water kunfu", command = nmfs_fun)
    Movement_fighting_style_button = Button(text = "Movement Fighting Styles\n ex - Electic Claw, Dragon Breath", command = mfs_fun)
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
