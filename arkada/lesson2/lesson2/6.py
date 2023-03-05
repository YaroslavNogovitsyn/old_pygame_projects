""" Добавим персонажа, который управляется стрелками. 
Фон будет смещаться, если персонаж пытается выйти за пределы экрана """
# Подключить нужные модули
import pygame

pygame.init()

# Глобальные переменные (настройки)
win_width = 800
win_height = 600
left_bound = win_width / 40  # границы, за которые персонаж не выходит (начинает ехать фон)
right_bound = win_width - left_bound

img_file_back = 'cave.png'
img_file_hero = 'm1.png'  # картинка для персонажа
shift = 0
speed = 0


# Классы
class Hero(pygame.sprite.Sprite):
    """ класс для героя игры - наследник класса Sprite. """

    def __init__(self, filename, x_speed=0, y_speed=0, x=left_bound, y=0, width=120, height=120):
        """ конструктор класса. Берёт картинку персонажа из файла, устанавливает в нужной точке. """
        pygame.sprite.Sprite.__init__(self)  # вызываем конструктор базового класса Sprite

        # каждый спрайт должен хранить свойство image - картинка (surface). 
        # картинка загружается из файла и умещается в прямоугольник нужных размеров:
        self.image = pygame.transform.scale(pygame.image.load(filename), (width, height)).convert_alpha()
        # используем convert_alpha, нам надо сохранять прозрачность

        # каждый спрайт должен хранить свойство rect - прямоугольник. 
        self.rect = self.image.get_rect()
        # ставим персонажа в переданную точку (x, y):
        self.rect.x = x
        self.rect.y = y
        # создаем дополнительные свойства, запоминаем переданные значения:
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        """ перемещает персонажа, применяя текущую горизонтальную и вертикальную скорость"""
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed


# Запуск игры
pygame.display.set_caption("ARCADA")
window = pygame.display.set_mode([win_width, win_height])

back = pygame.transform.scale(pygame.image.load(img_file_back).convert(), (win_width, win_height))

# список всех персонажей игры:
all_sprites = pygame.sprite.Group()
# создаем персонажа, добавляем его в список всех спрайтов:
robin = Hero(img_file_hero)
all_sprites.add(robin)

run = True

while run:
    # Ввод данных (обработка событий)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                robin.x_speed = -5  # персонаж должен пойти налево
            elif event.key == pygame.K_RIGHT:
                robin.x_speed = 5  # персонаж должен пойти направо
            elif event.key == pygame.K_UP:
                robin.y_speed = -5  # персонаж должен пойти вверх (ось Y направлена вниз!)
            elif event.key == pygame.K_DOWN:
                robin.y_speed = 5  # персонаж должен пойти вниз

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                robin.x_speed = 0
            elif event.key == pygame.K_RIGHT:
                robin.x_speed = 0
            elif event.key == pygame.K_UP:
                robin.y_speed = 0
            elif event.key == pygame.K_DOWN:
                robin.y_speed = 0

    # Вычисления:
    # перемещение игровых объектов, 
    all_sprites.update()

    # обработка столкновений, изменение состояния игры 
    if robin.rect.top < 0 or robin.rect.bottom > win_height:
        robin.rect.y -= robin.y_speed  # запрещаем персонажу выходить вниз и вверх

    if (
            robin.rect.right > right_bound and robin.x_speed > 0
            or
            robin.rect.left < left_bound and robin.x_speed < 0
    ):  # при выходе влево или вправо переносим изменение в сдвиг экрана
        shift -= robin.x_speed
        robin.rect.x -= robin.x_speed

    # Вывод данных (отрисовка)
    # рисуем фон со сдвигом
    local_shift = shift % win_width
    window.blit(back, (local_shift, 0))
    if local_shift != 0:
        window.blit(back, (local_shift - win_width, 0))

        # сверху фона размещаем все спрайты на своих местах:
    all_sprites.draw(window)

    pygame.display.update()

    # Пауза
    pygame.time.delay(20)
