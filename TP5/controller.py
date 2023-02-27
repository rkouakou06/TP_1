# encoding : utf8
"""The controller is the link between the "vue" and the "model".
It retrieves the variables contained in the "vue" and checks the data with the "model".
Here, it displays the graphical interface."""

from vue import Application #import of the Application class
from model import Model #import of the Model class allowing to modify a file

class Controller() :
    """Definition of the main attributes"""
    def __init__(self):
        self.model = Model("a.txt") #Inserting an empty "a.txt" file
        self.model.read_file() #creation of a dictionary that contains the animals of "a.txt"
        self.view = Application(self)
        self.view.view_window() #display of the graphic interface from "vue"

    def display(self, value):
        """Function to search the "dico_animaux" dictionary from "Model"
        and return what the user has entered in the search label"""
        self.view.display_label(self.model.dico_animaux[value])

    def add_animal(self, dict_animal):
        """Function to save all elements of the "dict_animal" dictionary from "Vue"."""
        self.model.save(dict_animal)

    def delete_animal(self, del_animal):
        """Function to delete an animal"""
        self.model.delete(del_animal)

    def modify_animal(self,dict_animal):
        """Function linked to the "model" allowing to modify an animal."""
        self.model.modify(dict_animal)

    def get_model_entries(self):
        """Function to retrieve the attributes of an animal."""
        return self.model.get_attributes()

    def get_names(self):
        """Function linked to the "model" to retrieve only the names of the animals."""
        return self.model.only_names

    def info_animal(self,name):
        """Function linked to the model to retrieve the attributes of the animals."""
        return self.model.info_animal(name)

    def quit_window(self):
        """Function to exit the window and print a message in the console"""
        print("close app")
        self.model.close() #close the file
        self.view.destroy() #destruction of the window

if __name__ == "__main__" :
    C = Controller()
