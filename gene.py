import random
# gene class declaration
# height and width variables comes from the source image in main
# has seven variables as described in homework file


class gene:

    def __init__(self, x=0, y=0, radius=0, red=0, green=0, blue=0, alpha=0):
        self.x = x
        self.y = y
        self.radius = radius
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    # random value initialization for the gene variables
    def rand_value(self):
        self.x = random.randint(-50, 180 + 50)
        self.y = random.randint(-50, 180 + 50)
        self.radius = random.randint(0, 90)
        self.red = random.randint(0, 255)
        self.green = random.randint(0, 255)
        self.blue = random.randint(0, 255)
        self.alpha = random.random()

    # function that checks whether the point is in picture or reach it
    # the first line checks inside
    # second line checks x<0 and y<0 points
    # third line checks x>width and y>height points
    def is_in_image(self):
        if (-self.radius < self.x < 180 + self.radius and -self.radius < self.y < 180 + self.radius): \
#                or (abs(self.x) < self.radius and abs(self.y) < self.radius) \
#                or ((self.x - 180) < self.radius and (self.y - 180) < self.radius):
            return True
        else:
            return False

# Printing function to print variables' values
    def print_gene(self):
        print("x: %2d, y: %2d, radius: %2d, red: %3d, green: %3d, blue: %3d, alpha: %1.2f" % (self.x, self.y, self.radius, self.red, self.green, self.blue, self.alpha))

