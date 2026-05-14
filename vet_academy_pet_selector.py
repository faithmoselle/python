"""
AUTHOR: Faith Moselle O. Paule
PROGRAM CODE: BCS13
DATE: S.Y. 2022-2023

PROGRAM: Vet Academy Pet Selection System
LANGUAGE: Python 3
TOPIC: Object-Oriented Programming (OOP) - Classes and Objects
TECH STACK: Python Standard Library

DESCRIPTION:
A virtual pet selection program for Vet Academy students. Users can choose
an animal to care for as a two-week assignment. The program displays the
animal's breed, sound, and food preferences.

CLASS STRUCTURE:
- Animal class: Blueprint for creating animal objects
  - Attributes: animal, breed, sound, food
  - Methods: display() - returns formatted animal information
"""

# ============================================================================
# CLASS DEFINITION (Blueprint for Animal objects)
# ============================================================================

class Animal:
    """
    Animal class representing a pet that students will care for.
    
    Attributes:
        animal (str): The type/name of the animal (Dog, Cat, Bird, Snake)
        breed (str): The specific breed of the animal
        sound (str): The sound the animal makes
        food (str): The food the animal eats
    """
    
    def __init__(self, animal, breed, sound, food):
        """
        Constructor method - Initializes a new Animal object.
        
        Called automatically when creating a new Animal instance.
        
        Args:
            animal (str): Type of animal (e.g., "Dog", "Cat")
            breed (str): Breed of the animal (e.g., "Golden Retriever")
            sound (str): Sound the animal makes (e.g., "Arf Arf")
            food (str): Food the animal eats (e.g., "Bones")
        """
        self.animal = animal  # Assign animal type
        self.breed = breed    # Assign breed
        self.sound = sound    # Assign sound
        self.food = food      # Assign food preference

    def display(self):
        """
        Returns formatted string containing all animal information.
        
        Returns:
            str: Formatted text with animal details including breed, sound, and food
        """
        return f"\nYour chosen pet for two weeks: {self.animal}\n\tBreed: {self.breed}\n\tSound: {self.sound}\n\tFood: {self.food}"


# ============================================================================
# CREATE ANIMAL OBJECTS (Instances of the Animal class)
# ============================================================================

# Create 4 different animal objects with their specific attributes
animal1 = Animal("Dog", "Golden Retriever", "Arf Arf", "Bones")
animal2 = Animal("Bird", "Eagle", "Chirp", "Worm")
animal3 = Animal("Cat", "Siamese", "Meow Meow", "Fish")
animal4 = Animal("Snake", "Python", "Sssss", "Meat")

# ============================================================================
# MAIN PROGRAM LOOP - USER INTERFACE
# ============================================================================

while True:
    # Display menu and get user input
    # FIX: Changed "enemy" to "animal" in the prompt
    pet = int(input("Welcome to the Vet Academy!!!\nKindly choose your animal to take care for two weeks as your assignment!\n\tAnimal 1: Dog\n\tAnimal "
                      "2: Bird\n\tAnimal 3: Cat\n\tAnimal 4: Snake\n\nYour chosen animal number: "))
    
    # Selection logic - display corresponding animal information
    if pet == 1:
        print(animal1.display())  # Display Dog info
        break  # Exit loop after valid selection
    elif pet == 2:
        print(animal2.display())  # Display Bird info
        break
    elif pet == 3:
        print(animal3.display())  # Display Cat info
        break
    elif pet == 4:
        print(animal4.display())  # Display Snake info
        break
    else:
        # FIX: Changed "1-3" to "1-4" to match actual options
        print("Please enter the number of your chosen animal 1-4:")

# Program ends after break - user has selected their pet
