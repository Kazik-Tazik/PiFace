import pygame
import sys
from pygame.locals import *
import math
import random
from pygame import mixer


def all():
    pygame.init()
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

    #background music
    mixer.music.load('sounds/Intense ending.wav')
    mixer.music.set_volume(0.2)
    mixer.music.play(0)

    rect = Rect(0, 500, 800, 300)
    w_rect = Rect(10, 510, 780, 80)


    white = 255, 255, 255
    # Icon of game
    pizza = pygame.image.load('textures/piface_game.png')
    power_shoot = pygame.image.load('textures/shoot.png')
    power_speed = pygame.image.load('textures/speed.png')
    power_money = pygame.image.load('textures/points.png')
    background = pygame.image.load('textures/background.png')

    ### BOSS
    boss = pygame.image.load('textures/boss1.png')

    boss_hp_bar = pygame.image.load('textures/boss_hp_bar.png')

    boss_hp_bar_size = list(boss_hp_bar.get_size())
    boss_hp_bar_x_size = boss_hp_bar_size[0]
    boss_hp_bar_y_size = boss_hp_bar_size[1]

    boss_size = list(boss.get_rect().size)
    # print(boss_size)
    boss_x_size = boss_size[0]
    boss_y_size = boss_size[1]

    boss_hp_bar_pre_y = int((boss_x_size/boss_hp_bar_x_size) * boss_y_size)

    # print(boss_hp_bar_pre_y)

    # boss_hp_bar_arr = [range(0, boss_x_size), range(0, boss_hp_bar_pre_y)]

    boss_hp_breakpoint = [0]*10

    # print(hp_bar_arr)

    boss_hp_bar = pygame.transform.scale(boss_hp_bar, (boss_x_size, boss_hp_bar_pre_y))

    boss_breakpoint = [100000, 1000000, 50000]

    bossX = 300
    bossY = 40
    bossX_speed = 5

    boss_health = 1000
    boss_health_clear = boss_health

    # 100% from boss_width
    boss_health_x = bossX

    y_border = 10

    boss_health_y = bossY + boss_y_size + y_border

    boss_health_bar_x = boss_health_x + 20

    boss_mode = False

    for i in range(len(boss_hp_breakpoint)):
        boss_hp_breakpoint[i] = boss_hp_breakpoint[i-1] + boss_health/10

    # print(boss_hp_breakpoint)

    boss_hp_bar_h = boss_hp_bar_pre_y - 6

    boss_health_bar_y = boss_health_y  + 4

    boss_fireball = pygame.image.load('textures/fireball.png')
    boss_fireball = pygame.transform.rotate(boss_fireball, 90)

    boss_fireball_pull = [0]

    boss_fireball_x = bossX
    boss_fireball_y = bossY



    ### END BOSS BLOCK

    # FPSf
    clock = pygame.time.Clock()

    # name of the game
    pygame.display.set_caption('Piface')

    # icon
    pygame.display.set_icon(pizza)
    speedX = 0.1

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
        if boss_mode:
            screen.blit(boss, (bossX, bossY))
            screen.blit(boss_hp_bar, (boss_health_x, boss_health_y))
        else:
            return

    # def boss_collision(bossX, bossY, bulletX, bulletY):
    #     x_range = range(bossX, bossX + boss_x_size)
    #     y_range = range(bossY, bossY + boss_y_size)
    #
    #     if (bulletX in x_range) and (bulletY in y_range):
    #         return  True
    #     else:
    #         return False

    def boss_fun(bossX, bossY, bulletX, bulletY):
        x_range = range(bossX, bossX + boss_x_size)
        y_range = range(bossY + 350, bossY + boss_y_size + 350)

        aver = (max(x_range) + min(x_range)) // 2

        if (bulletX in x_range) and (bulletY in y_range):

            if bulletX in range(bossX, aver):
                return [True, 'r']

            elif bulletX in range(aver, bossX + boss_x_size):
                return [True, 'l']

        else:
            return [False]

    def fire_bullet(x, y):
        screen.blit(bulletImg, (x + 16, y))


    def collision(enemyX, enemyY, bulletX, bulletY):
        distance = math.sqrt((enemyX - bulletX)**2 + (enemyY - bulletY)**2)
        if distance < 27:
            return True
        else:
            return False


    def boss_fight(boss_health):
        if(boss_health < boss_health_clear//10):
            return  ['Ban', 3]
        else:
            return ['Ban', 1]

    def boss_fireball_move(bossX, bossY, boss_y_size):
        boss_fireball_x = bossX
        boss_fireball_y_range = list(range(bossY+boss_y_size, scr_h))
        for i in range(len(boss_fireball_y_range)):
            # print(boss_fireball_y_range[i])
            boss_fireball_y = boss_fireball_y_range[i]
            screen.blit(boss_fireball, (boss_fireball_x, boss_fireball_y))


    def player_col(enemyX, enemyY, pifaceX, pifaceY):
        dist = math.sqrt((enemyX - pifaceX)**2 + (enemyY - pifaceY)**2)
        if dist < 42:
            return True
        else:
            return False

    def boss_death(bossX, bossY, pifaceX, pifaceY):
        x_range = range(bossX, bossX + boss_x_size)
        y_range = range(bossY, bossY + boss_y_size)

        if (pifaceX in x_range) and (pifaceY in y_range):
            return False

        return True

    def game_over_text():
        over_text = over_font.render("GAME OVER", True, (0, 0, 0))
        screen.blit(over_text, (175, 200))

    def victory_text():
        victory_text_game = victory_font.render("VICTORY", True, (0,0,0))
        screen.blit(victory_text_game, (175, 200))

    def money_button():
        screen.blit(power_money, (664, 500))

    def restart():
        restart_text = restart_font.render(f"Press Enter to restart", True, (0, 0, 0))
        screen.blit(restart_text, (175, 300))

    def money_in_game():
        money_text = money_font.render(f"Money: {money}$", True, (0, 0, 0))
        screen.blit(money_text, (20, 551))

    def now_score():
        now_score_text = now_score_font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(now_score_text, (20, 525))

    def shoot_button():
        screen.blit(power_shoot, (558, 500))

    def speed_button():
        screen.blit(power_speed, (452, 500))

    def enemy_death(n_of_enemy, enemyX, enemyY, pifaceX, pifaceY):
        for i in range(n_of_enemy):
            pl_col = player_col(enemyX[i], enemyY[i], pifaceX, pifaceY)

            if pl_col:
                pl_exp = mixer.Sound('sounds/explosion.wav')
                pl_exp.set_volume(0.06)
                pl_exp.play()
                game_over_text()
                # restart()
                mixer.music.load('sounds/BeepBox-Song (1).wav')
                mixer.music.set_volume(0.3)
                mixer.music.play(0)
                return False

        return True  # This line should be outside the for loop

    while True:

        while not boss_death(bossX, bossY, pifaceX, pifaceY):
                screen.fill((white))
                screen.blit(background, (0, 0))
                game_over_text()
                pygame.display.update()
                clock.tick(60)
                quit()

        while not enemy_death(n_of_enemy, enemyX, enemyY, pifaceX, pifaceY):
                screen.fill((white))
                screen.blit(background, (0, 0))
                game_over_text()
                pygame.display.update()
                clock.tick(60)
                # quit()

        while boss_death(bossX, bossY, pifaceX, pifaceY): # and enemy_death(bossX, bossY, pifaceX, pifaceY):
            screen.fill((white))
            screen.blit(background, (0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LALT:
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
            if boss_mode:
                boss_health_x = bossX
                boss_health_y = bossY + boss_y_size + y_border
                boss_health_bar_y = boss_health_y + 4
                boss_health_bar_x = boss_health_x #+ 20

                boss_health_delta = boss_health_clear-boss_health

                for i in range(len(boss_hp_breakpoint)):
                    if boss_health_delta >= boss_hp_breakpoint[i]:
                        if i == 0:
                            pygame.draw.rect(screen, (255,0,0), Rect(boss_health_bar_x+10, boss_health_bar_y, (boss_x_size/10 + 2), (boss_hp_bar_h)))
                        else:
                            pygame.draw.rect(screen, (255, 0, 0),
                                             Rect(boss_health_bar_x + ((boss_x_size / 10)*i), boss_health_bar_y, (boss_x_size / 10 + 2),
                                                  (boss_hp_bar_h)))


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
            if boss_mode:
                boss_f()
            now_score()
            shoot_button()
            money_in_game()
            money_button()
            speed_button()
            pygame.display.update()
            clock.tick(60)
all()