import subprocess
import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("AI Car Driving")

# Set up fonts
font = pygame.font.Font(None, 36)

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

menu_image = pygame.image.load("Logo.png") 
menu_image = pygame.transform.scale(menu_image, (200, 200))  

# Define menu options
menu_options = [
    "Train AI Car",
    "Exit"
]

# Function to display the menu
def display_menu(selected_option):
    screen.fill(white)
    screen.blit(menu_image, ((width - 200) // 2, 50))
    for i, option in enumerate(menu_options):
        text = font.render(option, True, red if i == selected_option else black)
        text_rect = text.get_rect(center=(width // 2, height // 2 + i * 50))
        pygame.draw.rect(screen, black, text_rect, 2)
        screen.blit(text, text_rect)

# Main game loop
selected_option = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                selected_option = (selected_option + 1) % len(menu_options)
            elif event.key == pygame.K_UP:
                selected_option = (selected_option - 1) % len(menu_options)
            elif event.key == pygame.K_RETURN:
                if selected_option == 0:
                    subprocess.Popen(["python", "newCarTraining.py"]) 
                elif selected_option == 1:
                    pygame.quit()
                    sys.exit()

    display_menu(selected_option)
    pygame.display.flip()
