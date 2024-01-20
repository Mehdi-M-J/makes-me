import pygame
import random

# Initialize the game
pygame.init()

# Set up the game window
window_width = 999
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Ping Pong Game")

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0 , 255 , 0)
YELLOW = (255 , 255, 0)
BLUE = (0 , 0 , 255)
AQUA = (0 , 255 , 255)

# Set up the game clock
clock = pygame.time.Clock()

# Set up the game variables
ball_radius = 12
ball_x = window_width // 2
ball_y = window_height // 2
ball_dx = random.choice([-2, 2])
ball_dy = random.choice([-2, 2])

paddle_width = 10
paddle_height = 120
paddle_speed = 10

paddle1_x = 10
paddle1_y = window_height // 2 - paddle_height // 2
paddle1_dy = 0

paddle2_x = window_width - paddle_width - 10
paddle2_y = window_height // 2 - paddle_height // 2
paddle2_dy = 0

score1 = 1
score2 = 1
font = pygame.font.Font( None, 36)

def update_ball():
    """
    Update the position of the ball and check for collisions with the paddles and walls.
    """

    global ball_x, ball_y, ball_dx, ball_dy, score1, score2

    # Update the ball's position
    ball_x += ball_dx
    ball_y += ball_dy

    # Check for collision with the paddles
    if ball_x <= paddle1_x + paddle_width and paddle1_y <= ball_y <= paddle1_y + paddle_height:
        ball_dx = abs(ball_dx)
    elif ball_x >= paddle2_x - ball_radius and paddle2_y <= ball_y <= paddle2_y + paddle_height:
        ball_dx = -abs(ball_dx)

    # Check for collision with the walls
    if ball_y <= 0 or ball_y >= window_height - ball_radius:
        ball_dy = -ball_dy

    # Check for scoring
    if ball_x <= 0:
        score2 += 2
        reset_ball()
    elif ball_x >= window_width:
        score1 += 2
        reset_ball()

def reset_ball():
    """
    Reset the position and direction of the ball.
    """

    global ball_x, ball_y, ball_dx, ball_dy

    ball_x = window_width // 2
    ball_y = window_height // 2
    ball_dx = random.choice([-2, 2])
    ball_dy = random.choice([-2, 2])

def update_paddle1():
    """
    Update the position of paddle 1 based on user input.
    """

    global paddle1_y, paddle1_dy

    paddle1_y += paddle1_dy

    # Keep the paddle within the window bounds
    if paddle1_y < 0:
        paddle1_y = 0
    elif paddle1_y > window_height - paddle_height:
        paddle1_y = window_height - paddle_height

def update_paddle2():
    """
    Update the position of paddle 2 based on user input.
    """

    global paddle2_y, paddle2_dy

    paddle2_y += paddle2_dy

    # Keep the paddle within the window bounds
    if paddle2_y < 0:
        paddle2_y = 0
    elif paddle2_y > window_height - paddle_height:
        paddle2_y = window_height - paddle_height

def draw_objects():
    """
    Draw the ball, paddles, and score on the game window.
    """

    window.fill(BLACK)

    # Draw the ball
    pygame.draw.circle(window, RED, (ball_x, ball_y), ball_radius)

    # Draw the paddles
    pygame.draw.rect(window, GREEN, (paddle1_x, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(window, GREEN, (paddle2_x, paddle2_y, paddle_width, paddle_height))

    # Draw the score
    score_text = font.render(f"{score1} : {score2}", True, AQUA)
    window.blit(score_text, (window_width // 2 - score_text.get_width() // 2, 10))

    # Update the game display
    pygame.display.update()

def handle_events():
    """
    Handle the user input events.
    """

    global paddle1_dy, paddle2_dy

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddle1_dy = -paddle_speed
            elif event.key == pygame.K_s:
                paddle1_dy = paddle_speed
            elif event.key == pygame.K_UP:
                paddle2_dy = -paddle_speed
            elif event.key == pygame.K_DOWN:
                paddle2_dy = paddle_speed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                paddle1_dy = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                paddle2_dy = 0

def game_loop():
    """
    The main game loop.
    """

    while True:
        # Handle user input events
        handle_events()

        # Update game objects
        update_ball()
        update_paddle1()
        update_paddle2()

        # Draw game objects
        draw_objects()

        # Set the game FPS
        clock.tick(300)

# Start the game loop
game_loop()