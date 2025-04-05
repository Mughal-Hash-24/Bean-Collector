import pygame
import random

class Object(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("bean.png").convert()  # Replace with your image file
        self.image.set_colorkey((0, 0, 0))  # Set white as the transparent color if needed
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width - self.rect.width)
        self.rect.y = random.randint(-height, -self.rect.height)
    
    def update(self):
        self.rect.y += b_vel  # Constant velocity

class Mug(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("mug.png").convert()  # Replace with your image file
        self.image.set_colorkey((0, 0, 0))  # Set black as the transparent color if needed
        self.rect = self.image.get_rect()
        self.rect.x = w_rect
        self.rect.y = h_rect

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= vel

        if keys[pygame.K_RIGHT] and self.rect.right < width:
            self.rect.x += vel

        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= vel

        if keys[pygame.K_DOWN] and self.rect.bottom < height:
            self.rect.y += vel

all_objects = pygame.sprite.Group()

pygame.init()

pygame.mixer.init()

screen = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Bean Collector By Mughal")

image = pygame.image.load("bean.png")

bg = pygame.image.load("background.png")

bean = pygame.image.load("bean.png")

pygame.display.set_icon(image)

screen_color = (155, 0, 255)

color_dark = (100, 100, 100)
color_light = (170, 170, 170)

timer_color = (150, 75, 0)

timer_width = 150
timer_height = 30

timer_vel = 0.5

timer_posx = 5
timer_posy = 465

collision_sound = pygame.mixer.Sound("collision_sound.wav")
score_sound = pygame.mixer.Sound("score_sound.wav")

score = 0

x = 50
y = 50

clock = pygame.time.Clock()

count = 1

w_rect = 225
h_rect = 300

w_but = 360
h_but = 460

vel = 5

b_vel = 5

small_font = pygame.font.SysFont("Arial", 30)

# score_font = pygame.font.SysFont("Arial", 30)

# scr = 0

# score = score_font.render("Score"+str(scr))

text = small_font.render("quit" , True, (255, 255, 255))

width = screen.get_width()
height = screen.get_height()

running = True

mug = Mug()  # Create the Mug object

while running:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if w_but <= mouse[0] <= w_but+140 and h_but <= mouse[1] <= h_but+40:
                running = False

    if score == 100:
        vel = 4
        b_vel = 6
    
    elif score == 200:
        vel = 3
        b_vel = 7

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and mug.rect.left > 0:
        mug.rect.x -= vel

    if keys[pygame.K_RIGHT] and mug.rect.right < width:
        mug.rect.x += vel

    # if keys[pygame.K_UP] and mug.rect.top > 0:
    #     mug.rect.y -= vel

    # if keys[pygame.K_DOWN] and mug.rect.bottom < height:
    #     mug.rect.y += vel

    timer_width -= timer_vel

    if timer_width <= 0:
        running = False

    all_objects.update()  # Update all the objects

    screen.blit(bg, dest=(0, 0))

    if random.randint(0, 100) < 5:
        new_object = Object()
        all_objects.add(new_object)

    # Check for collision between mug and beans
    collision = pygame.sprite.spritecollide(mug, all_objects, True)
    if collision:
        score += 1
        print("Collision detected! Score:", score)
        timer_width = 150
        collision_sound.play()
        if score % 50 == 0:
            score_sound.play()

    score_text = small_font.render("Score: " + str(score), True, (150, 75, 0))
    screen.blit(score_text, (10, 10))


    all_objects.draw(screen)
    screen.blit(mug.image, mug.rect)

    pygame.draw.rect(screen, timer_color, (timer_posx, timer_posy, timer_width, timer_height))

    mouse = pygame.mouse.get_pos()

    if w_but <= mouse[0] <= w_but+140 and h_but <= mouse[1] <= h_but+40:
        pygame.draw.rect(screen,color_light,pygame.Rect(w_but,h_but,140,40))
    else:
        pygame.draw.rect(screen, color_dark, pygame.Rect(w_but, h_but, 140, 40))

    screen.blit(text, dest=(w_but+40, h_but))
    # screen.blit(score, dest = (200, 400))

    clock.tick(60)

    pygame.display.update()

pygame.quit()