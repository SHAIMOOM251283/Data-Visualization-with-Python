import plotly.express as px
from random import randint

class Die:
    
    def __init__(self):
        self.num_dice = None
        self.sides_list = []
        self.range = None
        self.results = []
        self.frequencies = []
        self.title = None
        self.labels = None
        self.fig = None
        self.poss_results = None

    def dice_count(self):
        self.num_dice = int(input("Enter number of dice to roll: "))

    def sides(self):
        #self.sides_list = []
        for i in range(self.num_dice):
            sides = int(input(f"Enter number of sides on die {i + 1}: "))
            self.sides_list.append(sides)
                
    def get_range(self):
        self.range = int(input("Enter number of rolls: ")) 
                
    def roll(self):
        return sum(randint(1, sides) for sides in self.sides_list)
    
    def get_results(self):
        self.results = [self.roll() for _ in range(self.range)]
    
    def get_frequencies(self):
        self.poss_results = range(len(self.sides_list), sum(self.sides_list) + 1)
        self.frequencies = [self.results.count(value) for value in self.poss_results]
    
    def visualize(self):
        self.title = "Results of Rolling " + " and ".join(f"a D{sides}" for sides in self.sides_list) + f" {self.range} Times"
        self.labels = {'x': 'Result', 'y': 'Frequency of Result'}
        self.fig = px.bar(x = self.poss_results, y = self.frequencies, title = self.title, labels = self.labels)
        self.fig.show()
    
    def run(self):
        self.dice_count()
        self.sides()
        self.get_range()
        self.roll()
        self.get_results()
        self.get_frequencies()
        self.visualize()

if __name__ == "__main__":
    die = Die()
    die.run()
