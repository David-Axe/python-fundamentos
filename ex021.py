#Programa que abre e reproduz um áudio de um arquivo mp3.
#Programa com erro. No próprio curso diz que foi atualizado o python então ocorreria um erro. Corrigir futuramente.
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
