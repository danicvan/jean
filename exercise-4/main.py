# def calc(op: dict):

#     if "sum" in op:
#         return print(op.values())

# def talks ():
    # print("Talks 08")
    # print("CALCULADORA")
    # print("#" * 10)

    # json = {"sum": "+", "sub": "-", "multi": "*", "div": "/"}

    # tuple = ("a", "b")

    # print(type(tuple))

# import random

# def talks ():

#     cube = [1, 2, 3, 4, 5, 6]

#     for item in range(1): 
#         x = random.choice(cube)
#         print(x)

# import random

# def talks():

#     file = open("text.text", "w")
#     file.write("Pega no meu bolso \n  sdsada")
#     file.close()

#     file_path = os.path.abspath("text.text")
#     print(file_path)

#     with open("text.text") as f:
#         lines = f.readlines()
#         print(lines)

import os

def talks ():
    pass

class Point:

    x = 1
    y = 0
    pass

class Car:

    wheels = None
    brand = None
    horse = None

    def __init__(self, wheels: str, horse: str, brand: str) -> None:
        self.wheels = wheels
        self.horse = horse
        self.brand = brand
        pass

    def run(self):
        pass

    def stop(self):
        pass

    def lights(self):
        pass

    def run_fast(self):
        pass

print(Car(wheels="17", horse="78", brand="Nissan").wheels)

if __name__ == "__main__":
    talks()