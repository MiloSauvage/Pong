import pygame
from rect_left import RectLeft
from rect_right import RectRight
from ball import Ball


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1080, 720))
        pygame.display.set_caption("Pong")

        self.bg = pygame.image.load("bg.jpg")
        self.bg_rect = self.bg.get_rect()

        self.rect_left = RectLeft(self)
        self.rect_right = RectRight(self)

        self.ball = Ball(self)

        self.score_left = 0
        self.score_right = 0

        self.is_playing = False

    def update(self):
        font_score = pygame.font.SysFont("Segoe UI", 100)
        text_score_left = font_score.render(f"{self.score_left}", True, (255, 255, 255))
        text_score_right = font_score.render(f"{self.score_right}", True, (255, 255, 255))
        self.screen.blit(text_score_left, (450, -20))
        self.screen.blit(text_score_right, (540, -20))

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.rect_right.move_up()
        if pressed[pygame.K_DOWN]:
            self.rect_right.move_down()
        if pressed[pygame.K_a]:
            self.rect_left.move_up()
        if pressed[pygame.K_q]:
            self.rect_left.move_down()

        self.rect_left.update_bar_left()
        self.rect_right.update_bar_right()
        self.ball.update_ball()

    def check_win(self):
        if self.score_left >= 5:
            print("joueur gauche à gagner")
            self.score_left = 0
            self.score_right = 0
            self.is_playing = False
            self.ball.move = False
            self.ball.ball.x = 510
            self.ball.ball.y = 340
        if self.score_right >= 5:
            print("joueur gauche à gagner")
            self.score_left = 0
            self.score_right = 0
            self.is_playing = False
            self.ball.move = False
            self.ball.ball.x = 510
            self.ball.ball.y = 340

    def run(self):
        font = pygame.font.SysFont("Segoe UI", 100)
        text = font.render("Press SPACE for play", True, (255, 255, 255))

        running = True

        while running:

            if self.is_playing == True:

                self.screen.blit(self.bg, (0, 0))
                pygame.draw.line(self.screen, (255, 255, 255), [1080/2 - 20, 0], [1080/2 - 20, 720], 5)

                self.update()

                self.check_win()

                pygame.display.flip()
            else:
                self.screen.blit(self.bg, (0, 0))
                self.screen.blit(text, (50, 350))
                pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.is_playing = True
                        print("Lancement")
                    if event.key == pygame.K_p:
                        self.score_right += 1
                        print("Gauche :", self.score_right)
                    if event.key == pygame.K_o:
                        self.score_left += 1
                        print("Droite :", self.score_left)



