from random import choice
import matplotlib.pyplot as plt

class RandomWalk:

    def __init__(self):
        self.num_points = None
        self.x_step = None
        self.y_step = None
        self.x_values = []
        self.y_values = []

    def points(self):
        self.num_points = int(input("Enter Points: "))
    
    def get_x_step(self):
        x_direction = choice([1, -1])
        x_distance = choice([0, 1, 2, 3, 4])
        self.x_step = x_direction * x_distance
    
    def get_y_step(self):
        y_direction = choice([1, -1])
        y_distance = choice([0, 1, 2, 3, 4])
        self.y_step = y_direction * y_distance
    
    def fill_walk(self):
        self.x_values = [0] 
        self.y_values = [0] 

        while len(self.x_values) < self.num_points:

            self.get_x_step()
            self.get_y_step()

            if self.x_step == 0 and self.y_step == 0:
                continue

            x = self.x_values[-1] + self.x_step
            y = self.y_values[-1] + self.y_step

            self.x_values.append(x)
            self.y_values.append(y)
        
    def walk(self):
        plt.style.use('classic')
        fig, ax = plt.subplots(figsize=(8, 5), dpi=105)

        # Create a sequence of point numbers
        point_numbers = range(len(self.x_values))
        
        # Use scatter with a colormap
        ax.scatter(self.x_values, self.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=5)

        # Add the start point
        ax.scatter(0, 0, c='green', edgecolors='none', s=100)

        # Add the end point
        ax.scatter(self.x_values[-1], self.y_values[-1], c='red', edgecolors='none', s=100)

        ax.set_aspect('equal')
        
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        plt.show()

    def run(self):
        while True:
            self.points()
            self.get_x_step()
            self.get_y_step()
            self.fill_walk()
            self.walk()

            keep_running = input("Make another walk? (y/n): ")
            if keep_running == 'n':
                break

if __name__ == "__main__":
    rw = RandomWalk()
    rw.run()
