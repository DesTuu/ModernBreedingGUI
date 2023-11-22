import customtkinter as ctk

from info import create_info
from breeding import Breeding
from tutorial import Tutorial
from pokeinfo import Pokeinfo


class MyTabView(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.add("Info")
        self.add("Breeding")
        self.add("Pokeinfo")
        self.add("Poradniki")

        self.set("Breeding")

        create_info(self)

        breeding = Breeding(self)
        breeding.create_option_menu(1, 1, 14, 5)
        for i in range(2):
            breeding.create_option_menu(3, (i * 8) + 2, 4, 4)
        for i in range(4):
            breeding.create_option_menu(5, (i * 4) + 1, 2, 3)
        for i in range(8):
            breeding.create_option_menu(7, i * 2, 2, 2)
        for i in range(16):
            breeding.create_option_menu(9, i, 1, 1)

        tutorial = Tutorial(self)
        tutorial.create_tutorial()

        pokeinfo = Pokeinfo(self)