import pygame
from chars import*
import socket
import json

# Variables
host = "localhost"
port = 65432
GRID_WIDTH = 20
GRID_HEIGHT = 4
INNER_GRID_WIDTH = 5
INNER_GRID_HEIGHT = 8
SPACING_BETWEEN_GRIDS_X = 8 
SPACING_BETWEEN_GRIDS_Y = 10 
SPACING = 1
INNER_RECT_SIZE = 4
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
offset_x = 26
offset_y = 42
running = True
last_input = None
input_data = ""

# Init

s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s1.bind((host, port))
s1.setblocking(0)

pygame.init()

window_width = offset_x * GRID_WIDTH
window_height = offset_y * GRID_HEIGHT
window_size = (window_width, window_height)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("LCD")
screen.fill(BLUE)

# Function
def drawthings(array, row, column):
    global matchfound
    matchfound = array in [ph, km, ah, dgC, k1, mt, ms, bat]
    for i1 in range(INNER_GRID_WIDTH):
        for j1 in range(INNER_GRID_HEIGHT):
            index = i1 + j1 * INNER_GRID_WIDTH
            color = WHITE if array[index] == 1 else BLUE
            rect_x = (row * offset_x) + i1 * (INNER_RECT_SIZE + SPACING)
            rect_y = (column * offset_y) + j1 * (INNER_RECT_SIZE + SPACING)
            pygame.draw.rect(screen, color, (rect_x, rect_y, INNER_RECT_SIZE, INNER_RECT_SIZE))

# Loop
while running:
    matchfound = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    try:
        input, addr = s1.recvfrom(1024)

        if input:
            input_data = json.loads(input.decode())
            last_input = input_data['input']
            row1 = input_data["row"]
            column = input_data["column"]
            n1 = -1
            current_input = input_data['input'] if input_data else last_input
            if current_input is not None:
                if isinstance(current_input, int):
                    current_input = str(current_input)

                match current_input: # optional but can stay here if you dont want to be annoyed
                    case "ph1234567890": drawthings(ph, row1, column)
                    case "km1234567890": drawthings(km, row1, column)
                    case "ah1234567890": drawthings(ah, row1, column)
                    case "dgC1234567890": drawthings(dgC, row1, column)
                    case "k11234567890": drawthings(k1, row1, column)
                    case "mt1234567890": drawthings(mt, row1, column)
                    case "ms1234567890": drawthings(ms, row1, column)
                    case "bat1234567890": drawthings(bat, row1, column)

                case_names = ["ph1234567890", "km1234567890", "ah1234567890", "dgC1234567890", "k11234567890", "mt1234567890", "ms1234567890", "bat1234567890"]

                if matchfound:
                    for case_name in case_names:
                        current_input = current_input.replace(case_name, "")

                for l1 in str(current_input):
                    n1 = n1 + 1
                    row = row1 + n1
                    if row > (GRID_WIDTH - 1):
                        n1 = 0 
                        row = 0
                        row1 = 0
                        column = column + 1
                        if column > (GRID_HEIGHT - 1):
                            column = 0


                    match l1:                                       # Characters to display, feel free to add you own characters, 
                        case "0": drawthings(zero, row, column)     # I used the phind vs code extension to recreate the original 
                        case "1": drawthings(one, row, column)      # arduino lcd characters in the array format im using here
                        case "2": drawthings(two, row, column)
                        case "3": drawthings(three, row, column)
                        case "4": drawthings(four, row, column)
                        case "5": drawthings(five, row, column)
                        case "6": drawthings(six, row, column)
                        case "7": drawthings(seven, row, column)
                        case "8": drawthings(eight, row, column)
                        case "9": drawthings(nine, row, column)

                        case "A": drawthings(A, row, column)
                        case "B": drawthings(B, row, column)
                        case "C": drawthings(C, row, column)
                        case "D": drawthings(D, row, column)
                        case "E": drawthings(E, row, column)
                        case "F": drawthings(F, row, column)
                        case "G": drawthings(G, row, column)
                        case "H": drawthings(H, row, column)
                        case "I": drawthings(I, row, column)
                        case "J": drawthings(J, row, column)
                        case "K": drawthings(K, row, column)
                        case "L": drawthings(L, row, column)
                        case "M": drawthings(M, row, column)
                        case "N": drawthings(N, row, column)
                        case "O": drawthings(O, row, column)
                        case "P": drawthings(P, row, column)
                        case "Q": drawthings(Q, row, column)
                        case "R": drawthings(R, row, column)
                        case "S": drawthings(S, row, column)
                        case "T": drawthings(T, row, column)
                        case "U": drawthings(U, row, column)
                        case "V": drawthings(V, row, column)
                        case "W": drawthings(W, row, column)
                        case "X": drawthings(X, row, column)
                        case "Y": drawthings(Y, row, column)
                        case "Z": drawthings(Z, row, column)

                        case "a": drawthings(a, row, column)
                        case "b": drawthings(b, row, column)
                        case "c": drawthings(c, row, column)
                        case "d": drawthings(d, row, column)
                        case "e": drawthings(e, row, column)
                        case "f": drawthings(f, row, column)
                        case "g": drawthings(g, row, column)
                        case "h": drawthings(h, row, column)
                        case "i": drawthings(i, row, column)
                        case "j": drawthings(j, row, column)
                        case "k": drawthings(k, row, column)
                        case "l": drawthings(l, row, column)
                        case "m": drawthings(m, row, column)
                        case "n": drawthings(n, row, column)
                        case "o": drawthings(o, row, column)
                        case "p": drawthings(p, row, column)
                        case "q": drawthings(q, row, column)
                        case "r": drawthings(r, row, column)
                        case "s": drawthings(s, row, column)
                        case "t": drawthings(t, row, column)
                        case "u": drawthings(u, row, column)
                        case "v": drawthings(v, row, column)
                        case "w": drawthings(w, row, column)
                        case "x": drawthings(x, row, column)
                        case "y": drawthings(y, row, column)
                        case "z": drawthings(z, row, column)

                        case ".": drawthings(dot, row, column)
                        case ",": drawthings(comma, row, column)
                        case "+": drawthings(plus, row, column)
                        case "-": drawthings(minus, row, column)
                        case "!": drawthings(exclamation, row, column)
                        case "?": drawthings(question, row, column)
                        case "°": drawthings(degree, row, column)
                        case "=": drawthings(equals, row, column)
                        case "_": drawthings(underscore, row, column)
                        case ":": drawthings(colon, row, column)
                        case ";": drawthings(semicolon, row, column)
                        case "<": drawthings(less_than, row, column)
                        case ">": drawthings(greater_than, row, column)
                        case "[": drawthings(left_bracket, row, column)
                        case "]": drawthings(right_bracket, row, column)
                        case "%": drawthings(percentage, row, column)

                        case _: drawthings(space, row, column)

                    
                    pygame.display.flip()

    except socket.error:
        pass  