import pygame
from pygame.locals import *
import random
import  time
from tkinter import *
from tkinter import messagebox


size = width, height = (800, 800)
road_w = int(width/1.6)
roadmark_w = int(width/80)
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4


pygame.init()
running = True
# Set Window Size
screen = pygame.display.set_mode(size)
# Set BG Color
screen.fill((60, 220, 0))
# Set Window Title
pygame.display.set_caption("Jay Car Game........ v01")






# update display
pygame.display.update()

# load Player Car Image
car = pygame.image.load("D:\Work\Python\All_Python_Projects_Jay\Personal_Codes\Car Game\Red Car_120x200.png")
car_loc = car.get_rect()
car_loc.center = right_lane, height*0.8

# load Enemy Player Car Image
car2 = pygame.image.load("D:\Work\Python\All_Python_Projects_Jay\Personal_Codes\Car Game\Brown Car_120x200.png")
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height*0.2



# Game Looping
while running:
    # Animate enemy vehicle
    car2_loc[1] += 4
    if car2_loc[1] > height:
        if random.randint(0,1) == 0:
            car2_loc.center = right_lane, -200
        else:
            car2_loc.center = left_lane, -200

    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] -190:


        print("GAME OVER..... YOU LOOSE !!!!!!")


        # game_over_window = Tk()
        # game_over_window.geometry("100x100")
        # messagebox.showinfo("GAME OVER", "YOU LOOSE !!!!!")
        # game_over_window.mainloop()


        time.sleep(4)
        break

    # Event Listeners
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w/2), 0])
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_w/2), 0])
    # Draw Graphics
    pygame.draw.rect(screen, (50, 50, 50), (width / 2 - road_w / 2, 0, road_w, height))
    pygame.draw.rect(screen, (255, 240, 60), (width / 2 - roadmark_w / 2, 0, roadmark_w, height))
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 - road_w / 2 + roadmark_w * 2, 0, roadmark_w, height))
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 + road_w / 2 - roadmark_w * 3, 0, roadmark_w, height))

    # Screen Bitmap Operation
    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)

    # update display
    pygame.display.update()

pygame.quit()
