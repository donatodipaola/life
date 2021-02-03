import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


WHITE = (255, 255, 255)
DARK_BLUE = (21, 34, 56)
BLUE = (61, 74, 96)

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FPS = 10


class Display:
  def __init__(self, title, iterate_function, draw_function):
    pygame.init()
    self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(title)
    self.clock = pygame.time.Clock()
    self.is_running = True
    self.iterate_function = iterate_function
    self.draw_function = draw_function

  def start(self):
    while self.is_running:
      self.clock.tick(FPS)
      self.events()
      self.update()
      self.draw()
    pygame.quit()

  def events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.is_running = False

  def update(self):
    self.iterate_function()

  def draw(self):
    self.screen.fill(DARK_BLUE)
    self.draw_function(self.screen)
    pygame.display.flip()


def draw_grid(screen, grid, rows, cols):
  cell_size = 10
  for i in range(rows):
    for j in range(cols):
      color = BLUE
      if grid[i][j] == 1:
        color = WHITE
      rect = pygame.Rect([j*cell_size, i*cell_size, cell_size-1, cell_size-1])
      pygame.draw.rect(screen, color, rect)

