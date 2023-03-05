from pygame import *

run = True


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (80, 80))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Hero(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


class Enemy(GameSprite):
    side = "up"

    def update(self):
        if self.rect.y <= 145:
            self.side = "down"
        if self.rect.y >= 470:
            self.side = "up"
        if self.side == "up":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed


class Enemy_1(GameSprite):
    side = "up"

    def update(self):
        if self.rect.y <= 475:
            self.side = "down"
        if self.rect.y >= 690:
            self.side = "up"
        if self.side == "up":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed


class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        sprite.Sprite.__init__(self)
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface([self.width, self.height])
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect = Rect(wall_x, wall_y, wall_width, wall_height)

    def draw_wall(self):
        draw.rect(window, (self.color_1, self.color_2, self.color_3),
                  (self.rect.x, self.rect.y, self.width, self.height))


win_width = 1280
win_height = 768
display.set_caption("Лабиринт")
window = display.set_mode((win_width, win_height))
w1 = Wall(0, 0, 0, 0, 0, 1200, 10)  # верхняя стена
w2 = Wall(0, 0, 0, 0, 0, 10, 650)  # самая левая стена
w3 = Wall(0, 0, 0, 290, 115, 10, 100)  # N3
w4 = Wall(0, 0, 0, 120, 115, 10, 540)  # N2
w5 = Wall(0, 0, 0, 120, 115, 175, 10)  # N1
w6 = Wall(0, 0, 0, 150, 215, 150, 10)  # N4
w7 = Wall(0, 0, 0, 400, 115, 10, 220)  # N6
w8 = Wall(0, 0, 0, 140, 215, 10, 240)  # N5
w9 = Wall(0, 0, 0, 250, 325, 150, 10)  # N7
w10 = Wall(0, 0, 0, 250, 330, 10, 30)  # N8
w11 = Wall(0, 0, 0, 250, 350, 350, 10)  # N9
w12 = Wall(0, 0, 0, 140, 450, 350, 10)  # N10
w13 = Wall(0, 0, 0, 600, 350, 10, 305)  # N11
w14 = Wall(0, 0, 0, 485, 450, 10, 100)  # N12
w15 = Wall(0, 0, 0, 460, 650, 150, 10)  # N14
w16 = Wall(0, 0, 0, 460, 550, 35, 10)  # N13
w17 = Wall(0, 0, 0, 460, 475, 10, 80)  # N15
w18 = Wall(0, 0, 0, 140, 465, 330, 10)  # N16
w19 = Wall(0, 0, 0, 140, 475, 10, 255)  # N17
w20 = Wall(0, 0, 0, 140, 730, 100, 10)  # N18
w21 = Wall(0, 0, 0, 240, 590, 10, 150)  # 19
w22 = Wall(0, 0, 0, 240, 580, 80, 10)  # 20
w23 = Wall(0, 0, 0, 310, 580, 10, 200)  # 21
w24 = Wall(0, 0, 0, 1200, 0, 10, 410)  # N1.2
w25 = Wall(0, 0, 0, 400, 115, 680, 10)  # N1.1
w26 = Wall(0, 0, 0, 1080, 115, 10, 180)  # N1.3
w27 = Wall(0, 0, 0, 890, 285, 200, 10)  # N1.4
w28 = Wall(0, 0, 0, 890, 405, 320, 10)  # N1.5
w29 = Wall(0, 0, 0, 890, 135, 10, 155)  # N1.6
w30 = Wall(0, 0, 0, 430, 128, 470, 10)  # N1.7
w31 = Wall(0, 0, 0, 430, 135, 10, 195)  # N1.8
w32 = Wall(0, 0, 0, 430, 330, 320, 10)  # N1.9
w33 = Wall(0, 0, 0, 750, 230, 10, 200)  # N1.20
w34 = Wall(0, 0, 0, 530, 230, 220, 10)  # N1.21
w35 = Wall(0, 0, 0, 640, 425, 120, 10)  # N1.22
w36 = Wall(0, 0, 0, 890, 405, 10, 150)  # N1.23
w37 = Wall(0, 0, 0, 460, 660, 5, 10)  # N15
w38 = Wall(0, 0, 0, 460, 665, 190, 10)  # N16
w39 = Wall(0, 0, 0, 640, 425, 10, 250)  # N 17
w40 = Wall(0, 0, 0, 750, 545, 150, 10)  # N1.24
w41 = Wall(0, 0, 0, 750, 550, 10, 10)  # N1.3
w42 = Wall(0, 0, 0, 750, 700, 10, 68)  # N1.31
w43 = Wall(0, 0, 0, 750, 560, 180, 10)  # 1.32
w44 = Wall(0, 0, 0, 750, 700, 180, 10)  # 1.33
w45 = Wall(0, 0, 0, 930, 700, 10, 60)
w46 = Wall(0, 0, 0, 930, 760, 400, 10)
w47 = Wall(0, 0, 0, 930, 440, 400, 10)
w48 = Wall(0, 0, 0, 930, 440, 10, 130)
packman = Hero("hero.png", 50, win_height - 80, 5)
monster_1 = Enemy("cyborg.png", 780, 300, 2)
monster_2 = Enemy_1("cyborg.png", 330, 550, 1.9)
final_sprite = GameSprite("pac-1.png", 1150, 600, 0)
finish = False
while run:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.fill((255, 255, 255))

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        w11.draw_wall()
        w12.draw_wall()
        w13.draw_wall()
        w14.draw_wall()
        w15.draw_wall()
        w16.draw_wall()
        w17.draw_wall()
        w18.draw_wall()
        w19.draw_wall()
        w20.draw_wall()
        w21.draw_wall()
        w22.draw_wall()
        w23.draw_wall()
        w24.draw_wall()
        w25.draw_wall()
        w26.draw_wall()
        w27.draw_wall()
        w28.draw_wall()
        w29.draw_wall()
        w30.draw_wall()
        w31.draw_wall()
        w32.draw_wall()
        w33.draw_wall()
        w34.draw_wall()
        w35.draw_wall()
        w36.draw_wall()
        w37.draw_wall()
        w38.draw_wall()
        w39.draw_wall()
        w40.draw_wall()
        w41.draw_wall()
        w42.draw_wall()
        w43.draw_wall()
        w44.draw_wall()
        w45.draw_wall()
        w46.draw_wall()
        w47.draw_wall()
        w48.draw_wall()

        packman.update()
        monster_1.update()
        monster_2.update()

        packman.reset()
        monster_1.reset()
        monster_2.reset()
        final_sprite.reset()

        if ((sprite.collide_rect(packman, monster_1)) or (sprite.collide_rect(packman, monster_2)) or (
        sprite.collide_rect(packman, w1)) or (sprite.collide_rect(packman, w2)) or (
        sprite.collide_rect(packman, w3)) or (sprite.collide_rect(packman, w4)) or (
        sprite.collide_rect(packman, w5)) or (sprite.collide_rect(packman, w6)) or (
        sprite.collide_rect(packman, w7)) or (sprite.collide_rect(packman, w8)) or (
        sprite.collide_rect(packman, w9)) or (sprite.collide_rect(packman, w10)) or (
        sprite.collide_rect(packman, w11)) or (sprite.collide_rect(packman, w12)) or (
        sprite.collide_rect(packman, w13)) or (sprite.collide_rect(packman, w14)) or (
        sprite.collide_rect(packman, w15)) or (sprite.collide_rect(packman, w16)) or (
        sprite.collide_rect(packman, w17)) or (sprite.collide_rect(packman, w18)) or (
        sprite.collide_rect(packman, w19)) or (sprite.collide_rect(packman, w20)) or (
        sprite.collide_rect(packman, w21)) or (sprite.collide_rect(packman, w22)) or (
        sprite.collide_rect(packman, w23)) or (sprite.collide_rect(packman, w24)) or (
        sprite.collide_rect(packman, w25)) or (sprite.collide_rect(packman, w26)) or (
        sprite.collide_rect(packman, w27)) or (sprite.collide_rect(packman, w28)) or (
        sprite.collide_rect(packman, w29)) or (sprite.collide_rect(packman, w30)) or (
        sprite.collide_rect(packman, w31)) or (sprite.collide_rect(packman, w32)) or (
        sprite.collide_rect(packman, w33)) or (sprite.collide_rect(packman, w34)) or (
        sprite.collide_rect(packman, w35)) or (sprite.collide_rect(packman, w36)) or (
        sprite.collide_rect(packman, w37)) or (sprite.collide_rect(packman, w38)) or (
        sprite.collide_rect(packman, w39)) or (sprite.collide_rect(packman, w40)) or (
        sprite.collide_rect(packman, w41)) or (sprite.collide_rect(packman, w42)) or (
        sprite.collide_rect(packman, w43)) or (sprite.collide_rect(packman, w44)) or (
        sprite.collide_rect(packman, w45)) or (sprite.collide_rect(packman, w46)) or (
        sprite.collide_rect(packman, w47)) or (sprite.collide_rect(packman, w48))):
            finish = True
            img_1 = image.load("game-over-3.jpg")
            window.fill((255, 255, 255))
            window.blit(transform.scale(img_1, (win_width, win_height)), (0, 0))

        if sprite.collide_rect(packman, final_sprite):
            finish = True
            img = image.load("end.jpg")
            window.fill((255, 255, 255))
            window.blit(transform.scale(img, (win_width, win_height)), (0, 0))

    display.update()
