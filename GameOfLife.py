import pygame
import random
from Cell import *
vec = pygame.math.Vector2

class Game_window():

    def __init__(self, screen, x, y):
        self.screen = screen
        self.pos = vec(x, y)
        self.width, self.height = 725, 725
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()

        self.rows = 60
        self.cols = 60

        self.grid = [[Cell(self.image, x,  y) for x in range(self.cols) ] for y in range(self.rows)]
        self.set_neighbours()

    
    def update(self):
        self.rect.topleft = self.pos
        for row in self.grid:
            for cell in row:
                cell.update()

    def draw(self):
        self.image.fill((255,255,255))
        for row in self.grid:
            for cell in row:
                cell.draw()
        self.screen.blit(self.image, (self.pos.x, self.pos.y))

    def set_neighbours(self):
        for x in range(self.cols):
            for y in range(self.rows):
                
                #Periodyczne warunki brzegowe
                self.grid[x][y].neighbours.append(self.grid[(x - 1) % self.cols][y]) #left
                self.grid[x][y].neighbours.append(self.grid[(x + 1) % self.cols][y]) #right
                self.grid[x][y].neighbours.append(self.grid[x][(y - 1) % self.rows]) #top
                self.grid[x][y].neighbours.append(self.grid[x][(y + 1) % self.rows]) #bottom
                self.grid[x][y].neighbours.append(self.grid[(x - 1) % self.cols][(y - 1) % self.rows]) #left top
                self.grid[x][y].neighbours.append(self.grid[(x - 1) % self.cols][(y + 1) % self.rows]) #left bottom
                self.grid[x][y].neighbours.append(self.grid[(x + 1) % self.cols][(y - 1) % self.rows]) #right top
                self.grid[x][y].neighbours.append(self.grid[(x + 1) % self.cols][(y + 1) % self.rows]) #right bottom


    def reset_grid(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell(self.image, x,  y) for x in range(self.cols) ] for y in range(self.rows)]
        self.set_neighbours()

    def set_custom_cell_vars(self, option):

        if option == 0: #niezmienne
            self.grid[30][30].alive = True
            self.grid[30][31].alive = True
            self.grid[32][30].alive = True
            self.grid[32][31].alive = True
            self.grid[31][32].alive = True
            self.grid[31][29].alive = True
        elif option == 1: #glider
            self.grid[10][10].alive = True
            self.grid[10][11].alive = True
            self.grid[9][9].alive = True
            self.grid[9][10].alive = True
            self.grid[8][11].alive = True
        elif option == 2: #oscylator
            self.grid[20][20].alive = True
            self.grid[21][20].alive = True
            self.grid[22][20].alive = True
        elif option == 3: #losowe wypełnienie
            for row in self.grid:
                for cell in row:
                    cell.alive = random.choice([True, False])

    def evaluate(self):

        to_change = [[[False] for x in range(self.cols) ] for y in range(self.rows)]
        for row in self.grid:
            for cell in row:
                cell.alive_neighbours = 0
                for neighbour in cell.neighbours:
                    if neighbour.alive: cell.alive_neighbours += 1

        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):

                if cell.alive:
                    if (cell.alive_neighbours < 2) or (cell.alive_neighbours > 3): to_change[y][x] = True
                else:
                    if cell.alive_neighbours == 3: to_change[y][x] = True

        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):

                if to_change[y][x] == True: cell.alive = not(cell.alive)
