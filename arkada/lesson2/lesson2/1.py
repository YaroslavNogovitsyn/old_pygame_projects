# Подключить нужные модули
import pygame 
pygame.init() 

# Глобальные переменные (настройки)
win_width = 800 
win_height = 600
img_file_back='cave.png'

# Запуск 
pygame.display.set_caption("ARCADA") # устанавливать иожно в любой момент, даже до создания окна)
window = pygame.display.set_mode((win_width, win_height)) # если надо передать два числа одним параметром, 
                                                          # то часто это можно делать как списком: [x, y]
                                                          # так и кортежем: (x, y) 

back = pygame.transform.scale(pygame.image.load(img_file_back).convert(), (win_width, win_height)) # загрузим и преобразуем без лишних переменных

window.blit(back, (0, 0)) 
pygame.display.update() 

# Бесконечный цикл:
while 1:
    pass

