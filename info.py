import customtkinter as ctk


def create_info(tabview_instance):
    info_label = ctk.CTkLabel(tabview_instance.tab("Info"), font=("Arial Black", 28, "bold"),
                              text="""Klikając na pustą budkę na dole wybierasz statystykę, w której masz 1x31 w IV.
Wyświetli na zielono = OK, Wyświetli na czerwono = NOK.
Aplikacja uwzględnia tylko i wyłącznie używanie braców na każdym poku.
Nie bierze pod uwagę breedowania natury, która powinna być dodawana na samym końcu.
Nie bierze pod uwagę również płci.
By zrobić 5x31 poka z naturą należy zrobić pierw 5x31 bez natury, potem 4x31 bez natury itd.
Wyjątkiem jest jeśli wyjdzie odpowiednia natura przy breedzie minimum 3x31 IV""")
    info_label.place(relx=0.5, rely=0.5, anchor='center')
