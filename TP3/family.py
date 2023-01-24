# encoding : utf8
"""This program aims to create animals and give them attributes
such as name, species, diet... These animals can have children
and parents. So you can see their ancestors/descendants."""

class Animal():
    """We define this class and the main attributes"""
    def __init__(self, name, species, age, diet, mother = None) :
        self.name = name
        self.species = species
        self.age = age
        self.diet = diet
        self.children=[] #contains the names of the children
        self.mother = mother
        self.ancestors = [mother] #contains the names of all ancestors starting with the first
        self.descendants = [] #contains the names of all descendants

    def add_children(self, name) :
        """This function allows you to add a child to an animal.
        The child's name must be added. """
        child = Animal(name, self.species, self.age, self.diet, mother=self.name)
        for mom in self.ancestors :
            child.ancestors.append(mom)#adds the name of the parent to the list of ancestors
        self.children.append(child.name)#adds the name of children to the list of children
        return child

    def remove_children(self, name) :
        """This function allows you to delete a child.
        You have to add the name of the child to do the deletion."""
        if name in self.children:
            self.children.remove(name)
        print(name+" has been removed from the list of "+self.name+"'s children")

    def my_children(self):
        """This function allows to show all the children of an animal."""
        
        if not self.children :
            print(self.name + " has no child yet")
        else:
            print(self.name+" has "+str(len(self.children))+" children : "+str(self.children))

    def my_descendant(self):
        """This function should show all the descendants of an animal.
        It is not functional for the moment because it sends back only
        the children and not all the descendants"""
        all_child=[]
        for child in self.children:
            all_child.append(child)
        if not all_child :
            print(self.name+"doesn't have descendants yet")
        else:
            print(self.name+"'s descendant(s) : "+str(all_child))

    def my_ancestors(self):
        """This function allows you to show all the ancestors of an animal.
        The list of ancestors is read in reverse order to start with the oldest first """
        print(self.name + "'s ancestor(s) : " + str(self.ancestors[::-1]))


if __name__ == "__main__" :
    animal1=Animal("Billy","Dog",14,"carnivore","Poppy")
    animal2=Animal("Peter","Dog",8,"carnivore","Melo")
    animal4=animal1.add_children("Gugu")
    animal5=animal1.add_children("Roro")
    animal6=animal1.add_children("Tutu")
    animal7=animal5.add_children("Gigi")
    animal8=animal5.add_children("Popo")
    animal1.my_children()
    animal1.my_ancestors()
    animal1.remove_children("Tutu")
    animal1.my_children()
    animal5.my_children()
    animal5.my_ancestors()
    animal8.my_ancestors()
    animal2.my_ancestors()
    animal2.my_children()

    
