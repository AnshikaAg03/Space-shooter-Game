# test_pygame.py
import asyncio
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Test")
clock = pygame.time.Clock()

async def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        text = font.render("Pygame Works!", True, (255, 255, 255))
        screen.blit(text, (300, 280))
        pygame.display.flip()
        
        await asyncio.sleep(0)
        clock.tick(60)

asyncio.run(main())
