import requests
import webbrowser
import customtkinter as ctk
from PIL import Image
from tkinter import messagebox


class Pokeinfo:
    def __init__(self, tabview_instance):
        self.tabview_instance = tabview_instance
        self.label = ctk.CTkLabel(self.tabview_instance.tab("Pokeinfo"),
                                  text="Napisz nazwę pokemona lub jego numer ID i wciśnij Enter lub Przycisk", font=("Consolas", 16))
        self.entry = ctk.CTkEntry(self.tabview_instance.tab("Pokeinfo"), font=("Consolas", 16))
        self.button = ctk.CTkButton(self.tabview_instance.tab("Pokeinfo"), text="Wyszukaj", command=self.submit,
                                    font=("Consolas", 16))
        self.user_input = ""
        self.info_label = ""
        self.link_label = ""

        self.label.pack()
        self.entry.pack()
        self.entry.bind('<Return>', self.on_enter)
        self.button.pack()

    def on_enter(self, event):
        self.submit()

    def open_urls(self):
        print(self.user_input)
        webbrowser.open(f"https://www.smogon.com/dex/bw/pokemon/{self.user_input.lower()}")

    def submit(self):
        try:
            self.info_label.destroy()
            self.link_label.destroy()
        except Exception:
            pass
        self.user_input = self.entry.get()
        try:
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.user_input.lower()}")
            data = response.json()

            abils = []
            tys = []

            for i in data['abilities']:
                ability = i['ability']['name'].replace("-", " ")
                hidden = i['is_hidden']
                if hidden:
                    abils.append(f"{ability} - Hidden Ability")
                else:
                    abils.append(ability)

            abils = "\n".join(abils).title()

            for i in data['types']:
                type = i['type']['name']
                tys.append(type)

            tys = " | ".join(tys).title()

            id = data['id']
            image_path = f"downloaded_images/{id}.png"
            my_image = ctk.CTkImage(light_image=Image.open(image_path),
                                    dark_image=Image.open(image_path),
                                    size=(180, 180))

            hp = dict(data['stats'][0])['base_stat']
            att = dict(data['stats'][1])['base_stat']
            deff = dict(data['stats'][2])['base_stat']
            spatt = dict(data['stats'][3])['base_stat']
            spdef = dict(data['stats'][4])['base_stat']
            speed = dict(data['stats'][5])['base_stat']

            if att > spatt:
                att_or_spa = f"{self.user_input.title()} ma więcej ataku niż specjal ataku, więc jeśli chcesz ofensywnie zrobić" \
                             f" tego pokemona to polecam zrobic IV oraz EV w atak"
            elif att < spatt:
                att_or_spa = f"{self.user_input.title()} ma więcej specjal ataku niż ataku, więc jeśli chcesz ofensywnie zrobić" \
                             f" tego pokemona to polecam zrobić IV oraz EV w specjal atak"
            elif att == spatt:
                if self.user_input.lower() == "ditto":
                    att_or_spa = f"{self.user_input.title()} jest najsilniejszy jeśli złapiesz takiego z 31IV w HP " \
                                 f"oraz wbijesz wszystko w HP"
                else:
                    att_or_spa = f"{self.user_input.title()} ma tyle samo ataku co specjal ataku, więc jeśli chcesz zrobić go " \
                                 f"ofensywnie to możesz wybrać czy wolisz go zrobić pod atak lub specjal atak"

            self.info_label = ctk.CTkLabel(self.tabview_instance.tab("Pokeinfo"), font=("Consolas", 16), image=my_image,
                                           compound='top',
                                           text=f"""Informacje o pokemonie {self.user_input.title()}
Typy: {tys}

Umiejętnosći
{abils}

Bazowe statystyki
HP: {hp}
Atk: {att}
Def: {deff}
Sp. Atk: {spatt}
Sp. Def: {spdef}
Speed: {speed}

Jak breedować/zrobić tego pokemona?
{att_or_spa}

Ale lepiej upewnij się w grze w zakładce PvP/PvP Statistics oraz na stronie""")
            self.info_label.pack()
            self.link_label = ctk.CTkLabel(self.tabview_instance.tab("Pokeinfo"), font=("Consolas", 16), cursor="hand2",
                                           text_color="blue",
                                           text=f"""https://www.smogon.com/dex/bw/pokemon/{self.user_input.lower()}""")
            self.link_label.pack()
            self.link_label.bind("<Button-1>", lambda event: self.open_urls())
        except requests.exceptions.JSONDecodeError as e:
            messagebox.showerror(title="Error 404",
                                 message="""Nie znaleziono takiego pokemona, nieprawidłowa nazwa pokemona""",
                                 parent=self.tabview_instance.tab("Pokeinfo"))
