import pygame

class Snake:
    def __init__(self, block_size, start_x, start_y):
        self.block_size = block_size
        self.segments = [[start_x, start_y]]  # список сегментов змейки
        self.direction = "RIGHT"
        self.grow = False

    def move(self):
        head_x, head_y = self.segments[0]

        if self.direction == "UP":
            head_y -= self.block_size
        elif self.direction == "DOWN":
            head_y += self.block_size
        elif self.direction == "LEFT":
            head_x -= self.block_size
        elif self.direction == "RIGHT":
            head_x += self.block_size

        self.segments.insert(0, [head_x, head_y])

        if not self.grow:
            self.segments.pop()
        else:
            self.grow = False

    def change_direction(self, new_direction):
        opposite = {"UP":"DOWN", "DOWN":"UP", "LEFT":"RIGHT", "RIGHT":"LEFT"}
        if new_direction != opposite[self.direction]:
            self.direction = new_direction

    def draw(self, screen):
        for segment in self.segments:
            pygame.draw.rect(screen, "green", (segment[0], segment[1], self.block_size, self.block_size))

    def get_head_rect(self):
        head = self.segments[0]
        return pygame.Rect(head[0], head[1], self.block_size, self.block_size)


