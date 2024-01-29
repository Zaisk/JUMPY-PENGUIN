import pygame
import math


def main():
    # game initialization
    pygame.init()

    # load and set logo
    logo = pygame.image.load("graphics/Logo/alvie.png")
    pygame.display.set_icon(logo)
    # setting caption
    pygame.display.set_caption("Zaheer said 'R Kelly is the Best' ")

    # create a surface on screen that is 240px by 180 px
    screen = pygame.display.set_mode((900, 800))
    screen.fill("White")
    # define variable to control game loop
    running = True

    # sets the variable to control game frames
    clock = pygame.time.Clock()

    # creating a Surface data structure to later add to Display Surface
    # background_surface = pygame.image.load("graphics/Characters/birdy_2_75x75.png")
    box_surface = pygame.Surface((34, 34))

    # position of box
    box_x = 433
    box_y = 383

    # velocity and gravity variables
    velocity_x = 0
    velocity_y = 0
    gravity = 0.5

    # speed of box
    box_speed = 4

    # border dimensions
    window_width = 900
    window_height = 800

    # game loop
    while running:
        # This is the event handler, gets all events from event queue
        for event in pygame.event.get():
            # only do something if event is of type QUIT
            if event.type == pygame.QUIT:
                # exits game loop
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                distance_x = box_x - mouse_x
                distance_y = box_y - mouse_y
                distance = math.hypot(distance_x, distance_y)
                velocity_x = (distance_x / distance) * 10
                velocity_y = (distance_y / distance) * 10

        # if mouse not clicked fall by gravity
        if not pygame.mouse.get_pressed()[0]:
            velocity_y += gravity

        box_x += velocity_x
        box_y += velocity_y

        # Horizontal wrap-around (teleport to the other side)
        if box_x < 0 - box_surface.get_width():  # Left boundary
            box_x = window_width
        elif box_x > window_width:  # Right boundary
            box_x = 0 - box_surface.get_width()

        # Vertical boundary detection
        if box_y < 0:  # Top boundary
            box_y = 0
            velocity_y = 0  # To stop moving after hitting the top
        elif box_y > window_height - box_surface.get_height():  # Bottom boundary
            box_y = window_height - box_surface.get_height()
            velocity_y = 0  # Assuming you want it to stop at the bottom

        # # Boundary detection
        # if box_x < 0 or box_x > window_width - box_surface.get_width():
        #     velocity_x *= -1
        # if box_y < 0 or box_y > window_height - box_surface.get_height():
        #     velocity_y *= -1
        #     if box_y > window_height - box_surface.get_height():
        #         box_y = window_height - box_surface.get_height()  # Stick to the bottom

        # check for user inputs
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        #     box_x -= box_speed
        # if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        #     box_x += box_speed
        # if keys[pygame.K_UP] or keys[pygame.K_w]:
        #     box_y -= box_speed
        # if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        #     box_y += box_speed

        # Get mouse position
        # mouse_x, mouse_y = pygame.mouse.get_pos()
        # # Adjust position to keep the surface centered around the cursor
        # box_x = mouse_x - box_surface.get_width() // 2
        # box_y = mouse_y - box_surface.get_height() // 2
        #
        #
        #
        # # check boundaries
        # box_x = max(0, min(box_x, window_width - box_surface.get_width()))
        # box_y = max(0, min(box_y, window_height - box_surface.get_height()))

        # Clear screen before drawing
        screen.fill("White")
        # the functions that adds one surface to another
        screen.blit(box_surface, (box_x, box_y))

        # update the game per tick
        pygame.display.update()
        # 60 frames per second
        clock.tick(60)


if __name__ == "__main__":
    main()
