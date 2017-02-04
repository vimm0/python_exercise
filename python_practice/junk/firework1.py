import curses
from curses import wrapper
import random

max_x = 0
max_y = 0

class Particle(object):
    def __init__(self, x, y, vx, vy, expiry):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.expiry = expiry
        self.visible = True

    def next(self):
        self.x += self.vx
        self.y += self.vy
        self.expiry -= 1

        if self.expiry <= 0:
            self.visible = False
            return True

        return False

    def render(self, stdscr):
        if not self.visible:
            return
        if self.expiry < 3:
            char = '+'
        else:
            char = '*'
        max_y, max_x = stdscr.getmaxyx()

        if 0 < self.x < max_x and 0 < self.y < max_y:
                if self.expiry %2==0:
                    stdscr.addstr(self.y, self.x, char,curses.A_BLINK)
                elif self.expiry%3==0:
                    stdscr.addstr(self.y, self.x, char,curses.color_pair(1))
                else:
                    stdscr.addstr(self.y, self.x, char,curses.color_pair(2))
def main(stdscr):

    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    max_y, max_x = stdscr.getmaxyx()
    print (max_x, max_y)

    stdscr.clear()

    particles = []

    for i in range(0, 1):
        particles.append(Particle(x=40, y=20, vx=0, vy=-1, expiry=5))

    while True:
        stdscr.clear()

        for i, particle in enumerate(particles):
            particle.render(stdscr)

            will_disappear = particle.next()

            if will_disappear:
                del particles[i]

                for j in range(-1, 2):
                    for k in range(-1, 2):
                        particles.append(Particle(x=particle.x, y=particle.y, vx=j, vy=k, expiry=5))


        stdscr.refresh()
        stdscr.getkey()

        # sleep(1)

    # # This raises ZeroDivisionError when i == 10.
    # for i in range(0, 10):
    #
    #     v = i-10
    #     stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))

    stdscr.refresh()
    stdscr.getkey()

wrapper(main)
