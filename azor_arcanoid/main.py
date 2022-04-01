from pickle import TRUE
from turtle import width
import pygame
import time
import os
pygame.font.init()


#GAME SETTINGS(variables)
#window
WIDTH, HEIGHT = 700, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Azor_arcanoid")


#IMAGE ---> board, brick, ball, board, background
#background
BACKGROUND = pygame.image.load("assets/background.png")


#board
BOARD_IMG = pygame.image.load("assets/board.png")
BOARD_WIDTH = 200
BOARD_HEIGHT = 50


#brick
#yellow brick
YELLOW_BRICK_WIDTH,YELLOW_BRICK_HEIGHT = 50, 50 
YELLOW_BRICK = pygame.transform.scale(
    pygame.image.load("assets/yellow_brick.png"), (YELLOW_BRICK_WIDTH, YELLOW_BRICK_HEIGHT))

#red brick
RED_BRICK_WIDTH,RED_BRICK_HEIGHT = 90, 70 
RED_BRICK = pygame.transform.scale(
    pygame.image.load("assets/red_brick.png"), (RED_BRICK_WIDTH, RED_BRICK_HEIGHT))


#ball
BALL_WIDTH, BALL_HEIGHT = 40, 40
BALL_IMG = pygame.transform.scale(
    pygame.image.load("assets/ball.png"), (BALL_WIDTH, BALL_HEIGHT))


#BORDER
class Border:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, window):
        pygame.draw.rect(window, (0,0,0), (self.x, self.y, self.width, self.height))

class Brick:
    def __init__(self, x, y, img) -> None:
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))


def collide(obj1, obj1_mask, obj2, obj2_mask):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1_mask.overlap(obj2_mask, (offset_x, offset_y)) != None

