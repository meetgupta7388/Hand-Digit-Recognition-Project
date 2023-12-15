# Import necessary libraries
import pygame,sys
from pygame.locals import *
import numpy as np
import tensorflow as tf
from keras.models import load_model
import cv2
import os

# Set up window dimensions and colors
WINDOWSSIZEX = 640
WINDOWSSIZEY = 480
BOUNDARYINC = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Toggle to save images
IMAGESAVE = False

# Load pre-trained model
MODEL = load_model("python_project\my_model.h5")
LABELS = {0: "Zero", 1: "One", 2: "Two", 3: "Three",
          4: "Four", 5: "Five", 6: "Six", 7: "Seven",
          8: "Eight", 9: "Nine"}

# Initialize Pygame
pygame.init()
Font = pygame.font.Font(pygame.font.get_default_font(), 18)
DISPLAYSURFACE = pygame.display.set_mode((WINDOWSSIZEX, WINDOWSSIZEY))
pygame.display.set_caption("Digit Board ")

# Initialize variables for drawing
iswriting = False
number_xcord = []
number_ycord = []
img_cnt = 1
PREDICT = True

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # Mouse motion event when drawing
        if event.type == MOUSEMOTION and iswriting:
            xcord, ycord = event.pos
            pygame.draw.circle(DISPLAYSURFACE, WHITE, (xcord, ycord), 4, 0)
            number_xcord.append(xcord)
            number_ycord.append(ycord)
        # Mouse button down event to start drawing
        if event.type == MOUSEBUTTONDOWN:
            iswriting = True
        # Mouse button up event to stop drawing and process the drawn digit
        if event.type == MOUSEBUTTONUP:
            iswriting = False
            number_xcord = sorted(number_xcord)
            number_ycord = sorted(number_ycord)

            # Define the bounding box around the drawn digit
            rect_min_x, rect_max_x = max(number_xcord[0] - BOUNDARYINC, 0), min(WINDOWSSIZEX, number_xcord[-1] + BOUNDARYINC)
            rect_min_y, rect_max_y = max(number_ycord[0] - BOUNDARYINC, 0), min(number_ycord[-1] + BOUNDARYINC, WINDOWSSIZEX)

            number_xcord = []
            number_ycord = []

            # Extract the drawn digit as an array and convert to float32
            img_arr = np.array(pygame.PixelArray(DISPLAYSURFACE))[rect_min_x:rect_max_x, rect_min_y:rect_max_y].T.astype(np.float32)

            # Save the drawn image if IMAGESAVE is True
            if IMAGESAVE:
                cv2.imwrite("image.png")
                img_cnt += 1

            # Process the drawn digit and display prediction
            if PREDICT:
                image = cv2.resize(img_arr, (28, 28))
                image = np.pad(image, (10, 10), "constant", constant_values=0)
                image = cv2.resize(image, (28, 28)) / 255

                label = str(LABELS[np.argmax(MODEL.predict(image.reshape(1, 28, 28, 1)))])
                textSurface = Font.render(label, True, RED)

                textRecObj = textSurface.get_rect()
                textRecObj.left, textRecObj.bottom = rect_min_x, rect_max_y

                # Display the predicted label on the Pygame window
                DISPLAYSURFACE.blit(textSurface, textRecObj)
        # Keydown event to clear the drawing board
        if event.type == KEYDOWN:
            if event.unicode == "n":
                DISPLAYSURFACE.fill(BLACK)
    
    # Update the Pygame display
    pygame.display.update()
 