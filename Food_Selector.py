# Python project focused on making quicker eating decisions. This code is region based from personal experience. 

import random
import time

class Food():

    '''This program is a food place generator with specific food types \
and the times of day available to compliment it.
    You can always change the list of places associated with the food types.'''

    def FastFood(self):
        # A list of fast food places
        fastFood_List = ["Whataburger", 'Burger King', 'McDonalds', \
        'Panda Express', "Bush's Chicken", 'Tacos from the lake', \
        'Chik-Fil-A']
        return random.choice(fastFood_List)

    def RestFood(self):
        # A list of restaurant food places
        restFood_list = ['Tensai', 'Chilis', 'Fudds', 'Peter Piper']
        return random.choice(restFood_list)

    def HomeFood(self):
        # Default sentence for homemade foods
        return "Whatever mom or grandma wants to make."

    def CafeFood(self):
        # A list of cafes
        cafe_List = ['Deli Deli', 'Sweet Tweets', 'Downtown Cupcake Shop', \
        'Mostassa', 'Magic Cafe']
        return random.choice(cafe_List)

    def Rand(self):
        # Returns a food type based on the instances above
        foodList = [Food().FastFood(),Food().RestFood(),Food().HomeFood()]
        return random.choice(foodList)

class TimeOfDay():
    def BreakfastFood(self):
        b_list = ['IHOP', 'McDonalds', 'Cracker Barrel']
        return random.choice(b_list)
    def DessertFood(self):
        d_list = ['Ice Cream', 'Cotton Candy', 'Chocolate', 'Cake', 'Candy', \
        'Gummy Bears']
        return random.choice(d_list)

while True: # <- used for reiteration of loop in the case of a invalid input.
    user_input = int(input("Where would you like to eat? Press 1 for Fast Food, \
2 for Restaurant Food, 3 for Homemade Food, 4 for Cafe Food, 5 for Random, \
6 for Breakfast, 7 for Lunch, 8 for Dinner, or 9 for food for all times of the day?"))
    if user_input in range(0,6):
        if user_input == 1:
            print("Loading...")
            time.sleep(0.5)
            print(Food().FastFood()) # For fast food

        elif user_input == 2:
            print("Loading...")
            time.sleep(0.5)
            print(Food().RestFood()) # For restaurant food

        elif user_input == 3:
            print("Loading...")
            time.sleep(0.5)
            print(Food().HomeFood()) # For homemade food

        elif user_input == 4:
            print("Loading...")
            time.sleep(0.5)
            print(Food().CafeFood()) # For cafe food

        else:
            print("Loading...")
            time.sleep(0.5)
            print(Food().Rand()) # For a random selection of food

    elif user_input in range(6,10):
        if user_input == 6:
            print("Loading...")
            time.sleep(0.5)
            print(TimeOfDay().BreakfastFood()) # For breakfast food

        elif user_input == 7:
            print("Loading...")
            time.sleep(0.5)
            print(Food().FastFood()) # For lunch food

        elif user_input == 8:
            print("Loading...")
            time.sleep(0.5)
            print(Food().RestFood()) # For dinner food

        else:
            print("Loading...")
            time.sleep(0.5)
            print('For breakfast: ' + TimeOfDay().BreakfastFood())
            print('For lunch: ' + Food().FastFood())
            print('For dinner: ' + Food().RestFood())
            print('For dessert: ' + TimeOfDay().DessertFood())

    else:
        # What to do in the case of a invalid input
        print("You have used an invalid input.")
        print("Please try again but with a number from the list.")

