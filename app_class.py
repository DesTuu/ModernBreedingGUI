import customtkinter as ctk

from tab_class import MyTabView


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('blue')

        self.title("IVHelperApp")

        self.icon_path = "Pokeball_icon-icons.com_67533.ico"
        self.iconbitmap(default=self.icon_path)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")

        self.after(0, lambda: self.state("zoomed"))

        self.tab_view = MyTabView(master=self, width=screen_width - (screen_width * 0.026),
                                  height=screen_height - (screen_height * 0.139))
        self.tab_view.grid(row=0, column=0, padx=20, pady=20)

        self.switch_var = ctk.StringVar(value="off")
        self.switch = ctk.CTkSwitch(self, text="Włączyć jasny tryb aplikacji?",
                                   command=lambda: ctk.set_appearance_mode(
                                       'light') if self.switch_var.get() == "on" else ctk.set_appearance_mode('dark'),
                                   variable=self.switch_var, onvalue="on", offvalue="off")
        self.switch.place(relx=0.5, rely=0.02, anchor='center')
