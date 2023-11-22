import customtkinter as ctk


class Breeding:
    def __init__(self, tabview_instance):
        self.tabview_instance = tabview_instance
        self.selected_iv = dict()
        self.option_menu_dict = dict()
        self.entry_dict = dict()
        self.label_dict = dict()
        self.text_dict = dict()
        self.selected_option = dict()
        self.ivs = ["HP", "Att", "Def", "SpAtk", "SpDef", "Speed"]
        self.color_ok = 'green'
        self.color_nok = 'red'
        self.reset_button = ""

    def delete_all(self):
        for key in self.selected_iv:
            self.selected_iv[key].set("")
        for key in self.entry_dict:
            self.entry_dict[key].configure(state=ctk.NORMAL)
            self.entry_dict[key].delete(0, ctk.END)
            self.entry_dict[key].configure(state="readonly")
            self.text_dict[key] = ""

    def option_selected(self, choice, idx):
        row, column = idx
        self.selected_option[str(row) + str(column)] = self.selected_iv[str(row) + str(column)].get()
        try:
            if row == 9:
                # 2x31
                if (column + 2) % 2 == 0 and self.selected_option[str(row) + str(column + 1)]:
                    self.text_dict[str(row - 2) + str(column)] = self.selected_option[str(row) + str(column)] + ", " + \
                                                                 self.selected_option[str(row) + str(column + 1)]
                    self.text_dict[str(row - 2) + str(column)] = set(
                        self.text_dict[str(row - 2) + str(column)].split(", "))
                    if len(self.text_dict[str(row - 2) + str(column)]) == 2:
                        self.entry_dict[str(row - 2) + str(column)].configure(text_color=self.color_ok)
                    else:
                        self.entry_dict[str(row - 2) + str(column)].configure(text_color=self.color_nok)
                    self.text_dict[str(row - 2) + str(column)] = ", ".join(self.text_dict[str(row - 2) + str(column)])
                    self.entry_dict[str(row - 2) + str(column)].configure(state=ctk.NORMAL)
                    self.entry_dict[str(row - 2) + str(column)].delete(0, ctk.END)
                    self.entry_dict[str(row - 2) + str(column)].insert(0, self.text_dict[str(row - 2) + str(column)])
                    self.entry_dict[str(row - 2) + str(column)].configure(state="readonly")
                    # 3x31
                    if (column + 4) % 4 == 0 and self.text_dict[str(row - 2) + str(column)] and self.text_dict[
                        str(row - 2) + str(column + 2)]:
                        self.text_dict[str(row - 4) + str(column + 1)] = self.text_dict[
                                                                             str(row - 2) + str(column)] + ", " + \
                                                                         self.text_dict[str(row - 2) + str(column + 2)]
                        self.text_dict[str(row - 4) + str(column + 1)] = set(
                            self.text_dict[str(row - 4) + str(column + 1)].split(", "))
                        if len(self.text_dict[str(row - 4) + str(column + 1)]) == 3:
                            self.entry_dict[str(row - 4) + str(column + 1)].configure(text_color=self.color_ok)
                        else:
                            self.entry_dict[str(row - 4) + str(column + 1)].configure(text_color=self.color_nok)
                        self.text_dict[str(row - 4) + str(column + 1)] = ", ".join(
                            self.text_dict[str(row - 4) + str(column + 1)])
                        self.entry_dict[str(row - 4) + str(column + 1)].configure(state=ctk.NORMAL)
                        self.entry_dict[str(row - 4) + str(column + 1)].delete(0, ctk.END)
                        self.entry_dict[str(row - 4) + str(column + 1)].insert(0, self.text_dict[
                            str(row - 4) + str(column + 1)])
                        self.entry_dict[str(row - 4) + str(column + 1)].configure(state='readonly')
                        # 4x31
                        if (column + 8) % 8 == 0 and self.text_dict[str(row - 4) + str(column + 1)] and self.text_dict[
                            str(row - 4) + str(column + 5)]:
                            self.text_dict[str(row - 6) + str(column + 2)] = self.text_dict[
                                                                                 str(row - 4) + str(
                                                                                     column + 1)] + ", " + \
                                                                             self.text_dict[
                                                                                 str(row - 4) + str(column + 5)]
                            self.text_dict[str(row - 6) + str(column + 2)] = set(
                                self.text_dict[str(row - 6) + str(column + 2)].split(", "))
                            if len(self.text_dict[str(row - 6) + str(column + 2)]) == 4:
                                self.entry_dict[str(row - 6) + str(column + 2)].configure(text_color=self.color_ok)
                            else:
                                self.entry_dict[str(row - 6) + str(column + 2)].configure(text_color=self.color_nok)
                            self.text_dict[str(row - 6) + str(column + 2)] = ", ".join(
                                self.text_dict[str(row - 6) + str(column + 2)])
                            self.entry_dict[str(row - 6) + str(column + 2)].configure(state=ctk.NORMAL)
                            self.entry_dict[str(row - 6) + str(column + 2)].delete(0, ctk.END)
                            self.entry_dict[str(row - 6) + str(column + 2)].insert(0,
                                                                                   self.text_dict[
                                                                                       str(row - 6) + str(column + 2)])
                            self.entry_dict[str(row - 6) + str(column + 2)].configure(state='readonly')
                        elif (column + 8) % 8 == 4 and self.text_dict[str(row - 4) + str(column - 3)] and \
                                self.text_dict[
                                    str(row - 4) + str(column + 1)]:
                            self.text_dict[str(row - 6) + str(column - 2)] = self.text_dict[
                                                                                 str(row - 4) + str(
                                                                                     column - 3)] + ", " + \
                                                                             self.text_dict[
                                                                                 str(row - 4) + str(column + 1)]
                            self.text_dict[str(row - 6) + str(column - 2)] = set(
                                self.text_dict[str(row - 6) + str(column - 2)].split(", "))
                            if len(self.text_dict[str(row - 6) + str(column - 2)]) == 4:
                                self.entry_dict[str(row - 6) + str(column - 2)].configure(text_color=self.color_ok)
                            else:
                                self.entry_dict[str(row - 6) + str(column - 2)].configure(text_color=self.color_nok)
                            self.text_dict[str(row - 6) + str(column - 2)] = ", ".join(
                                self.text_dict[str(row - 6) + str(column - 2)])
                            self.entry_dict[str(row - 6) + str(column - 2)].configure(state=ctk.NORMAL)
                            self.entry_dict[str(row - 6) + str(column - 2)].delete(0, ctk.END)
                            self.entry_dict[str(row - 6) + str(column - 2)].insert(0,
                                                                                   self.text_dict[
                                                                                       str(row - 6) + str(column - 2)])
                            self.entry_dict[str(row - 6) + str(column - 2)].configure(state='readonly')
                    # 3x31
                    elif (column + 4) % 4 == 2 and self.selected_option[str(row) + str(column - 2)] and \
                            self.selected_option[
                                str(row) + str(column - 1)] and self.selected_option[str(row) + str(column + 1)]:
                        self.text_dict[str(row - 4) + str(column - 1)] = self.text_dict[
                                                                             str(row - 2) + str(column - 2)] + ", " + \
                                                                         self.text_dict[str(row - 2) + str(column)]
                        self.text_dict[str(row - 4) + str(column - 1)] = set(
                            self.text_dict[str(row - 4) + str(column - 1)].split(", "))
                        if len(self.text_dict[str(row - 4) + str(column - 1)]) == 3:
                            self.entry_dict[str(row - 4) + str(column - 1)].configure(text_color=self.color_ok)
                        else:
                            self.entry_dict[str(row - 4) + str(column - 1)].configure(text_color=self.color_nok)
                        self.text_dict[str(row - 4) + str(column - 1)] = ", ".join(
                            self.text_dict[str(row - 4) + str(column - 1)])
                        self.entry_dict[str(row - 4) + str(column - 1)].configure(state=ctk.NORMAL)
                        self.entry_dict[str(row - 4) + str(column - 1)].delete(0, ctk.END)
                        self.entry_dict[str(row - 4) + str(column - 1)].insert(0, self.text_dict[
                            str(row - 4) + str(column - 1)])
                        self.entry_dict[str(row - 4) + str(column - 1)].configure(state='readonly')
                        # 4x31
                        if (column + 8) % 8 == 2 and self.text_dict[str(row - 4) + str(column - 1)] and self.text_dict[
                            str(row - 4) + str(column + 3)]:
                            self.text_dict[str(row - 6) + str(column)] = self.text_dict[
                                                                             str(row - 4) + str(column - 1)] + ", " + \
                                                                         self.text_dict[
                                                                             str(row - 4) + str(column + 3)]
                            self.text_dict[str(row - 6) + str(column)] = set(
                                self.text_dict[str(row - 6) + str(column)].split(", "))
                            if len(self.text_dict[str(row - 6) + str(column)]) == 4:
                                self.entry_dict[str(row - 6) + str(column)].configure(text_color=self.color_ok)
                            else:
                                self.entry_dict[str(row - 6) + str(column)].configure(text_color=self.color_nok)
                            self.text_dict[str(row - 6) + str(column)] = ", ".join(
                                self.text_dict[str(row - 6) + str(column)])
                            self.entry_dict[str(row - 6) + str(column)].configure(state=ctk.NORMAL)
                            self.entry_dict[str(row - 6) + str(column)].delete(0, ctk.END)
                            self.entry_dict[str(row - 6) + str(column)].insert(0, self.text_dict[
                                str(row - 6) + str(column)])
                            self.entry_dict[str(row - 6) + str(column)].configure(state='readonly')
                        elif (column + 8) % 8 == 6 and self.text_dict[str(row - 4) + str(column - 5)] and \
                                self.text_dict[
                                    str(row - 4) + str(column - 1)]:
                            self.text_dict[str(row - 6) + str(column - 4)] = self.text_dict[
                                                                                 str(row - 4) + str(
                                                                                     column - 5)] + ", " + \
                                                                             self.text_dict[
                                                                                 str(row - 4) + str(column - 1)]
                            self.text_dict[str(row - 6) + str(column - 4)] = set(
                                self.text_dict[str(row - 6) + str(column - 4)].split(", "))
                            if len(self.text_dict[str(row - 6) + str(column - 4)]) == 4:
                                self.entry_dict[str(row - 6) + str(column - 4)].configure(text_color=self.color_ok)
                            else:
                                self.entry_dict[str(row - 6) + str(column - 4)].configure(text_color=self.color_nok)
                            self.text_dict[str(row - 6) + str(column - 4)] = ", ".join(
                                self.text_dict[str(row - 6) + str(column - 4)])
                            self.entry_dict[str(row - 6) + str(column - 4)].configure(state=ctk.NORMAL)
                            self.entry_dict[str(row - 6) + str(column - 4)].delete(0, ctk.END)
                            self.entry_dict[str(row - 6) + str(column - 4)].insert(0,
                                                                                   self.text_dict[
                                                                                       str(row - 6) + str(column - 4)])
                            self.entry_dict[str(row - 6) + str(column - 4)].configure(state='readonly')
                # 2x31
                elif (column + 2) % 2 == 1 and self.selected_option[str(row) + str(column - 1)]:
                    self.text_dict[str(row - 2) + str(column - 1)] = self.selected_option[
                                                                         str(row) + str(column)] + ", " + \
                                                                     self.selected_option[str(row) + str(column - 1)]
                    self.text_dict[str(row - 2) + str(column - 1)] = set(
                        self.text_dict[str(row - 2) + str(column - 1)].split(", "))
                    if len(self.text_dict[str(row - 2) + str(column - 1)]) == 2:
                        self.entry_dict[str(row - 2) + str(column - 1)].configure(text_color=self.color_ok)
                    else:
                        self.entry_dict[str(row - 2) + str(column - 1)].configure(text_color=self.color_nok)
                    self.text_dict[str(row - 2) + str(column - 1)] = ", ".join(
                        self.text_dict[str(row - 2) + str(column - 1)])
                    self.entry_dict[str(row - 2) + str(column - 1)].configure(state=ctk.NORMAL)
                    self.entry_dict[str(row - 2) + str(column - 1)].delete(0, ctk.END)
                    self.entry_dict[str(row - 2) + str(column - 1)].insert(0, self.text_dict[
                        str(row - 2) + str(column - 1)])
                    self.entry_dict[str(row - 2) + str(column - 1)].configure(state="readonly")
                    # 3x31
                    if (column + 4) % 4 == 1 and self.text_dict[str(row - 2) + str(column - 1)] and self.text_dict[
                        str(row - 2) + str(column + 1)]:
                        self.text_dict[str(row - 4) + str(column)] = self.text_dict[
                                                                         str(row - 2) + str(column - 1)] + ", " + \
                                                                     self.text_dict[str(row - 2) + str(column + 1)]
                        self.text_dict[str(row - 4) + str(column)] = set(
                            self.text_dict[str(row - 4) + str(column)].split(", "))
                        if len(self.text_dict[str(row - 4) + str(column)]) == 3:
                            self.entry_dict[str(row - 4) + str(column)].configure(text_color=self.color_ok)
                        else:
                            self.entry_dict[str(row - 4) + str(column)].configure(text_color=self.color_nok)
                        self.text_dict[str(row - 4) + str(column)] = ", ".join(
                            self.text_dict[str(row - 4) + str(column)])
                        self.entry_dict[str(row - 4) + str(column)].configure(state=ctk.NORMAL)
                        self.entry_dict[str(row - 4) + str(column)].delete(0, ctk.END)
                        self.entry_dict[str(row - 4) + str(column)].insert(0,
                                                                           self.text_dict[str(row - 4) + str(column)])
                        self.entry_dict[str(row - 4) + str(column)].configure(state="readonly")
                        # 4x31
                        if (column + 8) % 8 == 1 and self.text_dict[str(row - 4) + str(column)] and self.text_dict[
                            str(row - 4) + str(column + 4)]:
                            self.text_dict[str(row - 6) + str(column + 1)] = self.text_dict[
                                                                                 str(row - 4) + str(column)] + ", " + \
                                                                             self.text_dict[
                                                                                 str(row - 4) + str(column + 4)]
                            self.text_dict[str(row - 6) + str(column + 1)] = set(
                                self.text_dict[str(row - 6) + str(column + 1)].split(", "))
                            if len(self.text_dict[str(row - 6) + str(column + 1)]) == 4:
                                self.entry_dict[str(row - 6) + str(column + 1)].configure(text_color=self.color_ok)
                            else:
                                self.entry_dict[str(row - 6) + str(column + 1)].configure(text_color=self.color_nok)
                            self.text_dict[str(row - 6) + str(column + 1)] = ", ".join(
                                self.text_dict[str(row - 6) + str(column + 1)])
                            self.entry_dict[str(row - 6) + str(column + 1)].configure(state=ctk.NORMAL)
                            self.entry_dict[str(row - 6) + str(column + 1)].delete(0, ctk.END)
                            self.entry_dict[str(row - 6) + str(column + 1)].insert(0,
                                                                                   self.text_dict[
                                                                                       str(row - 6) + str(column + 1)])
                            self.entry_dict[str(row - 6) + str(column + 1)].configure(state='readonly')
                        elif (column + 8) % 8 == 5 and self.text_dict[str(row - 4) + str(column - 4)] and \
                                self.text_dict[
                                    str(row - 4) + str(column)]:
                            self.text_dict[str(row - 6) + str(column - 3)] = self.text_dict[
                                                                                 str(row - 4) + str(
                                                                                     column - 4)] + ", " + \
                                                                             self.text_dict[
                                                                                 str(row - 4) + str(column)]
                            self.text_dict[str(row - 6) + str(column - 3)] = set(
                                self.text_dict[str(row - 6) + str(column - 3)].split(", "))
                            if len(self.text_dict[str(row - 6) + str(column - 3)]) == 4:
                                self.entry_dict[str(row - 6) + str(column - 3)].configure(text_color=self.color_ok)
                            else:
                                self.entry_dict[str(row - 6) + str(column - 3)].configure(text_color=self.color_nok)
                            self.text_dict[str(row - 6) + str(column - 3)] = ", ".join(
                                self.text_dict[str(row - 6) + str(column - 3)])
                            self.entry_dict[str(row - 6) + str(column - 3)].configure(state=ctk.NORMAL)
                            self.entry_dict[str(row - 6) + str(column - 3)].delete(0, ctk.END)
                            self.entry_dict[str(row - 6) + str(column - 3)].insert(0,
                                                                                   self.text_dict[
                                                                                       str(row - 6) + str(column - 3)])
                            self.entry_dict[str(row - 6) + str(column - 3)].configure(state='readonly')
                    # 3x31
                    elif (column + 4) % 4 == 3 and self.text_dict[str(row - 2) + str(column - 3)] and self.text_dict[
                        str(row - 2) + str(column - 1)]:
                        self.text_dict[str(row - 4) + str(column - 2)] = self.text_dict[
                                                                             str(row - 2) + str(column - 3)] + ", " + \
                                                                         self.text_dict[str(row - 2) + str(column - 1)]
                        self.text_dict[str(row - 4) + str(column - 2)] = set(
                            self.text_dict[str(row - 4) + str(column - 2)].split(", "))
                        if len(self.text_dict[str(row - 4) + str(column - 2)]) == 3:
                            self.entry_dict[str(row - 4) + str(column - 2)].configure(text_color=self.color_ok)
                        else:
                            self.entry_dict[str(row - 4) + str(column - 2)].configure(text_color=self.color_nok)
                        self.text_dict[str(row - 4) + str(column - 2)] = ", ".join(
                            self.text_dict[str(row - 4) + str(column - 2)])
                        self.entry_dict[str(row - 4) + str(column - 2)].configure(state=ctk.NORMAL)
                        self.entry_dict[str(row - 4) + str(column - 2)].delete(0, ctk.END)
                        self.entry_dict[str(row - 4) + str(column - 2)].insert(0, self.text_dict[
                            str(row - 4) + str(column - 2)])
                        self.entry_dict[str(row - 4) + str(column - 2)].configure(state="readonly")
                        # 4x31
                        if (column + 8) % 8 == 3 and self.text_dict[str(row - 4) + str(column - 2)] and self.text_dict[
                            str(row - 4) + str(column + 2)]:
                            self.text_dict[str(row - 6) + str(column - 1)] = self.text_dict[
                                                                                 str(row - 4) + str(
                                                                                     column - 2)] + ", " + \
                                                                             self.text_dict[
                                                                                 str(row - 4) + str(column + 2)]
                            self.text_dict[str(row - 6) + str(column - 1)] = set(
                                self.text_dict[str(row - 6) + str(column - 1)].split(", "))
                            if len(self.text_dict[str(row - 6) + str(column - 1)]) == 4:
                                self.entry_dict[str(row - 6) + str(column - 1)].configure(text_color=self.color_ok)
                            else:
                                self.entry_dict[str(row - 6) + str(column - 1)].configure(text_color=self.color_nok)
                            self.text_dict[str(row - 6) + str(column - 1)] = ", ".join(
                                self.text_dict[str(row - 6) + str(column - 1)])
                            self.entry_dict[str(row - 6) + str(column - 1)].configure(state=ctk.NORMAL)
                            self.entry_dict[str(row - 6) + str(column - 1)].delete(0, ctk.END)
                            self.entry_dict[str(row - 6) + str(column - 1)].insert(0,
                                                                                   self.text_dict[
                                                                                       str(row - 6) + str(column - 1)])
                            self.entry_dict[str(row - 6) + str(column - 1)].configure(state='readonly')
                        elif (column + 8) % 8 == 7 and self.text_dict[str(row - 4) + str(column - 6)] and \
                                self.text_dict[
                                    str(row - 4) + str(column - 2)]:
                            self.text_dict[str(row - 6) + str(column - 5)] = self.text_dict[
                                                                                 str(row - 4) + str(
                                                                                     column - 6)] + ", " + \
                                                                             self.text_dict[
                                                                                 str(row - 4) + str(column - 2)]
                            self.text_dict[str(row - 6) + str(column - 5)] = set(
                                self.text_dict[str(row - 6) + str(column - 5)].split(", "))
                            if len(self.text_dict[str(row - 6) + str(column - 5)]) == 4:
                                self.entry_dict[str(row - 6) + str(column - 5)].configure(text_color=self.color_ok)
                            else:
                                self.entry_dict[str(row - 6) + str(column - 5)].configure(text_color=self.color_nok)
                            self.text_dict[str(row - 6) + str(column - 5)] = ", ".join(
                                self.text_dict[str(row - 6) + str(column - 5)])
                            self.entry_dict[str(row - 6) + str(column - 5)].configure(state=ctk.NORMAL)
                            self.entry_dict[str(row - 6) + str(column - 5)].delete(0, ctk.END)
                            self.entry_dict[str(row - 6) + str(column - 5)].insert(0,
                                                                                   self.text_dict[
                                                                                       str(row - 6) + str(column - 5)])
                            self.entry_dict[str(row - 6) + str(column - 5)].configure(state='readonly')
                # 5x31
                if self.text_dict[str(3) + str(2)] and self.text_dict[str(3) + str(10)]:
                    self.text_dict[str(1) + str(1)] = self.text_dict[str(3) + str(2)] + ", " + self.text_dict[
                        str(3) + str(10)]
                    self.text_dict[str(1) + str(1)] = set(self.text_dict[str(1) + str(1)].split(", "))
                    if len(self.text_dict[str(1) + str(1)]) == 5:
                        self.entry_dict[str(1) + str(1)].configure(text_color=self.color_ok)
                    else:
                        self.entry_dict[str(1) + str(1)].configure(text_color=self.color_nok)
                    self.text_dict[str(1) + str(1)] = ", ".join(self.text_dict[str(1) + str(1)])
                    self.entry_dict[str(1) + str(1)].configure(state=ctk.NORMAL)
                    self.entry_dict[str(1) + str(1)].delete(0, ctk.END)
                    self.entry_dict[str(1) + str(1)].insert(0, self.text_dict[str(1) + str(1)])
                    self.entry_dict[str(1) + str(1)].configure(state="readonly")

        except KeyError:
            pass

    def create_option_menu(self, row, column, columnspan, text):
        if row > 8:
            self.selected_iv[str(row) + str(column)] = ctk.StringVar()
            self.option_menu_dict[str(row) + str(column)] = ctk.CTkOptionMenu(self.tabview_instance.tab("Breeding"),
                                                                              values=self.ivs,
                                                                              font=("Arial", 14, "bold"),
                                                                              dynamic_resizing=False,
                                                                              width=83,
                                                                              height=24,
                                                                              command=lambda choice, idx=(
                                                                                  row, column): self.option_selected(
                                                                                  choice,
                                                                                  idx=idx),
                                                                              variable=self.selected_iv[
                                                                                  str(row) + str(column)])
            self.option_menu_dict[str(row) + str(column)].grid(row=row, column=column, columnspan=columnspan, padx=5)
            self.option_menu_dict[str(row) + str(column)].set("")
        else:
            self.entry_dict[str(row) + str(column)] = ctk.CTkEntry(self.tabview_instance.tab("Breeding"),
                                                                   width=int(1300 / (row + 2)),
                                                                   font=("Arial Black", 14, "bold"),
                                                                   justify='center')
            self.entry_dict[str(row) + str(column)].configure(state="readonly")
            if str(self.entry_dict.keys()) == "dict_keys(['11'])":
                self.entry_dict[str(row) + str(column)].grid(row=row, column=column, columnspan=columnspan,
                                                             pady=(50, 0))
            else:
                self.entry_dict[str(row) + str(column)].grid(row=row, column=column, columnspan=columnspan)
            self.label_dict[str(row) + str(column)] = ctk.CTkLabel(self.tabview_instance.tab("Breeding"),
                                                                   text=f"⬆ Powinno być {text}x31IV ⬆",
                                                                   font=("Arial Black", 13, "bold"))
            self.label_dict[str(row) + str(column)].grid(row=row + 1, column=column, columnspan=columnspan)

            self.reset_button = ctk.CTkButton(self.tabview_instance.tab("Breeding"), text="Wyczyść wpisy", width=15,
                                              height=5, command=self.delete_all,
                                              font=("Arial Black", 18, "bold"))
            self.reset_button.grid(row=11, column=7, columnspan=2, pady=(20,0))