#MAINLOOP
def main():
    #MAIN SETTINGS
    #game physics
    FPS = 60
    run = TRUE
    clock = pygame.time.Clock()
    lives = 3

    #board
    board = pygame.Rect(WIDTH//2-BOARD_IMG.get_width()//2, HEIGHT-BOARD_IMG.get_height()-20, BOARD_WIDTH, BOARD_HEIGHT)
    board_mask = pygame.mask.from_surface(BOARD_IMG)
    vel = 5

    #ball
    ball = pygame.Rect(board.x, board.y-BALL_IMG.get_height(), BALL_WIDTH, BALL_HEIGHT)
    ball_mask = pygame.mask.from_surface(BALL_IMG)    
    ball_vel = 3
    start_ball_action = True
    ball_left_action = True
    ball_right_action = False 
    ball_up_action = False
    ball_down_action = False

    #border
    border_width = 20
    border_height = HEIGHT-border_width
    left_border = Border(0, border_width, border_width, border_height)
    right_border = Border(WIDTH-border_width, border_width, border_width, border_height)
    up_border = Border(0, 0, border_height, border_width)
    center_border = Border(border_width, HEIGHT//2+WIDTH//7, WIDTH-border_width*2-RED_BRICK_WIDTH-50, border_width)

    #font
    main_font = pygame.font.SysFont("comicsans", 50)
    live_font = pygame.font.SysFont("comicsans", 35)

    #label
    start_label = main_font.render("Press space for begin :)", 1, (255, 255, 255))
    game_over = main_font.render("Game over:(", 1, (255, 255, 255))

    #BRICK
    bricks = []
    x = 20
    y = 60
    for i in range(1, 10):
        if i % 2 and i<7:
            while True:
                if y>=455:
                    x += 90
                    y = (70*i)
                    if i == 1:
                        y+=40
                    elif i == 3:
                        y-=20 
                    break
                brick = Brick(x, y, RED_BRICK)
                bricks.append(brick)
                y += 40
        elif i <7 and i % 2 == 0:
            while True:
                if y>=455:
                    x+=50
                    y = (70*i)
                    if i == 4:
                        y-=20
                    break
                brick = Brick(x, y, YELLOW_BRICK)
                bricks.append(brick)
                y+=40
        elif i > 7:
            brick = Brick(x, y, RED_BRICK)
            bricks.append(brick)
            x+=90
            y+=20

    #DRAW FUNCTIOON
    def draw():
        WIN.blit(BACKGROUND, (0,0))
        lives_label = live_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        WIN.blit(lives_label, (580, 20))
        center_border.draw(WIN)

        for brick in bricks:
            brick.draw(WIN)

        WIN.blit(BOARD_IMG, (board.x, board.y))
        WIN.blit(BALL_IMG, (ball.x, ball.y))
        left_border.draw(WIN)
        right_border.draw(WIN)
        up_border.draw(WIN)
        if start_ball_action and lives == 3:
            WIN.blit(start_label, (WIDTH//2-start_label.get_width()//2, HEIGHT//2))
        pygame.display.update()


    #GAME_LOOP
    while run:
        draw()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        keys = pygame.key.get_pressed()

        #Start_game
        if keys[pygame.K_SPACE] and start_ball_action:
            start_ball_action = False
            ball_up_action = True

        
        #GAME PHYSICS 
        if start_ball_action == False:
            #BOARD_REMOTE
            if keys[pygame.K_d] and board.x+BOARD_IMG.get_width() < WIDTH - right_border.width:
                board.x += vel
            elif keys[pygame.K_a] and board.x > 0+left_border.width:
                board.x -= vel
            
            #BALL REMOTE
            #ball over the surface
            if len(bricks) == 0 and lives > 0:
                win = main_font.render("You won!!!", 1, (255, 255, 255))
                WIN.blit(win, (WIDTH//2-win.get_width()//2, HEIGHT//2))
                time.sleep(1.5)
                break
            
            if ball.y + BALL_IMG.get_height() > board.y + BOARD_IMG.get_height()+BALL_HEIGHT+20:
                lives-=1
                #game over
                if lives == 0:
                    WIN.blit(game_over, (WIDTH//2-game_over.get_width()//2, HEIGHT//2))
                    lives_label = live_font.render(f"Lives: {lives}", 1, (255, 255, 255))
                    WIN.blit(lives_label, (580, 20))
                    pygame.display.update()
                    time.sleep(1.5)
                    break
                #continue
                else:
                    time.sleep(1.5)
                    start_ball_action = True
                    board.x = WIDTH//2-BOARD_IMG.get_width()//2
                    board.y = HEIGHT-BOARD_IMG.get_height()-20
                    ball.x = board.x
                    ball.y = board.y-BALL_IMG.get_height()
                    ball_down_action = False
                    ball_left_action = True
                    ball_right_action = False
            #brick collision
            for brick_ in bricks:
                if collide(brick_, brick_.mask, ball, ball_mask):
                    bricks.remove(brick_)
                    if ball_up_action:
                        ball_up_action = False
                        ball_down_action = True
                    elif ball_down_action:
                        ball_down_action = False
                        ball_up_action = True

            #board_collision
            if collide(ball, ball_mask, board, board_mask):
                if ball_down_action:
                    ball_down_action = False
                    ball_up_action = True
                if ball.x + BALL_IMG.get_width() <= board.x + BOARD_IMG.get_width()//2:
                    ball_right_action = True
                    if ball_left_action:
                        ball_left_action = False
                else:
                    ball_left_action = True
                    if ball_right_action:
                        ball_right_action = False
            
            #ball_control
            #up-left
            if ball_up_action and ball_left_action:
                ball.x += ball_vel-1
                ball.y -= ball_vel

            #up-right
            elif ball_up_action and ball_right_action:
                ball.x -= ball_vel-1
                ball.y -= ball_vel
            
            #down-left
            elif ball_down_action and ball_left_action:
                ball.y += ball_vel
                ball.x += ball_vel-1
            
            #down-right
            elif ball_down_action and ball_right_action:
                ball.y += ball_vel
                ball.x -= ball_vel-1

            #border collision ---> up
            if ball_up_action:
                #center_border
                if ball.x > 20 and ball.x < center_border.width and ball.y == center_border.y+15:
                    ball_up_action = False
                    ball_down_action = True 

                #left_border
                elif ball.x <= 20:
                    ball_left_action = True
                    ball_right_action = False
                
                #right_border
                elif ball.x+BALL_IMG.get_width() >= WIDTH - border_width:
                    ball_right_action = True
                    ball_left_action = False

                #up_border
                elif ball.y <= border_width:
                    ball_up_action = False
                    ball_down_action = True

            #border collision ---> down
            if ball_down_action:
                if ball.x > 20 and ball.x < center_border.width and ball.y == center_border.y-18:
                    ball_up_action = True
                    ball_down_action = False 
                
                #left_border
                if ball.x <= 20:
                    ball_left_action = True
                    ball_right_action = False

                #right_border
                elif ball.x+BALL_IMG.get_width() >= WIDTH - border_width:
                    ball_right_action = True
                    ball_left_action = False

                #up_border
                elif ball.y <= border_width:
                    ball_up_action = False
                    ball_down_action = True


        #BALL START
        if start_ball_action:
            if ball_left_action:
                ball.x += ball_vel
                if ball.x + BALL_IMG.get_width() >= board.x+BOARD_IMG.get_width():
                    ball_left_action = False
                    ball_right_action = True
            if ball_right_action:
                ball.x -= ball_vel
                if ball.x <= board.x:
                    ball_left_action = True
                    ball_right_action = False
    main()

if __name__ == "__main__":
    main()