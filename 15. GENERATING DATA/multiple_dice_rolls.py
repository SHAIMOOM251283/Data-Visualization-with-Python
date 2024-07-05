import plotly.express as px

#from functools import reduce
#import operator

from random import randint

class Die:
    
    def __init__(self):
        self.num_dice = None
        self.num_sides = None
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
        self.num_sides = int(input("Enter number of sides on each die: "))
                
    def get_range(self):
        self.range = int(input("Enter number of rolls: ")) 
                
    def roll(self):
        return sum(randint(1, self.num_sides) for _ in range(self.num_dice))
    
    #def roll(self):
    #    return reduce(operator.mul, (randint(1, self.num_sides) for _ in range(self.num_dice)), 1)
    
    #def roll(self):
    #    rolls = [randint(1, self.num_sides) for _ in range(self.num_dice)]
    #    return reduce(lambda x, y: x * y, rolls, 1)
    
    #def roll(self):
    #    result = 1
    #    for _ in range(self.num_dice):
    #        result *= randint(1, self.num_sides)
    #    return result
    
    #def roll(self):
    #    rolls = [randint(1, self.num_sides) for _ in range(self.num_dice)]
    #    result = 1
    #    for roll in rolls:
    #        result *= roll
    #    return result
    
    def get_results(self):
        self.results = [self.roll() for _ in range(self.range)]
    
    def get_frequencies(self):
        self.poss_results = range(self.num_dice, self.num_dice * self.num_sides + 1)
        self.frequencies = [self.results.count(value) for value in self.poss_results]
    
    def visualize(self):
        self.title = f"Results of Rolling {self.num_dice} D{self.num_sides} {self.range} Times"
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
