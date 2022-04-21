import rotatescreen
import time
screen = rotatescreen.get_primary_display()
for prank in range(1, 100):
    time.sleep(1)
    screen.rotate_to(prank*90%360)