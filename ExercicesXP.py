#ex1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

def find_oldest_cat(cat1,cat2,cat3):
    oldest=cat1
    if(cat3.age>cat1.age and cat3.age>cat2.age):
        oldest.name=cat3.name
        oldest.age=cat3.age
    elif(cat2.age>cat1.age and cat2.age>cat3.age):
        oldest.name=cat2.name
        oldest.age=cat2.age
    return oldest 
cat1=Cat("Lola",12)
cat2=Cat("Chouchou",7)
cat3=Cat("Lapinou",13)
oldest_cat=find_oldest_cat(cat1,cat2,cat3)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

#ex2
class Dog:
    def __init__(self,name,height):
        self.name=name
        self.height=height
    def bark(self):
        print(f"{self.name} goes woof!")
    def jump(self):
        x=self.height*2
        print(f"{self.name} jumps {x} cm high!")
davids_dog=Dog("boulette",12)
sarahs_dog=Dog("chouchounette",9)
print("David's dog name is ",davids_dog.name, "and his height is",davids_dog.height,"and Sarah's dog name is ",sarahs_dog.name," and his height is ",davids_dog.height)
davids_dog.bark()
sarahs_dog.bark()
davids_dog.jump()
sarahs_dog.jump()

#ex3
class Song:
    def __init__(self,lyrics):
        self.lyrics=lyrics
    def sing_me_a_song(self):
        for word in self.lyrics:
            print(word)
stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

#ex4
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name=zoo_name
        self.animals=[]
        self.grouped_animals={}

    def add_animal(self, new_animal):
        if(new_animal not in self.animals):
            self.animals.append(new_animal)
    def get_animals(self):
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if(animal_sold in self.animals):
            self.animals.remove(animal_sold)

    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        for animal in sorted_animals:
            firstLetter=animal[0].upper()
            if(firstLetter not in  self.grouped_animals):
                self.grouped_animals[firstLetter] = []
                self.grouped_animals[firstLetter].append(animal)
        

    def get_groups(self):
        for key in self.grouped_animals:
            print(key," : ",self.grouped_animals[key])

# Step 2: Create a Zoo instance
brooklyn_safari = Zoo("Brooklyn Safari")

# Step 3: Use the Zoo methods
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()




