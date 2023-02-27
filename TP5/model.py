# encoding : utf8
"""Here the "model" allows you to save animals and display them in a file."""

from Animal import Animal

class Model():
    """Model class"""
    def __init__(self, filename):
        self.filename = filename
        self.file=open(self.filename, "r+", encoding="utf8") #open the file in read+write
        self.dico_animaux = {} #creating a dictionary to store animals
        self.only_names = []

    def read_file(self):
        """Function allowing to select the attributes of an animal
        and to store them in the "dico_animaux" dictionary."""
        for line in self.file:
            line = line.strip() #remove line breaks
            tab = line.split(",") #separate line from ","
            a = Animal(tab[0],tab[1],tab[2],tab[3],tab[4])
            self.dico_animaux[a.name] = a #key = animal's name, value = all the attributs
            self.only_names.append(a.name) #list containing only the names of the animals

    def save(self, dict_animal):
        """Function allowing to save in the file the animals present
        in the "dict_animal" dictionary (present in the "vue" cript)."""
        self.file.write("\n"+dict_animal["species"]+","+
        dict_animal["age"]+","+dict_animal["diet"]+","+dict_animal["foot"]+","+dict_animal["name"])

    def delete(self, del_animal):
        """Function to delete an animal, both in the "dico_animaux" dictionary
        and in the file. it takes as input the name of the animal to delete."""
        del self.dico_animaux[del_animal] #delete from the dico
        #delete from the file
        self.file.seek(0) #position the cursor on the beginning of the file
        lines = self.file.readlines()
        self.file.seek(0)
        self.file.truncate() #clear the file of it's content
        for line in lines:
            line_split=line.strip("\n").split(",") #recovery of the animal's name
            if line_split[-1] != del_animal:
                #write the name of the animal if it is different from del_animal
                self.file.write(line)

    def modify(self, dict_animal):
        """Function to modify an animal.
        It uses the "delete" function, in order to delete the name
        and the attributes of the animal to be modified,
        and the "save" functon, in order to save the modifications on the file."""
        self.delete(dict_animal["name"])
        self.save(dict_animal)

    def close(self):
        """Function to close the file."""
        self.file.close()

    def get_attributes(self)->[]:
        """Function that allows to retrieve the attributes of an animal."""
        attr = []
        # get first key of the dict no mater what is it
        first_key = next(iter(self.dico_animaux))
        for key in self.dico_animaux[first_key].__dict__:
            attr.append(key)
        return attr

    def info_animal(self,name):
        """Function to retrieve the attributes of the animals.
        it will be used in case the user wants to modify an animal.
        It allows to display in the input fields the information about the selected animal."""
        self.file.seek(0)
        for line in self.file:
            if name in line:
                line = line.strip("\n").split(",")
                return line

if __name__ == "__main__" :
    model = Model("a.txt")
    model.read_file()
    model.close()
