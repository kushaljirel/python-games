import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows = 0
    w = 0
    def __init__(self, start, dirny=0, color=(225,0,0)):
        pass
    def move(self, dirnx, dirny):
        pass
    def draw(self, surface, eyes=False):
        pass
class snake(object):
    body = []
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self, head)
        self.dirnx = 0
        self.dirny = 1
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()

        for key in keys():
            if keys[pygame.K_left]:
                self.dirnx = -1
                self.dirny = 0
                self.turns[self.head.pos[:]] = [set.dirnx, self.dirny]


            elif keys[pygame.K_RIGHT]:
                self.dirnx = 1
                self.dirny = 0
                self.turns[self.head.pos[:]] = [set.dirnx, self.dirny]

            elif keys[pygame.K_UP]:
                self.dirnx = 0
                self.dirny = -1
                self.turns[self.head.pos[:]] = [set.dirnx, self.dirny]

            elif keys[pygame.K_DOWN]:
                self.dirnx = 0
                self.dirny = 1
                self.turns[self.head.pos[:]] = [set.dirnx, self.dirny]



        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                trun = self.turns[p]
                c.move(turn[0], turn[1])
                if i === len(self.body) - 1:
                    self.turns.pop(p)
            else:
                


    def reset(self, pos):
        d
    def addCube(self):
        d
    def draw(self, face):
        d

def drawGrid(w, rows, surface):
    sizeBtwn = w // rows
     
    x = 0
    y = 0
    for l in range(rows):
        x += sizeBtwn
        y +=sizeBtwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))

def redrawWindow(surface):
    global rows, width
    surface.fill((0,0,0))
    drawGrid(width, rows, surface)
    pygame.display.update()
    

def randomSnack(rows, items):
    

def message_box(subject, content):
    pass

def main():
    global width, rows
    width  = 500
    height = 500
    rows = 20
    win = pygame.dispaly.set_mode(width, height)
    s = snake((255,0,0), (10,10))
    flag = True

    clock = pygame.time.Clock()
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow(win)


rows = 
w = 
h = 

cube.rows = rows
cube.w = w

main()
