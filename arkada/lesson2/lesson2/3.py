# Подключить нужные модули
import pygame 
pygame.init() 

# Глобальные переменные (настройки)
win_width = 800 
win_height = 600
img_file_back='cave.png'
FPS = 60 # будем повторять цикл 60 раз в секунду


pygame.display.set_caption("ARCADA") 
window = pygame.display.set_mode((win_width, win_height)) 

back = pygame.transform.scale(pygame.image.load(img_file_back).convert(), (win_width, win_height)) 

# Основной цикл игры:
run = True # флаг продолжения программы
while run:
    # Обработка событий
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False 

    # Отрисовка 
    window.blit(back, (0, 0)) 
    pygame.display.update() 

    # Пауза
    pygame.time.delay(20)
