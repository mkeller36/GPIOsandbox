import curses
from gpiozero import Robot, Motor

left=Motor(26,19)
right=Motor(16,20)
robot = Robot( left, right)

actions = { 
    curses.KEY_UP:      robot.forward,
    curses.KEY_DOWN:    robot.backward,
    curses.KEY_LEFT:    robot.left,
    curses.KEY_RIGHT:   robot.right,
}

def main(window):
    next_key = None;
    while True:
        curses.halfdelay(1)
        if next_key is None:
            key = window.getch()
        else:
            key = next_key
            next_key = None
        if key != -1:
            curses.halfdelay(3)
            action = actions.get(key)
            if action is not None:
                action()
            next_key = key
            while next_key == key:
                next_key = wwindow.getch()
            robot.stop()

curses.wrapper(main)
