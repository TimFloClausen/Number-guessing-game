from random import randint
import pygame

pygame.mixer.init()

zahl = randint(0, 10)
zaehler = 0

print("Zahlen-Ratespiel")

while zaehler < 3:
    eingabe = int(input("Gebe deine Zahl ein: "))
    if eingabe > 10:
        print("Zahl über 10, Eingabe wurde nicht gewertet")
    else:
        if eingabe < zahl:
            zaehler += 1
            print("Die gesuchte Zahl ist grösser")
        elif eingabe > zahl:
            zaehler += 1
            print("Die gesuchte Zahl ist kleiner")
        else:
            print(f"Die gesuchte Zahl war: {zahl}")
            pygame.mixer.music.load("Zahlen-Ratespiel 1.0/Victory Sound Effect.mp3")
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            break

if zaehler == 3:
    print(f"Hahahaha, Du hast verloren du Noob! Die gesuchte Zahl war: {zahl} ")
    pygame.mixer.music.load("Zahlen-Ratespiel 1.0/Sad Trombone - Sound Effect (HD).mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

