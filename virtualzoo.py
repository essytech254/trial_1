import random # to generate random values used in simulating animal interaction and initiliazing attributes.

# Define the Animal class
class Animal: # represents the individual animals.
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.fear = random.randint(50, 100) # random intergers
        self.happiness = random.randint(0, 50) # random intergers
    
    def temp(self): # the temp method decreases the animals fear by 15 and increases its happiness by 10.
        self.fear -= 15
        self.happiness += 10
    
    def play(self): # increases the animal's happiness by 15.
        self.happiness += 15
    
    def __str__(self): # this method provides a string representation of an animal:name, species,fear,happiness.
        return f"{self.name} ({self.species}) - fear: {self.fear}, Happiness: {self.happiness}"

# Define different types of animals # inheritance. subclasses.
class Zebra(Animal):
    def __init__(self, name):
        super().__init__(name, "Zebra")

class Girrafe(Animal):
    def __init__(self, name):
        super().__init__(name, "Girrafe")

class Chimpanzee(Animal):
    def __init__(self, name):
        super().__init__(name, "Chimpanzee")

# Define the Zoo class
class Zoo: # this represents a virtual zoo that contains a collection of animals
    def __init__(self):# initilizes an empty list that stores animals in the zoo
        self.animals = []
    
    def add_animal(self, animal): # allows you to add animals in the zoo and append it to the list
        self.animals.append(animal)
    
    def remove_animal(self, animal): # allows you to remove animals from the zoo by removing it from the list.
        self.animals.remove(animal)
    
    def simulate_day(self): # simulates a day in the zoo.
    # it iterates through each animal in the zoo and with a random  chance it calls the 'temp','play' method to simulate ineractions within the animals.
    # it then prints out the status of each animal using the 'str' method
        for animal in self.animals:
            if random.choice([True, False]): # simulates the chances of an event occuring
            # checks thefirst random condition if it true it calls the 'temp' method simulating checking the temparature
                animal.temp()
            if random.choice([True, False]): #  checks the second random condition 50% of it being true it then calls the method simulating playing with it.
                animal.play()
            print(animal)
            #These random conditions introduce an element of unpredictability and variation in the animals' interactions and well-being in the virtual pet zoo.
    
    def __str__(self):
        return f"Zoo: {', '.join(animal.name for animal in self.animals)}"

# Create some animals
zebra = Zebra("Zebby")
girrafe = Girrafe("Giffy")
chimpanzee = Chimpanzee("Chimp")

# Create a zoo and add animals
# we add those animals to the zoo
zoo = Zoo()
zoo.add_animal(zebra)
zoo.add_animal(girrafe)
zoo.add_animal(chimpanzee)

# Simulate a few days in the zoo
for day in range(1, 4): #This line sets up a for loop that iterates over a range of numbers. range(1, 4) generates a sequence of numbers from 1 to 3 (inclusive).
    print(f"Day {day}:") # Within the loop, this line prints the current day number using an f-string.
    zoo.simulate_day() # The simulate_day method simulates a day in the virtual zoo, including interactions with the animals.
    print("\n") # this line prints a newline character (\n) to create a blank line in the output. This is done to separate the output for each day and make it more readable.

# Remove an animal from the zoo
zoo.remove_animal(zebra)
print("Zebby has left the zoo.\n")

# Simulate one more day
print("Final Day:")
zoo.simulate_day()
 