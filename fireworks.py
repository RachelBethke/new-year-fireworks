import curses
import time
import random

def draw_fireworks(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

    stdscr.clear()
    height, width = stdscr.getmaxyx()

    for _ in range(10): #firewokrs
        x = random.randint(1, width - 2)
        explosion_height = random.randint(height // 3, height - 5)

        # upwards animation
        for y in range(height - 2, explosion_height, -1):
            stdscr.clear()
            stdscr.addstr(y, x, "|", curses.color_pair(random.randint(1, 5)))
            stdscr.refresh()
            time.sleep(0.05)

        for _ in range(5):  # duration
            color = random.randint(1, 5)
            char = random.choice(["*", "o", "+", "."])
            for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, 0)]:
                nx, ny = x + dx, explosion_height + dy
                if 0 < ny < height and 0 < nx < width:
                    stdscr.addstr(ny, nx, char, curses.color_pair(color))
            stdscr.refresh()
            time.sleep(0.1)
            stdscr.clear()

    stdscr.addstr(height // 2, width // 2 - 10, "Happy New Year!", curses.A_BOLD)
    stdscr.refresh()
    time.sleep(3)

def main():
    print("Type 'Happy New Year!' to see fireworks:")
    while True:
        user_input = input("> ")
        if user_input.lower() == "happy new year!":
            curses.wrapper(draw_fireworks)
            break

if __name__ == "__main__":
    main()
