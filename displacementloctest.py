import pygame
import driver.fanucfrontend as ffe

MOUSE_LEFT = 1
MOUSE_MIDDLE = 2
MOUSE_RIGHT = 3


def main():
    frontend = ffe.FANUCFrontEnd("http://10.162.12.191")
    frontend.reset()
    frontend.stop_motion()
    frontend.start_motion()
    status = frontend.get_status()
    pos = status['position']
    pygame.display.set_mode((500, 500))
    dimension = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                frontend.stop_motion()
                exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pygame.event.set_grab(True)
                dimension = event.button
                print("Pressed")
            elif event.type == pygame.MOUSEBUTTONUP:
                pygame.event.set_grab(False)
                print("Released")
            elif event.type == pygame.MOUSEMOTION:
                if pygame.event.get_grab():
                    if dimension == MOUSE_LEFT:  # X, Y
                        pos[0] += event.rel[0]
                        pos[1] += event.rel[1]
                    elif dimension == MOUSE_MIDDLE:  # Y, Z
                        pos[1] += event.rel[0]
                        pos[2] += event.rel[1]
                    elif dimension == MOUSE_RIGHT:  # X, Z
                        pos[0] += event.rel[0]
                        pos[2] += event.rel[1]
                    frontend.send_motion_request(pos[0], pos[1], pos[2], pos[3], pos[4], pos[5], "lca")


if __name__ == "__main__":
    main()
