from random import randint
import pygame

pygame.mixer.init()

zahl = randint(0, 10)
zaehler = 0

print("Number guessing game")

while zaehler < 3:
    eingabe = int(input("Enter your number: "))
    if eingabe > 10:
        print("Number over 10, input was not counted")
    else:
        if eingabe < zahl:
            zaehler += 1
            print("The number you are looking for is greater")
        elif eingabe > zahl:
            zaehler += 1
            print("The number you are looking for is smaller")
        else:
            print(f"Die gesuchte Zahl war: {zahl}")
            pygame.mixer.music.load("Victory Sound Effect.mp3")
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            break

if zaehler == 3:
    print(f"Hahahaha, you lost, you noob! The number you were looking for was: {zahl} ")
    pygame.mixer.music.load("Sad Trombone - Sound Effect (HD).mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

