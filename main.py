import pygame, sys
from Square import Square
from pygame.locals import *
import numpy as np

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
HEIGHT = 400
WIDTH = 400
ROWS = 20

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    drawGrid()
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def crearCuadrados(blockSize: int) -> list:
    lista = []
    for x in range(0, WIDTH, blockSize):
        for y in range(0, HEIGHT, blockSize):
            lista.append(Square(x, y, blockSize))
    return np.array(lista)

def drawGrid():
    blockSize = 20 #Set the size of the grid block
    listaCuadrados = crearCuadrados(blockSize)
    for cuadrado in listaCuadrados:
        rect = pygame.Rect(cuadrado.position_x, cuadrado.position_y, blockSize, blockSize)
        pygame.draw.rect(SCREEN, (255,0,255), rect, 1)
    #print(listaCuadrados)
    #print(len(listaCuadrados))
    print(listaCuadrados[1])
main()
