#Programa que abre e reproduz um áudio de um arquivo mp3.
#“Infelizmente em uma das atualizações do Python a biblioteca do Pygame parou de funcionar em relação a funcionalidade do mp3. O Professor Guanabara informa que tudo bem pular este exercício já que houve esta mudança, e mais pra frente caso necessário e haja interesse pesquisar a nova forma de incluir mp3.” (mensagem do curso)
#Mas, futuramente encontraremos uma solução!
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
