# Faça um programa em Python que abra e reproduza um áudio de um arquivos MP3

from pygame

pygame.init()
pygame.mixer.music.load("ppp.mp3")
pygame.mixer.music.play()
pygame.eventi.wait()