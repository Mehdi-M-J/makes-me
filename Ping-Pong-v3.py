import pygame
from pygame.locals import *
import sys

class PingPongGame:
    """
    Class to handle the Ping Pong game.

    Attributes:
    - width: int
        Width of the game window.
    - height: int
        Height of the game window.
    - ball_radius: int
        Radius of the ball.
    - paddle_width: int
        Width of the paddles.
    - paddle_height: int
        Height of the paddles.
    - ball_x: int
        X-coordinate of the ball.
    - ball_y: int
        Y-coordinate of the ball.
    - ball_dx: int
        Change in X-coordinate of the ball.
    - ball_dy: int
        Change in Y-coordinate of the ball.
    - paddle1_y: int
        Y-coordinate of the first paddle.
    - paddle2_y: int
        Y-coordinate of the second paddle.
    - score1: int
        Score of player 1.
    - score2: int
        Score of player 2.
    """

    def __init__(self, width: int, height: int):
        """
        Constructor to instantiate the PingPongGame class.

        Parameters:
        - width: int
            Width of the game window.
        - height: int
            Height of the game window.
        """

        self.width = width
        self.height = height
        self.ball_radius = 12
        self.paddle_width = 20
        self.paddle_height = 190
        self.ball_x = width // 2
        self.ball_y = height // 2
        self.ball_dx = 3
        self.ball_dy = 3
        self.paddle1_y = height // 2 - self.paddle_height // 2
        self.paddle2_y = height // 2 - self.paddle_height // 2
        self.score1 = 2
        self.score2 = 2
        # self.paddle_speed = 90

    def handle_events(self):
        """
        Handles the events in the game.

        Returns:
        - bool:
            Returns False if the user quits the game, otherwise returns True.
        """

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    self.paddle2_y -= 70
                elif event.key == K_DOWN:
                    self.paddle2_y += 70
                elif event.key == K_w:
                    self.paddle1_y -= 70
                elif event.key == K_s:
                    self.paddle1_y += 70

        return True

    def update_ball(self):
        """
        Updates the position of the ball.

        Returns:
        - bool:
            Returns False if the ball goes out of bounds, otherwise returns True.
        """

        self.ball_x += self.ball_dx
        self.ball_y += self.ball_dy

        if self.ball_y - self.ball_radius <= 0 or self.ball_y + self.ball_radius >= self.height:
            self.ball_dy *= -1

        if self.ball_x - self.ball_radius <= 0:
            self.score2 += 1
            self.reset_ball()
        elif self.ball_x + self.ball_radius >= self.width:
            self.score1 += 1
            self.reset_ball()

        if self.ball_x - self.ball_radius <= self.paddle_width and self.paddle1_y <= self.ball_y <= self.paddle1_y + self.paddle_height:
            self.ball_dx *= -1
        elif self.ball_x + self.ball_radius >= self.width - self.paddle_width and self.paddle2_y <= self.ball_y <= self.paddle2_y + self.paddle_height:
            self.ball_dx *= -1

        return True

    def reset_ball(self):
        """
        Resets the position of the ball to the center of the game window.
        """

        self.ball_x = self.width // 2
        self.ball_y = self.height // 2

    def draw(self, screen):
        """
        Draws the game elements on the screen.

        Parameters:
        - screen: pygame.Surface
            The game window surface.
        """

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), (self.width // 2 - 1, 0, 2, self.height))
        pygame.draw.circle(screen, (255, 255, 0), (self.ball_x, self.ball_y), self.ball_radius)
        pygame.draw.rect(screen, (0, 255, 0), (0, self.paddle1_y, self.paddle_width, self.paddle_height))
        pygame.draw.rect(screen, (0, 255, 0), (self.width - self.paddle_width, self.paddle2_y, self.paddle_width, self.paddle_height))

        font = pygame.font.Font(None, 36)
        text1 = font.render(str(self.score1), True, (255, 0, 0))
        text2 = font.render(str(self.score2), True, (255, 0, 0))
        screen.blit(text1, (self.width // 2 - 50, 10))
        screen.blit(text2, (self.width // 2 + 30, 10))

    def run(self):
        """
        Runs the Ping Pong game.
        """

        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ping Pong Game")

        clock = pygame.time.Clock()

        while True:
            if not self.handle_events():
                break

            if not self.update_ball():
                break

            self.draw(screen)
            pygame.display.update()
            clock.tick(900)

        pygame.quit()

# Starting the Ping Pong game
if __name__ == "__main__":
    game = PingPongGame(1250, 600)
    game.run()