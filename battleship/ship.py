import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()
img = pygame.image.load('./chapter_14/scoring/images/ship.bmp')
while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here.
    # ...
    

    screen.fill("grey")  # Fill the display with a solid color

    # Render the graphics here.
    # ...
    rect = img.get_rect()
    screen.blit(img, rect)

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)