# Handwritten Digit Recognition

This project implements a real-time handwritten digit recognition system using Pygame and TensorFlow.

## Features

- Real-time drawing interface using Pygame
- Digit recognition using a pre-trained TensorFlow model
- Instant prediction display
- Ability to clear the drawing board

## Requirements

- Python 3.x
- Pygame
- NumPy
- TensorFlow
- Keras
- OpenCV

## Installation

1. Clone this repository:
    ```bash
   git clone https://github.com/meetgupta7388/Hand-Digit-Recognition-Project.git
2. Install the required packages:
    ```bash
    pip install pygame numpy tensorflow opencv-python
3. Ensure you have the pre-trained model file `my_model.h5` in the `python_project` directory.

## Usage

- Run the main script:
     ```bash
     python handwritten.py
- Draw a digit on the black screen using your mouse.
- The program will automatically recognize and display the predicted digit.
- Press 'n' to clear the screen and draw a new digit.

## How it works

1. The script creates a drawing interface using Pygame.
2. As you draw, it tracks the mouse movements to create the digit.
3. When you release the mouse button, it processes the drawn image.
4. The image is resized and normalized to match the input format of the neural network.
5. The pre-trained model predicts the digit, and the result is displayed on the screen.

## Customization

- You can toggle image saving by setting `IMAGESAVE = True` in the script.
- Adjust `WINDOWSSIZEX` and `WINDOWSSIZEY` to change the window size.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check this project if you want to contribute.



    



   
