# Suppose there is a hat containing 5 blue balls, 4 red balls, and 2 green balls. What is the probability that a random draw of 4 balls will contain at least 1 red ball and 2 green balls? While it would be possible to calculate the probability using advanced mathematics, an easier way is to write a program to perform a large number of experiments to estimate an approximate probability.

# For this project, you will write a program to determine the approximate probability odeff drawing certain balls randomly from a hat.

# First, create a Hat class in prob_calculator.py. The class should take a variable number of arguments that specify the number of balls of each color that are in the hat. For example, a class object could be created in any of these ways:

# hat1 = Hat(yellow=3, blue=2, green=6)
# hat2 = Hat(red=5, orange=4)
# hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

# A hat will always be created with at least one ball. The arguments passed into the hat object upon creation should be converted to a contents instance variable. contents should be a list of strings containing one item for each ball in the hat. Each item in the list should be a color name representing a single ball of that color. For example, if your hat is {"red": 2, "blue": 1}, contents should be ["red", "red", "blue"].

# The Hat class should have a draw method that accepts an argument indicating the number of balls to draw from the hat. This method should remove balls at random from contents and return those balls as a list of strings. The balls should not go back into the hat during the draw, similar to an urn experiment without replacement. If the number of balls to draw exceeds the available quantity, return all the balls.

# Next, create an experiment function in prob_calculator.py (not inside the Hat class). This function should accept the following arguments:

# hat: A hat object containing balls that should be copied inside the function.
# expected_balls: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat, set expected_balls to {"blue":2, "red":1}.
# num_balls_drawn: The number of balls to draw out of the hat in each experiment.
# num_experiments: The number of experiments to perform. (The more experiments performed, the more accurate the approximate probability will be.)
# The experiment function should return a probability.

import random
import copy

class Hat:

    def __init__(self, **kwargs):
        """Args: {"red": 2, "blue": 1}"""
        self.contents = []

        if (len(kwargs) == 0):
            print("at least one argument needed")
            quit()

        for k, v in kwargs.items():
            for i in range(v):
                self.contents.append(k)

    def draw(self, num):
        s = []
        if (num > len(self.contents)):
            return self.contents

        # random list of indices
        tl = random.sample(range(len(self.contents)), k=num)
        for i in tl:
            s.append(self.contents[i])

        tmp = [self.contents[i] for i in range(len(self.contents)) if not i in tl]
        self.contents = tmp
        return s


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected = []
    print(expected_balls)
    for k, v in expected_balls.items():
        for i in range(v):
            expected.append(k)

    hit = 0
    for ne in range(num_experiments):
        ch = copy.deepcopy(hat)
        drawn = ch.draw(num_balls_drawn)

        chk = False
        for e in expected:
            if e in drawn:
                chk = True
                drawn.remove(e)
            else:
                chk = False
                break  # failed if one element is not found in num_balls_drawn

        if chk:
            hit += 1

    return hit / num_experiments


hat = Hat(blue=8, red=2, green=6)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)
