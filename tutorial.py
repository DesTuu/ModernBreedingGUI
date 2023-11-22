import webbrowser
import customtkinter as ctk


class Tutorial:
    def __init__(self, tabview_instance):
        self.tabview_instance = tabview_instance
        self.link_image = "https://cdn.discordapp.com/attachments/1133401796073758832/1146435926688546856/7JbVvvI.jpg"
        self.link_video = "https://www.youtube.com/watch?v=ZV7nS8sT_Fw"
        self.link_hidden = "https://forums.pokemmo.com/index.php?/topic/147619-hidden-ability-breeding-guide/"
        self.link_tutorial = "https://forums.pokemmo.com/index.php?/topic/49440-the-breeding-guide/"
        self.link_paczus = "https://docs.google.com/document/d/1AH6u07Yv87gK1ReP1BsjjzVk7Z5Ue8_O/edit?usp=sharing&ouid=110637772332510300137&rtpof=true&sd=true"

    def open_urls(self, link):
        webbrowser.open(link)

    def create_tutorial(self):
        link_label0 = ctk.CTkLabel(self.tabview_instance.tab("Poradniki"), font=("Consolas", 25), cursor="hand2", text_color="blue",
                               text=f"""ILUSTRACJA""")
        link_label0.pack(pady=40)
        link_label0.bind("<Button-1>", lambda e: self.open_urls(self.link_image))

        link_label1 = ctk.CTkLabel(self.tabview_instance.tab("Poradniki"), font=("Consolas", 25), cursor="hand2", text_color="blue",
                               text=f"""PORADNIK WIDEO""")
        link_label1.pack(pady=40)
        link_label1.bind("<Button-1>", lambda e: self.open_urls(self.link_video))

        link_label2 = ctk.CTkLabel(self.tabview_instance.tab("Poradniki"), font=("Consolas", 25), cursor="hand2", text_color="blue",
                               text=f"""HIDDEN ABILITY""")
        link_label2.pack(pady=40)
        link_label2.bind("<Button-1>", lambda e: self.open_urls(self.link_hidden))

        link_label3 = ctk.CTkLabel(self.tabview_instance.tab("Poradniki"), font=("Consolas", 25), cursor="hand2", text_color="blue",
                               text=f"""PORADNIK NA FORUM""")
        link_label3.pack(pady=40)
        link_label3.bind("<Button-1>", lambda e: self.open_urls(self.link_tutorial))

        link_label4 = ctk.CTkLabel(self.tabview_instance.tab("Poradniki"), font=("Consolas", 25), cursor="hand2", text_color="blue",
                               text=f"""POLSKI PORADNIK""")
        link_label4.pack(pady=40)
        link_label4.bind("<Button-1>", lambda e: self.open_urls(self.link_paczus))
