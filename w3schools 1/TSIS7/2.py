import pygame
from pygame import mixer
import time

pygame.init()
mixer.init()

a = int(0)
scr = pygame.display.set_mode((640, 640))
pygame.display.set_caption('My music')

playlist = []
playlist.append('songs\Bloo_-_Downtown_Baby_(musmore.com).mp3')
playlist.append('songs\Tom Odell - Another Love.mp3')
playlist.append('songs\The Weeknd - Call Out My Name.mp3')

playlist_image = []
playlist_image.append(pygame.image.load('image/bloo_downtownbaby.jpeg').convert())
playlist_image.append(pygame.image.load('image/anotherlove.jpeg').convert())
playlist_image.append(pygame.image.load('image/theweekend.jpeg').convert())


scl = pygame.transform.scale(playlist_image[a], (640, 640))
scr.blit(scl, (0, 0) )
pygame.display.update()


mixer.music.set_volume(0.2)
mixer.music.queue

mixer.music.load(playlist[a]) 
mixer.music.play()

print(len(playlist))


run = False

while not run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_p]:
        mixer.music.pause()
    elif keys[pygame.K_r]:
        mixer.music.unpause()
    elif keys[pygame.K_RIGHT]:
        if a < len(playlist)-1 and a >= 0:
           a+=1
           mixer.music.load(playlist[a])
           scl = pygame.transform.scale(playlist_image[a], (640, 640))
           scr.blit(scl, (0, 0) )
           pygame.display.update()
           mixer.music.play()
           time.sleep(0.25)
        else: 
            a = 0
            mixer.music.load(playlist[a])
            scl = pygame.transform.scale(playlist_image[a], (640, 640))
            scr.blit(scl, (0, 0) )
            pygame.display.update()
            mixer.music.play()
            time.sleep(0.25)

        

    elif keys[pygame.K_LEFT]:
        if a < len(playlist) and a >= 1:
           a-=1
           mixer.music.load(playlist[a]) 
           scl = pygame.transform.scale(playlist_image[a], (640, 640))
           scr.blit(scl, (0, 0) )
           pygame.display.update()
           mixer.music.play()
           time.sleep(0.25)
        else: 
            a = len(playlist)-1
            mixer.music.load(playlist[a])
            scl = pygame.transform.scale(playlist_image[a], (640, 640))
            scr.blit(scl, (0, 0) )
            pygame.display.update()
            mixer.music.play()
            time.sleep(0.25)

        
 
    

pygame.quit()
    





        

        
            
