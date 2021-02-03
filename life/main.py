
import viz
import life

ROWS = 48
COLS = 64

class Simulation:
  def __init__(self):
    self.world = life.random_world(ROWS,COLS)

  def iterate(self):
    self.world = life.next_generation(self.world)

  def draw(self, screen):
    viz.draw_grid(screen, self.world.data, self.world.rows, self.world.cols)


def main():
  sim = Simulation()
  display = viz.Display("Life", sim.iterate, sim.draw)
  display.start()


if __name__ == '__main__':
    main()
