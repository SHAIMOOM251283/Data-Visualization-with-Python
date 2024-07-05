from random import choice
import matplotlib.pyplot as plt

class RandomWalk:

    def __init__(self):
        self.num_points = None
        self.x_values = []
        self.y_values = []

    def points(self):
        self.num_points = int(input("Enter Points: "))

    def fill_walk(self):
        self.x_values = [0] 
        self.y_values = [0] 

        while len(self.x_values) < self.num_points:

            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def walk(self):
        plt.style.use('seaborn-v0_8')
        fig, ax = plt.subplots(figsize=(8, 5), dpi=105)
        ax.plot(self.x_values, self.y_values, color='red', linewidth=1)

        ax.plot(0, 0, 'go', markersize=10)

        ax.plot(self.x_values[-1], self.y_values[-1], 'bo', markersize=10) 

        ax.set_aspect('equal')
    
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        plt.tight_layout()
        plt.show()

    def run(self):
        while True:
            self.points()
            self.fill_walk()
            self.walk()

            keep_running = input("Make another walk? (y/n): ")
            if keep_running == 'n':
                break

if __name__ == "__main__":
    rw = RandomWalk()
    rw.run()
    
    
