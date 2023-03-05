''' Добавим управление стрелками. При нажатии влево фон будет смещаться вправо, и наоборот '''
# Подключить нужные модули
import pygame

pygame.init()

# Глобальные переменные (настройки)
win_width = 800
win_height = 600
img_file_back = 'cave.png'
shift = 0  # сдвиг фона
speed = 0  # текущая скорость перемещения

# Классы


pygame.display.set_caption("ARCADA")
window = pygame.display.set_mode((win_width, win_height))

back = pygame.transform.scale(pygame.image.load(img_file_back).convert(), (win_width, win_height))

# Основной цикл игры:
run = True
while run:
    # Ввод данных (обработка событий)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:  # есть события типа "клавиша нажата"
            if event.key == pygame.K_LEFT:  # стрелка "влево"
                speed = 5  # начали ехать
            elif event.key == pygame.K_RIGHT:  # стрелка "вправо"
                speed = -5  # начали ехать
        elif event.type == pygame.KEYUP:  # есть события типа "клавиша отпущена"
            if event.key == pygame.K_LEFT:
                speed = 0  # закончили ехать
            elif event.key == pygame.K_RIGHT:
                speed = 0  # закончили ехать

    # Вычисления:
    # перемещение игровых объектов, 
    shift += speed
    local_shift = shift % win_width  # общий сдвиг может быть несколько экранов.
    # Берем остаток от деления на ширину экрана, чтобы получить сдвиг в пределах экрана
    # и понять, насколько надо двигать картинку.

    # обработка столкновений 
    # изменение состояния игры
    window.blit(back, (local_shift, 0))  # рисуем фон справа от сдвига
    if local_shift != 0:
        window.blit(back, (local_shift - win_width, 0))  # рисуем такой же фон слева от сдвига

    # Вывод данных (отрисовка)
    pygame.display.update()

    pygame.time.delay(20)
