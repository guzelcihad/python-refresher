# Import the library

import matplotlib.pyplot as plt
%matplotlib inline  

class Circle(object):
    
    # constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color

    # method
    def add_radius(self, r):
        self.radius = self.radius + r
    
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  

redCircle = Circle(10, 'red')
dir(redCircle)

redCircle.radius

redCircle.color

redCircle.radius = 1
redCircle.radius

redCircle.drawCircle()


class Rectangle(object):

    def __init__(self, width=2, height=3, color='r'):
        self.height = height
        self.width = width
        self.color = color

    