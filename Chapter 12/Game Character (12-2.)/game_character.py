import pygame
import sys

# The exercise states to import a bpm of a game charcter, I decided for another image though.

class Project:
    """General class to manage project."""

    def __init__(self):
        """Initialize the game, and create game recourses."""
        pygame.init()
        
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Display of an image")
        self.screen.fill((12, 73, 92))

        self.image = Image(self)

    def run_project(self):
        """Starting the main loop."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.image.bliteme()

            # Making the most recently drawn visible on the screen.
            pygame.display.flip()


# Importing the Earth Image
class Image:
    """Class for the image."""
    def __init__(self, project):
        self.screen = project.screen
        self.screen_rect = project.screen.get_rect()

        # Load the image
        self.image = pygame.image.load('images/earth.bmp')
        self.image = pygame.transform.scale(self.image, (400, 400))
        self.image_rect = self.image.get_rect()

        # Start each new image in the center of the screen.
        self.image_rect.center = self.screen_rect.center
    
    # Drawing the image (hopefully)
    def bliteme(self):
        self.screen.blit(self.image, self.image_rect)


# Creating an instance and run the project
project = Project()
project.run_project()