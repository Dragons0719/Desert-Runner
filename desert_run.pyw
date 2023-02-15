# Created by Elijah Rotenberger
# Last changed: 2/15/23
# Version 1.0.0

import pygame
import random


SCREEN_WIDTH = 640
SCREEN_LENGTH = 480

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_LENGTH))
pygame.display.set_caption("Desert Run")

score = 0
hs_text = "Assets\highscore.txt"

icon_img = pygame.image.load("Assets\\Sprite\\sprite.ico").convert_alpha()

icon = pygame.display.set_icon(icon_img)

sprite_frames = []
for i in range(0, 26):
    frame = pygame.image.load(f"Assets\\Sprite\\sprite-{i}.png").convert_alpha()
    sprite_frames.append(frame)

frame_index = 0
frame_timer = 0

sprite_x = 80
sprite_y = 350



def menu():
    image = pygame.image.load("Assets\Pictures\start_menu.png")
    while True: 
        pygame.font.init()
        screen.blit(image, (0,0))
        custom_font = pygame.font.Font("Assets\Fonts\Rye-Regular.ttf", 30)
        try:
            highestscore = int(gethighscore())
        except:
            highestscore = 0
        highscore_text = custom_font.render("High Score: {}".format(highestscore), True, (0,0,0))
        text_rect = highscore_text.get_rect(center=(SCREEN_WIDTH/2, 105))
        screen.blit(highscore_text, text_rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range (300,325) and event.pos[1] in range (200,228):
                    game()
            if event.type == pygame.KEYDOWN:
                creditslp()

def game():
    global score, sprite_x, sprite_y, frame_index, frame_timer

    image = pygame.image.load("Assets\Pictures\infbg.png")
    image = pygame.transform.scale(image, (640,480))
    bgx = 0
    jump = 0
    score = 0
    falling = False
    jumpcount = 0
    cactus_x = 700
    cactus_speed = 2
    cactus = pygame.image.load("Assets\Pictures\cactusobs.png")
    cactus = pygame.transform.scale(cactus, (80,80))
    sprite_y = 350
    while True: 
        pygame.font.init()
        screen.blit(image, (bgx-640,0))
        screen.blit(image, (bgx,0))
        screen.blit(image, (bgx+640,0))
        custom_font = pygame.font.Font("Assets\Fonts\Rye-Regular.ttf", 30)
        score_text = custom_font.render("Score: {}".format(score), True, (0,0,0))
        screen.blit(score_text, (230, 30))
        frame_timer += 1
        if frame_timer == 6: # change this value to control animation speed
            frame_timer = 0
            frame_index = (frame_index + 1) % len(sprite_frames)
        sprite = sprite_frames[frame_index]
        sprite_rect = sprite.get_rect(center=(sprite_x, sprite_y))
        screen.blit(sprite, sprite_rect)
        bgx = bgx-1
        if bgx <= -640:
            bgx=0
        if jump == 1:
            sprite_y = sprite_y - 6
            jumpcount += 1
            if jumpcount > 40:
                jumpcount = 0
                jump = 0
                falling = True
                
        c_rect = screen.blit(cactus, (cactus_x, 330))
        cactus_x -= cactus_speed
        if cactus_x < -50:
            score += 100
            cactus_x = random.randint(700,800)
            print(score)
        if falling == True:
            sprite_y += 1
            if sprite_y >= 350:
                sprite_y = 350
                falling = False
        if c_rect.colliderect(sprite_rect):
            endgame()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range (300,325) and event.pos[1] in range (200,228):
                    print("play")
            if event.type == pygame.KEYDOWN:
                jump = 1

def endgame():
    global score, SCREEN_LENGTH, SCREEN_WIDTH
    image = pygame.image.load("Assets\Pictures\game_over.png")
    while True: 
        screen.blit(image, (0,0))
        pygame.font.init()
        try:
            highestscore = int(gethighscore())
        except:
            highestscore = 0
        custom_font = pygame.font.Font("Assets\Fonts\Rye-Regular.ttf", 30)
        score_text = custom_font.render("Score: {}".format(score), True, (0,0,0))
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH/2, 100))
        screen.blit(score_text, score_rect)
        if(highestscore < score):
            with open("Assets\highscore.txt", "w") as f:
                f.write(str(score))
            nhs_text = custom_font.render("New High Score!", True, (0,0,0))
            screen.blit(nhs_text, (230, 50))
        highscore_text = custom_font.render("High Score: {}".format(highestscore), True, (0,0,0))
        text_rect = highscore_text.get_rect(center=(SCREEN_WIDTH/2, 135))
        screen.blit(highscore_text, text_rect)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                game()

def gethighscore():
    with open("Assets\highscore.txt", "r") as f:
        return f.read()

def creditslp():
    image = pygame.image.load("Assets\Pictures\credits.png")
    while True: 
        screen.blit(image, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                menu()


menu()