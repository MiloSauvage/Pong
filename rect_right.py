import pygame


class RectRight:
    def __init__(self, game):
        self.game = game
        self.bar_set = [1080 - 100, 160, 50, 240]
        self.bar_right = pygame.Rect(self.bar_set[0], self.bar_set[1], self.bar_set[2], 400)

    def update_bar_right(self):
        self.bar_set[1] = self.bar_right.y
        self.bar_set[3] = self.bar_set[1] + 240
        pygame.draw.rect(self.game.screen, (255, 255, 255), self.bar_right)

    def move_up(self):
        self.bar_right.y -= 2
        #print(self.bar_set)

    def move_down(self):
        self.bar_right.y += 2
        #print(self.bar_set)
