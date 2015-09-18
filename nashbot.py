#!/usr/bin/env python

# andrew.nash
# 13/09/2015

import pygame
import sys
import random
from pygame.locals import *

# Main class
class NashBot:
    def __init__(self):
        self.displaySize = (640,480)

# Background class
class Background:
    def __init__(self,displaySize):
	    # Set background image
	    self.image = Surface(displaySize)

        # Fill the background image
	    self.image.fill(27, 210, 57)

    def draw(self, display):
	    # Draw the background to the screen
	    display.blt(self.image, (0,0))

if __name__=='__main__':
        game = NashBot()
        game.run()
