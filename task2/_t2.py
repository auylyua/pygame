import pygame
import os
import sys

pygame.init()
pygame.mixer.init()

w, h = 500, 500
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Simple Music Player")

music_folder = 'music'
album = [os.path.join(music_folder, f) for f in os.listdir(music_folder) if f.endswith('.mp3')]

if len(album) < 10:
    print("You need at least 10 songs!")
    sys.exit()

cover_folder = 'cover'
cover_files = sorted([f for f in os.listdir(cover_folder) if f.endswith(('.png', '.jpg', '.jpeg'))])

if len(cover_files) < len(album):
    print("Not enough cover images!")
    sys.exit()

covers = [pygame.image.load(os.path.join(cover_folder, f)) for f in cover_files]

names = [
    "Alright", "BOOGIE", "C U Girl", "Collard Greens", "euphoria",
    "Infrunami", "Not Like Us", "One More Love Song", "Swimming Pools(Drank)", "Uuuu"
]

def start_music(index):
    pygame.mixer.music.load(album[index])
    pygame.mixer.music.play()
    print(f"Playing: {names[index]}")

track = 0
is_paused = False

start_music(track)

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill((0, 0, 0))

    cover = pygame.transform.scale(covers[track], (300, 300))
    screen.blit(cover, (w // 2 - 150, h // 2 - 180))

    song_text = font.render(names[track], True, (255, 255, 255))
    screen.blit(song_text, (w // 2 - song_text.get_width() // 2, h // 2 + 140))

    pygame.draw.polygon(screen, (255, 255, 255), [
        (w // 2 - 90, h // 2 + 180), (w // 2 - 110, h // 2 + 200), (w // 2 - 90, h // 2 + 220)
    ])

    pygame.draw.rect(screen, (255, 255, 255), (w // 2 - 15, h // 2 + 183, 30, 30))

    pygame.draw.polygon(screen, (255, 255, 255), [
        (w // 2 + 90, h // 2 + 180), (w // 2 + 110, h // 2 + 200), (w // 2 + 90, h // 2 + 220)
    ])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == SONG_END:
            track = (track + 1) % len(album)
            start_music(track)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if is_paused:
                    pygame.mixer.music.unpause()
                    is_paused = False
                else:
                    pygame.mixer.music.pause()
                    is_paused = True

            elif event.key == pygame.K_RIGHT:
                track = (track + 1) % len(album)
                start_music(track)

            elif event.key == pygame.K_LEFT:
                track = (track - 1) % len(album)
                start_music(track)

            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
                is_paused = False

    pygame.display.flip()

pygame.quit()
sys.exit()
