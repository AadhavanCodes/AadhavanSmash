import pygame
import math
import socket


def rotate(image, rect, angle):
    """
    rotate returns the rotated version of image and the rotated image's rectangle.
    """
    # Get a new imagae that is the original image but rotated
    new_image = pygame.transform.rotate(image, angle)
    # Get a new rect with the center of the old rect
    new_rect = new_image.get_rect(center=rect.center)
    return new_image, new_rect


def angleBetweenPoints(x1, y1, x2, y2):
    """
    angleBetweenPoints returns the angle between two points.
    """
    x_difference = x2 - x1
    y_differnece = y2 - y1
    return math.degrees(math.atan2(-y_differnece, x_difference))


def centeringCoords(thing, screen):
    """
    centeringCoords returns the coords that will put thing in the center of the screen.
    """
    new_x = screen.get_width() / 2 - thingy.get_width() / 2
    new_y = screen.get_height() / 2 - thingy.get_height() / 2
    return new_x, new_y


class keys_transform():

    def __init__(self):
        self.keys = {pygame.K_BACKSPACE: False,
                        pygame.K_TAB: False,
                        pygame.K_CLEAR: False,
                        pygame.K_RETURN: False,
                        pygame.K_PAUSE: False,
                        pygame.K_ESCAPE: False,
                        pygame.K_SPACE: False,
                        pygame.K_EXCLAIM: False,
                        pygame.K_QUOTEDBL: False,
                        pygame.K_HASH: False,
                        pygame.K_DOLLAR: False,
                        pygame.K_AMPERSAND: False,
                        pygame.K_QUOTE: False,
                        pygame.K_LEFTPAREN: False,
                        pygame.K_RIGHTPAREN: False,
                        pygame.K_ASTERISK: False,
                        pygame.K_PLUS: False,
                        pygame.K_COMMA: False,
                        pygame.K_MINUS: False,
                        pygame.K_PERIOD: False,
                        pygame.K_SLASH: False,
                        pygame.K_0: False,
                        pygame.K_1: False,
                        pygame.K_2: False,
                        pygame.K_3: False,
                        pygame.K_4: False,
                        pygame.K_5: False,
                        pygame.K_6: False,
                        pygame.K_7: False,
                        pygame.K_8: False,
                        pygame.K_9: False,
                        pygame.K_COLON: False,
                        pygame.K_SEMICOLON: False,
                        pygame.K_LESS: False,
                        pygame.K_EQUALS: False,
                        pygame.K_GREATER: False,
                        pygame.K_QUESTION: False,
                        pygame.K_AT: False,
                        pygame.K_LEFTBRACKET: False,
                        pygame.K_BACKSLASH: False,
                        pygame.K_RIGHTBRACKET: False,
                        pygame.K_CARET: False,
                        pygame.K_UNDERSCORE: False,
                        pygame.K_BACKQUOTE: False,
                        pygame.K_a: False,
                        pygame.K_b: False,
                        pygame.K_c: False,
                        pygame.K_d: False,
                        pygame.K_e: False,
                        pygame.K_f: False,
                        pygame.K_g: False,
                        pygame.K_h: False,
                        pygame.K_i: False,
                        pygame.K_j: False,
                        pygame.K_k: False,
                        pygame.K_l: False,
                        pygame.K_m: False,
                        pygame.K_n: False,
                        pygame.K_o: False,
                        pygame.K_p: False,
                        pygame.K_q: False,
                        pygame.K_r: False,
                        pygame.K_s: False,
                        pygame.K_t: False,
                        pygame.K_u: False,
                        pygame.K_v: False,
                        pygame.K_w: False,
                        pygame.K_x: False,
                        pygame.K_y: False,
                        pygame.K_z: False,
                        pygame.K_DELETE: False,
                        pygame.K_KP0: False,
                        pygame.K_KP1: False,
                        pygame.K_KP2: False,
                        pygame.K_KP3: False,
                        pygame.K_KP4: False,
                        pygame.K_KP5: False,
                        pygame.K_KP6: False,
                        pygame.K_KP7: False,
                        pygame.K_KP8: False,
                        pygame.K_KP9: False,
                        pygame.K_KP_PERIOD: False,
                        pygame.K_KP_DIVIDE: False,
                        pygame.K_KP_MULTIPLY: False,
                        pygame.K_KP_MINUS: False,
                        pygame.K_KP_PLUS: False,
                        pygame.K_KP_ENTER: False,
                        pygame.K_KP_EQUALS: False,
                        pygame.K_UP: False,
                        pygame.K_DOWN: False,
                        pygame.K_RIGHT: False,
                        pygame.K_LEFT: False,
                        pygame.K_INSERT: False,
                        pygame.K_HOME: False,
                        pygame.K_END: False,
                        pygame.K_PAGEUP: False,
                        pygame.K_PAGEDOWN: False,
                        pygame.K_F1: False,
                        pygame.K_F2: False,
                        pygame.K_F3: False,
                        pygame.K_F4: False,
                        pygame.K_F5: False,
                        pygame.K_F6: False,
                        pygame.K_F7: False,
                        pygame.K_F8: False,
                        pygame.K_F9: False,
                        pygame.K_F10: False,
                        pygame.K_F11: False,
                        pygame.K_F12: False,
                        pygame.K_F13: False,
                        pygame.K_F14: False,
                        pygame.K_F15: False,
                        pygame.K_NUMLOCK: False,
                        pygame.K_CAPSLOCK: False,
                        pygame.K_SCROLLOCK: False,
                        pygame.K_RSHIFT: False,
                        pygame.K_LSHIFT: False,
                        pygame.K_RCTRL: False,
                        pygame.K_LCTRL: False,
                        pygame.K_RALT: False,
                        pygame.K_LALT: False,
                        pygame.K_RMETA: False,
                        pygame.K_LMETA: False,
                        pygame.K_LSUPER: False,
                        pygame.K_RSUPER: False,
                        pygame.K_MODE: False,
                        pygame.K_HELP: False,
                        pygame.K_PRINT: False,
                        pygame.K_SYSREQ: False,
                        pygame.K_BREAK: False,
                        pygame.K_MENU: False,
                        pygame.K_POWER: False,
                        pygame.K_EURO: False}


    def transform(self, events):
        for e in events:
            if e in self.keys:
                self.keys[e] = not self.keys[e]

        return self.keys


class keyDownListener():
    """
    keyDownListener keeps track of one key and says when it gets pressed down.
    self.down will be True once every time the key is pressed and False otherwise.
    """

    def __init__(self):
        self.down = False
        self.is_up = False

    def update(self, key_pressed):
        if not key_pressed:
            self.is_up = True
            self.down = False
        else:
            if self.is_up:
                self.down = True
            else:
                self.down = False
            self.is_up = False


def getMyIP():
    """
    getMyIP returns the IP address on the computer you run it on.
    This may not work properly if you're not connected to the internet.
    (If this code seems super complicated, don't worry.. I don't understand it either  -Andy)
    """
    return str((([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")]
                 or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in
                      [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]])
                + ["no IP found"])[0])
