from asciimatics.effects import Cycle , Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
import asciimatics

def demo(screen):
    effects = [
        Cycle(
            screen,
            FigletText("TABLE TENNIS", font='big'),
            screen.height // 2 - 8),
        Cycle(
            screen,
            FigletText("SCOREBOARD", font='big'),
            screen.height // 2 + 3),
        Stars(screen, (screen.width + screen.height) // 2)
    ]
    screen.play([Scene(effects, 500)])

Screen.wrapper(demo)
