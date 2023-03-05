from pygame import *

window = display.set_mode((700, 500))

display.set_caption("Первый проект")
window.fill((255, 255, 255))
heigh = 60
wigth = 40
x = 5
y = 500 - heigh - 5
window.fill((0, 0, 0))
draw.rect(window, (0, 0, 255), (x, y, wigth, heigh))
display.update()

time.delay(5000)
