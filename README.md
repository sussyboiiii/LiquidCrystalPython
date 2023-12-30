# LCD Emulator Project

This project is a Python-based LCD (Liquid Crystal Display) emulator. It is designed to simulate the behavior of an LCD, mimicking the functionality of an Arduino LCD. The emulator allows you to display text and other information on a virtual LCD screen, making it particularly useful for testing and debugging applications that use an LCD display without needing the physical hardware.

The purpose of this project was to test the display logic of an e-bike display project ([vesc_lcd](https://github.com/sussyboiiii/vesc_lcd)) without needing an Arduino or LCD. As there wasn't anyway to do this without an arduino before, I made this repo.

https://github.com/sussyboiiii/lcd_emulator/assets/90244617/2b281fca-d0cf-4127-9088-709247ffaccd


## Project Structure

The project consists of three main Python files:

1. `lcd.py`: This is the core of the LCD emulator. It sets up a virtual LCD screen, handles input, and updates the display. It uses Pygame for the graphical interface and a UDP socket for receiving data. The emulator supports a grid of 20x4, 16x2, 16x1 and more characters, with each character being represented by a 5x8 pixel grid. It also includes mappings for a wide range of characters, allowing you to display text, numbers, and special characters.

2. `helloworld.py`: This is a demo script that sends data to the LCD emulator. It demonstrates how to send text to the emulator and how to update the display. It uses a separate process to run the LCD emulator and sends data via a UDP socket. The script includes a loop that continuously updates the display, showing a scrolling "Hello, World!" message.

3. `main.py`: This is a setup file that contains the bare minimum for getting started with the LCD emulator. It sets up a UDP socket and starts the LCD emulator in a separate process. This file serves as a template for creating your own scripts that interact with the LCD emulator.

4. `chars.py`: This file contains the definitions for custom characters. You can add your own characters to this file and they will be available for use in the LCD emulator.

## Features

- Supports virtually any LCD screen size.
- Supports custom characters.
- Mimics the functionality of the LiquidCrystal Arduino Library.

## Getting Started

To see a demonstration of the LCD emulator in action, run the `helloworld.py` script. This will display the text "Hello, World!" on the virtual LCD screen.

To get started with the LCD emulator, run the `main.py` script. This will start the LCD emulator in a separate process. You can then send data to the emulator via the UDP socket.

## Contributing

If you encounter any bugs, please feel free to open an issue or make a pull request. Thanks!
