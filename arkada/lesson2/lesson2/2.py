# Подключить нужные модули
import pygame

pygame.init()

# Глобальные переменные (настройки)
win_width = 800
win_height = 600
img_file_back = 'cave.png'

# Запуск 
pygame.display.set_caption("ARCADA")
window = pygame.display.set_mode((win_width, win_height))

back = pygame.transform.scale(pygame.image.load(img_file_back).convert(), (win_width, win_height))

# Основной цикл игры:
run = True  # флаг продолжения программы
while run:
    # Получение событий
    events = pygame.event.get()  # Получили очередь событий (она очистилась!), загрузили полученный список в переменную events
    for event in events:  # проходим по списку
        if event.type == pygame.QUIT:  # тип события QUIT, т.е. человек нажал на крестик закрытия программы
            run = False  # сбрасываем флаг продолжения, цикл больше не повторится, программа закроется

    # Отрисовка 
    window.blit(back, (0, 0))  # в цикле каждый раз будем обновлять картинку
    pygame.display.update()
