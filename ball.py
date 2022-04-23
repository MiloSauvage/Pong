import pygame
import random


class Ball:
    def __init__(self, game):
        self.game = game
        self.ball_set = [510, 340, 20, 20]
        self.ball = pygame.Rect(self.ball_set[0], self.ball_set[1], self.ball_set[2], self.ball_set[3])

        self.move = False

        self.time = 0
        self.time_max = 500

        self.alea_x = [-1, 1]
        self.alea_y = [1, -1]

        self.x_start = 0
        self.y_start = 0

        self.count = 0

    def difficulty(self):
        if self.count >= 3:
            #print("+")
            self.x_start = self.x_start * 1.3
            self.y_start = self.y_start * 1.3
            self.count = 0

    def direction_start(self):
            choice_x = random.randint(0, 1)
            choice_y = random.randint(0, 1)
            self.x_start = self.alea_x[choice_x]
            self.y_start = self.alea_y[choice_y]
            #print(self.x_start, self.y_start)
            self.move = True

    def move_ball(self):
        #print(self.move)
        self.ball.x += self.x_start

        self.ball.y += self.y_start
        #print(self.ball.x, self.ball.y)

    def timer_ball(self):
        if self.move == False:
            self.time += 1
            if self.time >= self.time_max:
                self.time = 0
                self.direction_start()

    def check_collide(self):

        if self.ball.colliderect(self.game.rect_left.bar_left):
            self.x_start = self.x_start * (-1)
            self.count += 1
        if self.ball.colliderect(self.game.rect_right.bar_right):
            self.x_start = self.x_start * (-1)
            self.count += 1

        if self.ball.y >= 720:
            self.y_start = self.y_start * (-1)
        if self.ball.y <= 0:
            self.y_start = self.y_start * (-1)

        if self.ball.x >= 1080:
            self.x_start = self.x_start * (-1)
            self.game.score_left += 1
            self.move = False
            self.ball.x = 510
            self.ball.y = 340
        if self.ball.x <= 0:
            self.x_start = self.x_start * (-1)
            self.game.score_right += 1
            self.move = False
            self.ball .x = 510
            self.ball.y = 340

    def update_ball(self):
        #print(self.time)
        self.timer_ball()
        if self.move == True:
            self.check_collide()
            self.move_ball()
            self.difficulty()
        self.ball_set[0] = self.ball.x
        self.ball_set[1] = self.ball.y
        pygame.draw.rect(self.game.screen, (255, 255, 255), self.ball)
        #print("vitesse :", self.x_start)



