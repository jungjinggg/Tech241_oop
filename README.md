# OOP
**Object-Oriented Programming** is a method of organising code around objects which are instances of classes.
### Classes
**a class** is a blueprint that obtains objects which provides initial values(variables or attributes) and methods.

**Dog** class is a template which can be used for all dogs, it has a variable: animal_kind, and a method: bark.

<img src="D:\Python project\Tech 241\python_oop\dog_class.jpg"/>

Create instances: fido and lassie, which are objects created from Dog class. So that objects' attributes and methods can be accessed. 

<img src="D:\Python project\Tech 241\python_oop\dog_class_phase1.png"/>

When assign global variables, the variables in the class can be overwritten.

<img src="D:\Python project\Tech 241\python_oop\dog_class_phase2.png"/>

### Four pillars

<img src="D:\Python project\Tech 241\python_oop\animal_class.png"/>

#### 1. Abstraction
The idea of abstraction is to not know the implementations in order to use it. From the diagram, Animal class 
```python
class Animal:

    def __int__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        return "One breath at a time, in and out"

    def eat(self):
        return "Nom Nom Nom"

    def procreate(self):
        return "Time to find a mate"

    def move(self):
        return "Onwards and upwards"

# breathe is abstracted
cat = Animal()
print(cat.breathe())
```
#### 2. Inheritance
Inheritance is when a class inherits attributes and methods from parent/base classes. The diagram shows that Reptile class inherits from Animal class. This allows the Reptile class to possess attributes and methods from the Animal class and its own. 
```python
from animal import Animal

class Reptile(Animal):

    def __init__(self):
        super().__init__()          # initialises the parent/base class - inherit everything from Animal
        self.cold_blood = True
        self.tetrapod = None        # Not all reptile have 4 legs
        self.heart_chambers = [3, 4]
        self.amniotic_eggs = None   # Not true for all reptiles

    # Private
    def __seek_heat(self):
        return "it's chilly outside, I need a sunbed"

    # Protected
    # this is where to access seek_heat method
    def _show_seek_heat(self):
        print(self._seek_heat())

    def hunt(self):
        return "Hunting prey"

    def use_venom(self):
        return "If I have it, may as well use it"

    def attract_mate_through_scent(self):
        print("Time to put on the aftershave")


bulbasaur = Reptile()
print(bulbasaur.hunt())     # Reptile class
print(bulbasaur.breathe())  # Animal class
```
#### 3. Encapsulation
Encapsulation remove or limit what you can access to the specified classes. 

**Types of modifiers in Python** 

* Public - anyone can access it anywhere

* Private -  accessible only within the class itself

        # Private
        # __ in front of the name
        def __seek_heat(self):
            return "it's chilly outside, I need a sunbed"

        # This function is used to call __seek_heat method
        def _show_seek_heat(self):
            print(self._seek_heat())

* Protected - accessible within the class and it's subclasses
    
        # Protected
        # _ in front of the name
        def _show_seek_heat(self):
            print(self._seek_heat())

    
```python
from reptile import Reptile

class Snake(Reptile):

    def __int__(self):
        super().__init__()
        self.forked_tongue = True
        self.cold_blood = True
        self.venom = None   # Not all snakes are venomous
        self.limbs = False
        self.tetrapod = False

    def use_tongue_to_smell(self):
        return "Do I say it smells nice, or tastes nice..?"

sidney = Snake()

print(sidney.breathe())             # Animal method
print(sidney.seek_heat())           # Reptile method
print(sidney.use_tongue_to_smell()) # Snake method
```
#### 4. Polymorphism 
This usually occurs when inheriting classes where objects can have the same names but able to do different things. From the diagram, Python class inherits from Snake which is a child class of Reptile class. In Animal class and Python class, there are two breathe methods, but they act differently. So that when breathe method is called in Python class file, it will print whatever it is defined. 
```python
from snake import Snake

class Python(Snake):
    def __int__(self):
        super().__int__()
        self.large = True
        self.two_lungs = True
        self.venom = False

    def digest_large_prey(self):
        return "Ok, hand me the stretchy pants"

    def constrict(self):
        return "and...squeeeeeze"

    def climb(self):
        return "Up we go"

    def shed_skin(self):
        return "I'm growing out of this now"

    def breathe(self):
        return "I am breathing but I am a Python"

peter = Python()

print(peter.breathe())              # Python class
print(peter.eat())                  # Animal class
print(peter.hunt())                 # Reptile class
print(peter.use_tongue_to_smell())  # Snake class
```