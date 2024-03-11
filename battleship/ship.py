import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()
img = pygame.image.load('./battleship/images/battleship.bmp')
ship_rect = img.get_rect()
ship_rect.midbottom = screen.get_rect().midbottom
bullet_color = (255, 0 ,0)
frame_per_second = 144


def Create_bullet(self):
    bullet= pygame.Rect(0, 0, 5, 30)
    bullet.midtop = ship_rect.midtop
    return bullet

while True:
    # Process player inputs.
    moving_right = False
    moving_left = False
    moving_top = False
    moving_bottom = False
    bullets = []

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                moving_right = True
            elif event.key == pygame.K_a:
                moving_left = True
            elif event.key == pygame.K_w:
                moving_top = True
            elif event.key == pygame.K_s:
                moving_bottom = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                moving_right = False
            elif event.key == pygame.K_a:
                moving_left = False
            elif event.key == pygame.K_w:
                moving_top = False
            elif event.key == pygame.K_s:
                moving_bottom = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                b = Create_bullet()
                bullets.append(b)
        
    # Do logical updates here.
    # ...
    if moving_left and ship_rect.x >= 0:
        ship_rect.x -= 10
    elif moving_right and ship_rect.x <= screen.get_rect().right - ship_rect.width:
        ship_rect.x += 10
    elif moving_top and ship_rect.y >= 0:
        ship_rect.y -= 10
    elif moving_bottom and ship_rect.y <= screen.get_rect().bottom - ship_rect.height:
        ship_rect.y += 10

    for bullet in bullets:
        if screen.get_rect().top < bullet.top:
            bullet.top = -5

        
    screen.fill("grey")  # Fill the display with a solid color
    # Render the graphics here.
    # ...

    screen.blit(img, ship_rect)
    for bullet in bullets:
        pygame.draw.rect(screen, bullet_color, bullet)

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(frame_per_second)         # wait until next frame (at 60 FPS)