class Farm:
    def __init__(self,farm_name):
        self.name=farm_name
        self.animals={}
    def add_animal(self,animal_type,count=1):
        print("animal_type ",animal_type)
        if(animal_type in self.animals):
            self.animals[animal_type]+=count
        else:
            self.animals[animal_type]=count
    def get_info(self):
        sentence="The farm's name is "+self.name+"\n"
        for key in self.animals:
            print(key)
            sentence=sentence+key+" : "+str(self.animals[key])+"\n"
        sentence=sentence+"E-I-E-I-0!"
        return sentence

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.get_info()
print(macdonald.get_info())