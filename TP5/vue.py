# encoding : utf8
"""This script allows you to configure the elements that will be visible in the window."""
from tkinter import *
from tkinter import messagebox

class Application(Tk):
    """Class containing all the widgets present in the interface"""
    def __init__(self, controller):
        Tk.__init__(self)
        self.controller = controller
        self.attributes = self.controller.get_model_entries()
        self.names = self.controller.get_names() #recovers only the names of the animals
        self.creer_widgets()

    def creer_widgets(self):
        """Function allowing to create all the widgets that will be present in the window."""
        #LABELS
        self.label = Label(self, text="J'adore Python !")
        self.label1 = Label(self, text="")
        self.label_search = Label(self, text="Recherche")
        #BUTTONS
        self.bouton_display = Button(self, text="Afficher", command=self.display_something)
        self.bouton = Button(self, text="Quitter", command=self.quit_window)
        self.bouton_add_animal = Button(self, text="Add/Modify", command=self.add_modif_animal)
        self.button_del = Button(self, text="Delete", command=self.delete_animal)
        self.button_modify = Button(self, text="Modify", command=self.info_animal)
        self.search = Entry(self)
        self.entries = {}
        self.entries_label = {}
        for att in self.attributes:
            #Loop displaying a label and an entry for each attribute
            self.entries[att] = Entry(self)
            self.entries_label[att] = Label(self, text=att)

        #Initialization of the listbox
        self.listebox = Listbox(self)
        counter = 0
        for names in self.names:
            counter += 1
            self.listebox.insert(counter, names)

        self.label.pack()
        self.label1.pack()
        self.label_search.pack()
        self.search.pack()
        self.bouton_display.pack()
        self.listebox.pack()
        self.button_del.pack()
        self.button_modify.pack()
        for att in self.attributes:
            self.entries_label[att].pack()
            self.entries[att].pack()
        self.bouton_add_animal.pack()
        self.bouton.pack()

    def quit_window(self):
        """Function to exit the window via the Controler script.
        It is linked to the "quitter" button."""
        self.controller.quit_window()

    def display_something(self):
        """Function to display all attributes of the animal the user is looking for.
        It is linked to the "afficher" button."""
        self.controller.display(self.search.get())

    def display_label(self, value):
        """Function to display the animal and its attributes that the user has searched for."""
        self.label1['text'] = value

    def add_modif_animal(self):
        """Function to add or modify an animal."""
        dict_animal = {} #dictionary containing the animals with their attributes
        for key in self.entries:
            dict_animal[key] = self.entries[key].get() #saves the elements entered in dict_animal
        if dict_animal["name"] in self.names:
            #if the name of the animal is already present, it adds that the modifications
            self.controller.modify_animal(dict_animal)
            messagebox.showinfo(title="Modified", message="The animal has been modified")
        if dict_animal["name"] not in self.names:
            #if the name of the animal is not present, it adds the new animal and its attributes
            self.controller.add_animal(dict_animal)
            self.listebox.insert(END, dict_animal["name"])
            messagebox.showinfo(title ="Added", message ="The animal has been added")
        for key in self.entries: #empty the fields 
            self.entries[key].delete(0, END)

    def delete_animal(self):
        """Function to delete an animal."""
        deletion = self.listebox.get(self.listebox.curselection())#retrieves the animal selected
        self.controller.delete_animal(deletion)#removes the animal
        for i in range(self.listebox.size()):
            #allows you to remove the animal from the listbox
            if self.listebox.get(i) == deletion :
                self.listebox.delete(i)
        messagebox.showinfo(title = "Deleted", message ="The animal has been deleted")

    def info_animal(self):
        """function allowing to have the attributes of the animals
        in order to display them on the input fields when the user wants to modify them"""
        for key in self.entries:
            self.entries[key].delete(0, END) #empty the fields
        modification = self.listebox.get(self.listebox.curselection())
        info = self.controller.info_animal(modification)
        nb_entries = len(self.attributes)
        for i in range(0,nb_entries):
            #inserts the attributes of the animal on the corresponding input fields
            self.entries[self.attributes[i]].insert(0,info[i])

    def view_window(self):
        """Function to display the window."""
        self.title("Ma Première App :-)")
        self.mainloop()

if __name__ == "__main__":
    app = Application()
    app.view_window()
