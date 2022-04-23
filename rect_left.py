import pygame


class RectLeft:
    def __init__(self, game):
        self.game = game
        self.bar_set = [50, 160, 50, 240]
        self.bar_left = pygame.Rect(self.bar_set[0], self.bar_set[1], self.bar_set[2], 400)

    def update_bar_left(self):
        self.bar_set[1] = self.bar_left.y
        self.bar_set[3] = self.bar_set[1] + 240
        pygame.draw.rect(self.game.screen, (255, 255, 255), self.bar_left)

    def move_up(self):
        self.bar_left.y -= 2
        #print(self.bar_set)

    def move_down(self):
        self.bar_left.y += 2
        #print(self.bar_set)

