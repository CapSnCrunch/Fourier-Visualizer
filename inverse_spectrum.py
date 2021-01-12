import cv2 # pip install opencv-python
import numpy as np # pip install numpy
import pygame # pip install pygame
from pygame.locals import *
import pygame.surfarray as surfarray

'''
    Draw on the pygame window and see the spectrum of the image update in real time!
    You can mess with the view_size parameter to zoom in and out on the spectrum.
    Press r to refresh your drawing window.
    Press numpad values to load preselected images.
    Scrolling will shift the drawing color along a grey scale all the way up to white for erasing.

    The most interesting drawings are small dots and lines near the center of the window. Most others will just look like noise.

    Press s to save a inverse-spectrum to the designated save location. The purpose of this is to attempt to get plain images which have some desired spectrum.
    This is not currently working but it will be a cool way to 'encode' images with a Fourier Transform.
'''

fft2, ifft2 = np.fft.fft2, np.fft.ifft2
fftshift, ifftshift = np.fft.fftshift, np.fft.ifftshift

### CHANGE THESE TO USE PRESELECTED IMAGES ###
current_folder = 'Fourier-Visualizer/Images/' # Change depending on your local setup
save_directory = 'Fourier-Visualizer/Inverse Spectra/' # Change depending on your local setup

images = ['bee.jpg', 'flowers.jpg', 'trees.jpg', 'forest.jpg', 'nebula.jpg', 'water.jpg', 'clouds.jpg', 'mountain.jpg', 'city.jpg', 'buildings.jpg']

# Parameters
width = 500
height = 500
view_size = 250


img = np.zeros((width, height))

def main():
    pygame.init()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    #WHITE = (0, 0, 0)
    #BLACK = (255, 255, 255)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('DRAW HERE')
    screen.fill(WHITE)

    color = BLACK

    #pygame.draw.line(screen, BLACK, (0, 250), (500, 250), 1)
    #pygame.draw.line(screen, BLACK, (250, 0), (250, 500), 1)

    center = (width / 2, height / 2)

    mouse_position = (0, 0)
    drawing = False
    last_pos = None
    clock = pygame.time.Clock()

    saved = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == MOUSEMOTION:
                if drawing:
                    mouse_position = pygame.mouse.get_pos()
                    # if mouse_position[0] < 256 and mouse_position[1] < 256:
                    if True:
                        if last_pos is not None:
                            pygame.draw.line(screen, color, last_pos, mouse_position, 1)
                        last_pos = mouse_position

            elif event.type == MOUSEBUTTONUP:
                mouse_position = (0, 0)
                last_pos = None
                drawing = False

            elif event.type == MOUSEBUTTONDOWN:
                drawing = True
                # Check for scrolling up or down
                if event.button == 5: 
                    color = tuple([min(x + 10, 255) for x in color])
                elif event.button == 4: 
                    color = tuple([max(x - 10, 0) for x in color])

            elif event.type == KEYDOWN:
                # Refresh the screen
                if event.key == 114:
                    screen.fill(WHITE)
                    saved = False
                    #pygame.draw.line(screen, BLACK, (0, 250), (500, 250), 1)
                    #pygame.draw.line(screen, BLACK, (250, 0), (250, 500), 1)
                # Load image
                elif 1073741913 <= event.key <= 1073741922:
                    try:
                        if event.key == 1073741922:
                            img = pygame.image.load(current_folder + images[0])
                        else:
                            img = pygame.image.load(current_folder + images[event.key - 1073741912]) 
                        screen.blit(img, (0, 0))
                    except:
                        screen.fill(WHITE)

                elif event.key == 115 and not saved:
                    cv2.imwrite(save_directory + 'inverse-spectra.jpg', img)
                    saved = True

        pygame.display.update()
        clock.tick(30) # Limit the frame rate to 30 FPS.

        # Grab current drawing
        x = pygame.surfarray.array2d(screen)
        # x = x[0:250, 0:250]

        # Normalization
        # x = x / np.max(x)

        # Take spectrum of current drawing
        x = x.transpose()
        x = fftshift(ifft2(x))

        # Grab center view window from current spectrum
        img = np.array(x, dtype = np.uint8)
        img = img[int(center[0] - view_size / 2):int(center[0] + view_size / 2), int(center[1] - view_size / 2):int(center[1] + view_size/2)]

        # Record max for rescaling later
        img_max = np.max(img)

        # Normalization
        img = img / img_max

        # print(np.min(img), np.max(img))

        # Scale view window back up to width x height
        img = np.kron(img, np.ones((int(width / view_size), int(height / view_size))))

        cv2.imshow('Image', img)
        cv2.waitKey(30) # Gives time to handle user input

main()
