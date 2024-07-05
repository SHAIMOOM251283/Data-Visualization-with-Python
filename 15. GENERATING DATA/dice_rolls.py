import plotly.express as px
from random import randint

class Die:
    
    def __init__(self):
        self.d1_sides = None
        self.d2_sides = None
        self.num_rolls = None
        self.results = []
        self.frequencies = []
        self.title = None
        self.labels = None
        self.fig = None
        self.poss_results = None

    def set_dice1_sides(self):
        self.d1_sides = int(input("Enter number of sides for Dice 1: "))
    
    def set_dice2_sides(self):
        self.d2_sides = int(input("Enter number of sides for Dice 2: "))
           
    def set_num_rolls(self):
        self.num_rolls = int(input("Enter number of rolls: ")) 
                
    def roll_dice(self):
        return randint(1, self.d1_sides) + randint(1, self.d2_sides)
    
    def generate_results(self):
        self.results = [self.roll_dice() for _ in range(self.num_rolls)]
    
    def calculate_frequencies(self):
        max_result = self.d1_sides + self.d2_sides
        self.poss_results = range(2, max_result + 1)
        self.frequencies = [self.results.count(value) for value in self.poss_results]

    def visualize_results(self):
        self.title = f"Results of Rolling a D{self.d1_sides} and a D{self.d2_sides} Dice {self.num_rolls} Times"
        self.labels = {'x': 'Result', 'y': 'Frequency of Result'}
        self.fig = px.bar(x = self.poss_results, y = self.frequencies, title = self.title, labels = self.labels)
        self.fig.show()
    
    def run(self):
        self.set_dice1_sides()
        self.set_dice2_sides()
        self.set_num_rolls()
        self.generate_results()
        self.calculate_frequencies()
        self.visualize_results()

if __name__ == "__main__":
    die = Die()
    die.run()
