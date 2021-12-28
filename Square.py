from dataclasses import dataclass
import pygame, sys
from pygame.locals import *

@dataclass
class Square:
    position_x: int
    position_y: int
    blockSize: int