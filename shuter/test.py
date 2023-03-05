from pygame import *
from random import *

font.init()
font = font.Font(None, 36)

speed = 10

win_width = 700
win_height = 500

score = 0

max_score = 10
lost = 0
max_lost = 5


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        if keys[K_1] and keys[K_2] and keys[K_3]:
            finish = False
        if keys[K_a] and self.rect.x > 5 and keys[K_LCTRL]:
            speed = 20
            self.rect.x -= self.speed
            speed = 10
        if keys[K_d] and self.rect.x < win_width - 80 and keys[K_LCTRL]:
            speed = 20
            self.rect.x += self.speed
            speed = 10
        if keys[K_w] and self.rect.y > 5 and keys[K_LCTRL]:
            speed = 20
            self.rect.y -= self.speed
            speed = 10
        if keys[K_s] and self.rect.y < win_height - 80 and keys[K_LCTRL]:
            speed = 20
            self.rect.y += self.speed
            speed = 10

    def fire(self):
        bullet = Bullet("pyla.png", self.rect.centerx - 0, self.rect.top, 15, 20, -15)
        bullets.add(bullet)


class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            global lost
            lost = lost + 1


class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()


bullets = sprite.Group()
monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy("monster.png", randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monster)

background = image.load("galaxy_2.jpg")
background = transform.scale(background, (700, 500))

display.set_caption("Шутер")
window = display.set_mode((win_width, win_height))
window.blit(background, (0, 0))

rocet = Player('rocet_5.png', 200, 200, 100, 100, speed)

finish = False

run = True
while run:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                rocet.fire()
    if not finish:
        window.fill((255, 255, 255))
        text = font.render("Score: " + str(score), 1, (0, 0, 0))
        window.blit(text, (10, 20))
        text_lose = font.render("Lost: " + str(lost), 1, (0, 0, 0))
        window.blit(text_lose, (10, 50))
        rocet.update()
        rocet.reset()

        monsters.update()
        monsters.draw(window)

        bullets.update()
        bullets.draw(window)

        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score = score + 1
            monster = Enemy("monster.png", randint(80, win_width - 80), -60, 80, 50, randint(1, 5))
            monsters.add(monster)
        if lost >= 5:
            finih = True

        if score >= max_score:
            finish = True

        if finish:
            run = False

    display.update()
