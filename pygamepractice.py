import pygame
from sys import exit

# FUNCTIONS
# DISPLAY SCORE


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'{current_time}', False, 'Black')
    score_rect = score_surf.get_rect(center=(400, 100))
    screen.blit(score_surf, score_rect)


# INITIATING PYGAME & SET UP BACKGROUND & TEXT
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('PyGame Practice')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/fonttype.ttf', 50)
game_active = False
start_time = 0

# LOADING GRAPHICS AND ANIMATION
# GRAPHICS AND TEXT
sky_surface = pygame.image.load('graphics/sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()

text_surface = test_font.render('PyGame Practice', False, 'Black')
title_text = test_font.render('Silly Game', False, 'White')
sub_text = test_font.render('Press Space To Play', False, 'White')

# SNAIL
snail_surface = pygame.image.load(
    'graphics/snail/snailWalk1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(600, 300))

# PLAYER
player_surface = pygame.image.load(
    'graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 300))
player_gravity = 0

# INTRO SCREEN
player_stand = pygame.image.load(
    'graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

# GAME LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -21.1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -21.1
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)

    # GAME ACTIVE MECHANICS
    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        screen.blit(text_surface, (300, 50))
        display_score()

        # SNAIL
        snail_rect.x -= 4
        if snail_rect.right <= 0:
            snail_rect.left = 800
        screen.blit(snail_surface, snail_rect)

        # PLAYER
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        # COLLISION
        if snail_rect.colliderect(player_rect):
            game_active = False

    else:
        screen.fill('Black')
        screen.blit(player_stand, player_stand_rect)
        screen.blit(title_text, (325, 50))
        screen.blit(sub_text, (250, 320))

    pygame.display.update()
    clock.tick(60)
