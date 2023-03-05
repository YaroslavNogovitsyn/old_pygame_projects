from pygame import *

window = display.set_mode((700, 500))
display.set_caption("Первый проект")
background = transform.scale(image.load("background.png"), (700, 500))
# данные о первом спрайте - квадрате
height = 60
width = 40
x = 5
y = 500 - height - 5
speed = 5
# данные о спрайте-картинке
x2 = 100
y2 = 395
# изображение героя
img1 = transform.scale(image.load('1-2.png'), (100, 100))
# игровой цикл
run = True
while run:
    # цикл срабатывает каждую 0.05 секунд
    time.delay(50)
    # на каждой итерации красим экран в исходный цвет и рисуем заново объект в новом месте
    # window.fill((0,0,0)) #черный фон
    window.blit(background, (0, 0))
    # перебираем все события, которые могли произойти
    for e in event.get():
        # событие нажатия на крестик окошка
        if e.type == QUIT:
            run = False
        # ----------------------------------------------------------------------------
        # Управление и обновление изображения спрайта-квадрата
        # Простой способ управления, не работает, если зажать клавишу
        if e.type == KEYDOWN:  # Проверяем, что это событие нажатия на клавишу
            if e.key == K_LEFT:  # Проверяем, а что за кнопка нажата
                x -= speed
            elif e.key == K_RIGHT:
                x += speed
            elif e.key == K_UP:
                y -= speed
            elif e.key == K_DOWN:
                y += speed
    draw.rect(window, (0, 0, 255), (x, y, width, height))

    # ----------------------------------------------------------------------------
    # Управление и обновление изображения спрайта-картинки
    # Более сложное решение, если клавишу отжать - прекращаем движение, герой не выходит за границы экрана.
    window.blit(img1, (x2, y2))
    keys = key.get_pressed()
    if keys[K_LEFT] and x2 > 5:
        x2 -= speed
    if keys[K_RIGHT] and x2 < 595:
        x2 += speed
    if keys[K_UP] and y2 > 5:
        y2 -= speed
    if keys[K_DOWN] and y2 < 395:
        y2 += speed
    display.update()
