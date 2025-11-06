# This allows us to use code from the open-source
# pygame library throughout this file
import pygame

# Import all of the constants
from constants import *

from logger import log_state


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
