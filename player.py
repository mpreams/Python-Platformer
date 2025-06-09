import pygame

class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)  # Red

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_index = 0 

    def move(self, dx, dy):
        """Move the player by dx and dy."""
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, vel):
        self.x_vel = -vel  
        if self.direction != "left":
            self.direction = "left"
            self.animation_index = 0  

    def move_right(self, vel):
        self.x_vel = vel  
        if self.direction != "right":
            self.direction = "right"
            self.animation_index = 0    

    def loop(self, vel):
        self.move(self.x_vel, self.y_vel) 

    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, self.rect)