import pygame
import sys
from pygame.locals import *
import math
import random
from pygame import mixer

def all():
    pygame.init()
    # t = time.time()
    # width and height
    scr_w = 800
    scr_h = 600
    score = 0
    # screen
    screen = pygame.display.set_mode((scr_w, scr_h))
    money = 0
    money_change = 10

    over_font = pygame.font.Font('text/FFFFORWA.TTF', 64)
    money_font = pygame.font.Font('text/FFFFORWA.TTF', 16)
    restart_font = pygame.font.Font('text/FFFFORWA.TTF', 16)
    now_score_font = pygame.font.Font('text/FFFFORWA.TTF', 16)
    victory_font = pygame.font.Font('text/FFFFORWA.TTF', 64)

    # background music
    mixer.music.load('sounds/Intense ending.wav')
    mixer.music.set_volume(0.2)
    mixer.music.play(0)

    rect = Rect(0, 500, 800, 300)
    w_rect = Rect(10, 510, 780, 80)
    white = 255, 255, 255
    victories = 0
    # Icon of game
    pizza = pygame.image.load('textures/boss1.png')
    power_shoot = pygame.image.load('textures/shoot.png')
    power_speed = pygame.image.load('textures/speed.png')
    power_money = pygame.image.load('textures/points.png')
    background = pygame.image.load('textures/background.png')
    boss = pygame.image.load('textures/boss1.png')
    bossX = 1000
    bossY = 1000
    boss_health = 1000
    # FPS
    clock = pygame.time.Clock()
    # name of the game
    pygame.display.set_caption('Shmacle')
    # icon
    pygame.display.set_icon(pizza)
    speedX = 1
    # enemy
    enemy = []
    enemyX = []
    enemyY = []
    enemyX_change = []
    enemyY_change = []
    n_of_enemy = 10
    for i in range(n_of_enemy):
        enemy.append(pygame.image.load('textures/enemy_purpul.png'))
        enemy.append(pygame.image.load('textures/enemy_blue.png'))
        enemy.append(pygame.image.load('textures/enemy_yellow.png'))
        enemy.append(pygame.image.load('textures/enemy_green.png'))
        enemy.append(pygame.image.load('textures/enemy_white.png'))
        enemyX.append(random.randint(0, 736))
        enemyY.append(random.randint(64, 150))
        enemyX_change.append(speedX)
        enemyY_change.append(64)

    # player
    piface = pygame.image.load('textures/pi1.png')
    money_sound = mixer.Sound('sounds/money_sound (1).mp3')
    pifaceX = 400
    pifaceY = 400
    pifaceX_change = 5
    pifaceY_change = 5
    score_change = 100
    # bullet
    bulletImg = pygame.image.load('textures/bullet.png')
    # bulletImg = pygame.transform.scale(bulletImg, (1, 20))
    bulletX = 0
    bulletY = 0
    bulletX_change = 0
    bulletY_change = 25
    bullet_state = "ready"

    def player(x, y, piface):
        screen.blit(piface, (x, y))

    def enemy_game(x, y, enemy, i):
        screen.blit(enemy[i], (x, y))

    def boss_f():
        screen.blit(boss, (bossX, bossY))

    def boss_collision(bossX, bossY, bulletX, bulletY):
        distance = math.sqrt((bossX - bulletX) ** 2 + (bossY - bulletY) ** 2)
        if distance < 43:
            return True
        else:
            return False


    def fire_bullet(x, y):
        screen.blit(bulletImg, (x + 16, y))

    def collision(enemyX, enemyY, bulletX, bulletY):
        distance = math.sqrt((enemyX - bulletX)**2 + (enemyY - bulletY)**2)
        if distance < 27:
            return True
        else:
            return False

    def player_col(enemyX, enemyY, pifaceX, pifaceY):
        dist = math.sqrt((enemyX - pifaceX)**2 + (enemyY - pifaceY)**2)
        if dist < 42:
            return True
        else:
            return False

    def game_over_text():
        over_text = over_font.render("GAME OVER", True, (0, 0, 0))
        screen.blit(over_text, (175, 200))

    def victory_text():
        victory_text_game = victory_font.render("VICTORY", True, (0,0,0))
        screen.blit(victory_text_game, (250, 200))

    def restart():
        restart_text = restart_font.render(f"Press Enter to restart", True, (0, 0, 0))
        screen.blit(restart_text, (250, 300))

    def money_in_game():
        money_text = money_font.render(f"Money: {money}$", True, (0, 0, 0))
        screen.blit(money_text, (20, 551))

    def now_score():
        now_score_text = now_score_font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(now_score_text, (20, 525))

    def speed_button():
        screen.blit(power_speed, (346, 500))

    def shoot_button():
        screen.blit(power_shoot, (505, 500))

    def money_button():
        screen.blit(power_money, (664, 500))

    def cost_of_speed_button():
        cost_of_speed_text = money_font.render(f"500$", True, (0, 0, 0))
        screen.blit(cost_of_speed_text, (300, 560))

    def cost_of_shoot_button():
        cost_of_speed_text = money_font.render(f"700$", True, (0, 0, 0))
        screen.blit(cost_of_speed_text, (459, 560))

    def cost_of_money_button():
        cost_of_speed_text = money_font.render(f"300$", True, (0, 0, 0))
        screen.blit(cost_of_speed_text, (618, 560))

    def victories_text():
        victory_text_game = money_font.render(f"Victories: {victories}", True, (0,0,0))
        screen.blit(victory_text_game, (160, 540))

    while True:
        screen.fill((white))
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LALT] or keys[pygame.K_z] or keys[pygame.K_c] or keys[pygame.K_LEFT] or keys[pygame.K_UP] or keys[pygame.K_RIGHT] or keys[pygame.K_DOWN] or keys[pygame.K_x]:
                if bullet_state == "ready":
                    bulletSound = mixer.Sound('sounds/lazer.wav')
                    bulletSound.set_volume(0.1)
                    bulletSound.play()
                    bulletX = pifaceX
                    bulletY = pifaceY
                    bullet_state = "fire"
            if event.key == pygame.K_z and money >= 500:
                pifaceX_change += 1
                pifaceY_change += 1
                money -= 500
                money_sound.set_volume(0.2)
                money_sound.play()
            if event.key == pygame.K_c and money >= 300:
                money_change += 5
                money -= 300
                money_sound.set_volume(0.2)
                money_sound.play()
            if event.key == pygame.K_LEFT and pifaceX > 0:
                pifaceX -= pifaceX_change
                # piface_this = pygame.transform.rotate(piface_clean, -90)
            if event.key == pygame.K_UP and pifaceY > 0:
                pifaceY -= pifaceY_change
                # piface_this = pygame.transform.rotate(piface_clean, 90)
            if event.key == pygame.K_RIGHT and pifaceX < (scr_w - 64):
                pifaceX += pifaceX_change
                # piface_this = pygame.transform.rotate(piface_clean, 45)
            if event.key == pygame.K_DOWN and pifaceY < (scr_h - 165):
                pifaceY += pifaceY_change
            if event.key == pygame.K_x and money >= 700:
                bulletY_change += 3
                money -= 700
                money_sound.set_volume(0.2)
                money_sound.play()
                # piface_this = pygame.transform.rotate(piface_clean, -90)
            if event.key == pygame.K_RETURN:
                all()
        for i in range(n_of_enemy):
            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyY[i] += enemyY_change[i]
                enemyX_change[i] = speedX
            elif enemyX[i] >= 736:
                enemyX_change[i] = -speedX
                enemyY[i] += enemyY_change[i]

            colission = collision(enemyX[i], enemyY[i], bulletX, bulletY)
            if colission:
                expl = mixer.Sound('sounds/260614__kwahmah-02__pop.wav')
                expl.set_volume(0.2)
                expl.play()
                bulletY = 480
                bullet_state = "ready"
                score += score_change
                money += money_change
                speedX += 0.01
                enemyX_change[i] = speedX
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(50, 150)

            pl_col = player_col(enemyX[i], enemyY[i], pifaceX, pifaceY)
            if pl_col:
                pl_exp = mixer.Sound('sounds/explosion.wav')
                pl_exp.set_volume(0.06)
                pl_exp.play()
                pifaceX = 10000
                pifaceY = 10000
                for j in range(len(enemyX)):
                    enemyX[j] = 1000
                for j in range(len(enemyY)):
                    enemyY[j] = 1000
                game_over_text()
                # your_score()
                restart()
                mixer.music.load('sounds/BeepBox-Song (1).wav')
                mixer.music.set_volume(0.3)
                mixer.music.play(0)
                break

            if score == 1000:
                victory_text()
                restart()
                pifaceX = 1000
                pifaceY = 1000
                # mixer.music.load('sounds/Intense ending.wav')
                # mixer.music.set_volume(0.3)
                # mixer.music.play(0)
                break

            bs_Col = boss_collision(bossX, bossY, bulletX, bulletY)
            if bs_Col:
                score += 1
                bulletY = -2
                boss_health -= 10
                if boss_health <= 0:
                    bossX = 1000
                    bossY = 1000


            if enemyY[i] > 456:
                for j in range(len(enemyX)):
                    enemyX[j] = 1000
                for j in range(len(enemyY)):
                    enemyY[j] = 1000
                pifaceX = 10000
                pifaceY = 10000
                game_over_text()
                # your_score()
                restart()
                break

            enemy_game(enemyX[i], enemyY[i], enemy, i)

        if bullet_state == "fire":
            if bulletY <= 0:
                bulletX = 0
                bulletY = 0
                bullet_state = "ready"
            else:
                bulletY -= bulletY_change
                fire_bullet(bulletX, bulletY)

        pygame.draw.rect(screen, (0, 0, 0), rect)
        pygame.draw.rect(screen, (255, 255, 255), w_rect)
        player(pifaceX, pifaceY, piface)
        now_score()
        shoot_button()
        money_in_game()
        boss_f()
        money_button()
        speed_button()
        # victories_text()
        cost_of_speed_button()
        cost_of_shoot_button()
        cost_of_money_button()
        pygame.display.update()
        clock.tick(90)
all()