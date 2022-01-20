import pygame
import random
import math
pygame.init()
clock = pygame.time.Clock()
font = pygame.font.Font("FFF_Tusj.ttf", 50)
font2 = pygame.font.Font("FFF_Tusj.ttf", 30)
screenwidth = 800
screenheight = 600
screen = pygame.display.set_mode((screenwidth, screenheight))
grid = 20
colour = 255,255,255
colour2 = 255,0,0
scorenum = 1

class Apple:
    def __init__(self, colours):
        self.X = round(random.randint(0, screenwidth - grid) / grid)  * grid
        self.Y = round(random.randint(0, screenheight - grid) / grid) * grid
        self.colours = colours
    def drawApple(self):
        
        pygame.display.update(pygame.draw.rect(screen, self.colours, pygame.Rect(self.X, self.Y, 20, 20)))
     

    def redrawApple(self): 
        self.X = round(random.randint(0, screenwidth - grid) / grid)  * grid
        self.Y = round(random.randint(0, screenheight - grid) / grid) * grid
        pygame.display.update(pygame.draw.rect(screen, self.colours, pygame.Rect(self.X, self.Y, 20, 20)))
        

class Snake:
    def __init__(self, snakeX, snakeY):
        self.X = snakeX
        self.Y = snakeY
        self.snakeYspeed = 0
        self.snakeXspeed = 20
        self.snakeArr = []
        self.snakeLength = 1
        self.snakeStart = self.X, self.Y
        self.snakeArr.append(self.snakeStart)
    def draw(self):
        for i in self.snakeArr:
            pygame.draw.rect(screen, colour, pygame.Rect(i[0], i[1], 20, 20))
        pygame.display.flip()
    def move(self):
        self.Y += self.snakeYspeed
        self.X += self.snakeXspeed
        self.snakeArr.insert(0, [self.X, self.Y])
        while len(self.snakeArr) > self.snakeLength:
            self.snakeArr.pop()
            for z in range(1, len(self.snakeArr)):
                if self.snakeArr[z]== [self.X, self.Y]:
                    self.snakeLength = 1
                    global scorenum
                    scorenum = 1
                    self.X = 20
                    self.Y = 20
                    self.snakeYspeed = 0
                    self.snakeXspeed = 20
                    print(self.snakeLength)
                    return menu()
                    
        if snake.X == apple.X and snake.Y == apple.Y:
            apple.redrawApple()
            scorenum += 1
            self.snakeLength += 1
        snake.draw()
        if snake.X == apple2.X and snake.Y == apple2.Y:
            rand1 = random.randint(1,3)
            if rand1 == 1:
                self.snakeLength = 1
                scorenum = 1
                self.X = 20
                self.Y = 20
                self.snakeYspeed = 0
                self.snakeXspeed = 20
                print(self.snakeLength)
                return menu()
            else:
                apple2.redrawApple()
                scorenum += 3
                self.snakeLength += 3

    def moveSnakeDown(self):
        self.snakeYspeed = 20
        self.snakeXspeed = 0

    def moveSnakeUp(self):
        self.snakeYspeed = -20
        self.snakeXspeed = 0

    def moveSnakeRight(self):
        self.snakeYspeed = 0
        self.snakeXspeed = 20

    def moveSnakeLeft(self):
        self.snakeYspeed = 0
        self.snakeXspeed = -20
    def borders(self):
        if self.X < 0:
            self.X = screenwidth - 20
        if self.Y < 0:
            self.Y = screenheight -20
        if self.X >  screenwidth - 20:
            self.X = 0
        if self.Y > screenheight - 20:
            self.Y = 0
    def increaseSnake(self):
        for i in range (self.snakeLength):
            self.snakeArr.append(pygame.draw.rect(screen, colour, pygame.Rect(self.X, self.Y, 20, 20)))
            pygame.display.flip()

apple2 = Apple("yellow")
apple = Apple("red")
snake = Snake(20,20)

def game():
    
    running = True
    while running:
        clock.tick(10)
        screen.fill ((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    snake.moveSnakeDown()
                if event.key == pygame.K_w:
                    snake.moveSnakeUp()
                if event.key == pygame.K_d:
                    snake.moveSnakeRight()
                if event.key == pygame.K_a:
                    snake.moveSnakeLeft()
        scoretext = font2.render("score: " + str(scorenum), True, (255, 255, 255))
        screen.blit(scoretext, (0, 0))
        apple.drawApple()
        apple2.drawApple()
        snake.borders()
        snake.move() 


def menu():

    snakeText = font.render("Snake Game", True, (255, 255, 255))  
    snakeText_rect = snakeText.get_rect(center =(screenwidth / 2 , screenheight / 2 - 200))
    snakeText2 = font.render("Use WASD Keys To Move", True, (255, 255, 255))  
    snakeText2_rect = snakeText2.get_rect(center =(screenwidth / 2 , screenheight / 2 - 50))
    snakeText3 = font.render("Press Enter To Play", True, (255, 255, 255))  
    snakeText3_rect = snakeText3.get_rect(center =(screenwidth / 2 , screenheight / 2 + 50))
    running = True
    while running:
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("works") 
                    return game()
        
        screen.fill ((0, 0, 0))
        screen.blit(snakeText, snakeText_rect)
        screen.blit(snakeText2, snakeText2_rect)
        screen.blit(snakeText3, snakeText3_rect)
        pygame.display.update()
if __name__ == "__main__":
    menu()
