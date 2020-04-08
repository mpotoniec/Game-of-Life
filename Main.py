import pygame
import sys

from GameOfLife import Game_window
from Button import Button


WIDTH, HEIGHT = 1000, 775
FPS = 60
BACKGROUND = (255, 255, 255)

def get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    button.click()

def update():
    game_of_life.update()
    for button in buttons:
        button.update(mouse_pos, game_state=state)

def draw():
    window.fill(BACKGROUND)
    for button in buttons:
        button.draw()
    game_of_life.draw()

def running_get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    button.click()

def running_update():
    game_of_life.update()
    for button in buttons:
        button.update(mouse_pos, game_state=state)
    if frame_count%(FPS/speed) == 0:
        game_of_life.evaluate()

def running_draw():
    window.fill(BACKGROUND)
    for button in buttons:
        button.draw()
    game_of_life.draw()

def paused_get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    button.click()

def paused_update():
    game_of_life.update()
    for button in buttons:
        button.update(mouse_pos, game_state=state)

def paused_draw():
    window.fill(BACKGROUND)
    for button in buttons:
        button.draw()
    game_of_life.draw()

def mouse_on_grid(pos):
    if pos[0] > 25 and pos[0] < WIDTH - 250:
        if pos[1] > 25 and pos[1] < HEIGHT - 25:
            return True
    else: return False

def click_cell(pos):
    grid_pos = [pos[0] - 25, pos[1] - 25]
    grid_pos[0] = grid_pos[0]//12
    grid_pos[1] = grid_pos[1]//12
    game_of_life.grid[grid_pos[1]] [grid_pos[0]].alive = not(game_of_life.grid[grid_pos[1]] [grid_pos[0]].alive)

def make_buttons():
    buttons = []

    buttons.append(Button(window, 825, 50, 100, 30, text = 'run/pause',
                          colour = (130, 130, 130), hover_colour=(170, 170, 170), bold_text=False, function = run_pause, state = ''))

    
    buttons.append(Button(window, 825, 80, 100, 30, text = 'set grid',
                          colour = (130, 130, 130), hover_colour=(170, 170, 170), bold_text=False, function = set_grid, state = ''))

    buttons.append(Button(window, 825, 200, 100, 30, text = 'niezmienne',
                          colour = (130, 130, 130), hover_colour=(170, 170, 170), bold_text=False, function = constantly, state = ''))

    buttons.append(Button(window, 825, 230, 100, 30, text = 'glider',
                          colour = (130, 130, 130), hover_colour=(170, 170, 170), bold_text=False, function = glider, state = ''))

    buttons.append(Button(window, 825, 260, 100, 30, text = 'oscylator',
                          colour = (130, 130, 130), hover_colour=(170, 170, 170), bold_text=False, function = oscilator, state = ''))

    buttons.append(Button(window, 825, 290, 100, 30, text = 'losowy',
                          colour = (130, 130, 130), hover_colour=(170, 170, 170), bold_text=False, function = random_cells_set, state = ''))
    
    buttons.append(Button(window, 825, 600, 100, 30, text = 'speed up',
                          colour = (130, 130, 130), hover_colour=(170, 170, 170), bold_text=False, function = speedUP, state = ''))

    buttons.append(Button(window, 825, 630, 100, 30, text = 'slow down',
                          colour = (130, 130, 130), hover_colour=(170, 170, 170), bold_text=False, function = slowDOWN, state = ''))


    return buttons

def run_pause():
    global state
    if state == 'paused' or state == 'setting':
        state = 'running'
    elif state == 'running':
        state = 'paused'

def set_grid():
    global state
    state = 'setting'
    game_of_life.reset_grid(60,60)

def constantly():
    global state
    state = 'setting'
    game_of_life.set_custom_cell_vars(0)

def glider():
    global state
    state = 'setting'
    game_of_life.set_custom_cell_vars(1)  

def oscilator():
    global state
    state = 'setting'
    game_of_life.set_custom_cell_vars(2)

def random_cells_set():
    global state
    state = 'setting'
    game_of_life.set_custom_cell_vars(3)

def speedUP():
    global speed
    if speed == 5:
        speed = 10
    elif speed == 10:
        speed = 30
    else: speed = 60
    

def slowDOWN():
    global speed
    if speed == 60:
        speed = 30
    elif speed == 30:
        speed = 10
    else: speed = 5

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
game_of_life = Game_window(window, 25, 25)
buttons = make_buttons()
state = 'setting'
frame_count = 0
speed = 60

running = True

while running:
    frame_count += 1
    mouse_pos = pygame.mouse.get_pos()
    if state == 'setting':
        get_events()
        update()
        draw()
    if state == 'running':
        running_get_events()
        running_update()
        running_draw()
    if state == 'paused':
        paused_get_events()
        paused_update()
        paused_draw()
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
sys.exit()
