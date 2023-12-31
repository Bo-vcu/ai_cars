import math
import pickle
import pygame
from state import State
from settings import *

CAR_SIZE_X = 60    
CAR_SIZE_Y = 60

BORDER_COLOR = (255, 255, 255, 255) # Color To Crash on Hit

class Car:
    def __init__(self, game_state):
        self.game_state = game_state
        # Load Car Sprite and Rotate
        self.sprite = pygame.image.load('taxi_zonder_bg.png').convert() # Convert Speeds Up A Lot
        self.sprite = pygame.transform.scale(self.sprite, (CAR_SIZE_X, CAR_SIZE_Y))
        self.rotated_sprite = self.sprite 

        # self.position = [690, 740] # Starting Position
        # self.position = [830, 920] # Starting Position
        self.position = [600, 300] # Starting Position
        self.angle = 0
        self.speed = 0

        self.speed_set = False # Flag For Default Speed Later on

        self.center = [self.position[0] + CAR_SIZE_X / 2, self.position[1] + CAR_SIZE_Y / 2] # Calculate Center

        self.radars = [] # List For Sensors / Radars
        self.drawing_radars = [] # Radars To Be Drawn

        self.alive = True # Boolean To Check If Car is Crashed

        self.distance = 0 # Distance Driven
        self.time = 0 # Time Passed

        self.reached = False

    def draw(self, screen):
        screen.blit(self.rotated_sprite, self.position) # Draw Sprite
        self.draw_radar(screen) #OPTIONAL FOR SENSORS

    def draw_radar(self, screen):
        # Optionally Draw All Sensors / Radars
        for radar in self.radars:
            position = radar[0]
            pygame.draw.line(screen, (0, 255, 0), self.center, position, 1)
            pygame.draw.circle(screen, (0, 255, 0), position, 5)

    def check_collision(self, game_map):
        for point in self.corners:
            # If Any Corner Touches Border Color -> Crash
            # Assumes Rectangle
            x = int(point[0])
            y = int(point[1])
            
            if (
                0 <= x < game_map.get_width()
                and 0 <= y < game_map.get_height()
                and not game_map.get_at((x, y)) == BORDER_COLOR
            ):
                #self.alive = False
                break

    def check_radar(self, degree, game_map):
        length = 0
        x = int(self.center[0] + math.cos(math.radians(360 - (self.angle + degree))) * length)
        y = int(self.center[1] + math.sin(math.radians(360 - (self.angle + degree))) * length)

        # While We Don't Hit BORDER_COLOR AND length < 300 (just a max) -> go further and further
        while (
            0 <= x < game_map.get_width()
            and 0 <= y < game_map.get_height()
            and not game_map.get_at((x, y)) == BORDER_COLOR
            and length < 300
        ):
            length = length + 1
            x = int(self.center[0] + math.cos(math.radians(360 - (self.angle + degree))) * length)
            y = int(self.center[1] + math.sin(math.radians(360 - (self.angle + degree))) * length)

        # Calculate Distance To Border And Append To Radars List
        dist = int(math.sqrt(math.pow(x - self.center[0], 2) + math.pow(y - self.center[1], 2)))
        self.radars.append([(x, y), dist])
    
    def update(self, game_map):
        # Set The Speed To 20 For The First Time
        # Only When Having 4 Output Nodes With Speed Up and Down
        if not self.speed_set:
            self.speed = 10
            self.speed_set = True

        if self.time > 350:

            self.alive=False

        x = math.pow(self.center[0]-self.game_state.endPos[0],2)
        y = math.pow(self.center[1]-self.game_state.endPos[1],2)
        if(math.sqrt(x + y) <= 50):
            self.speed = 0
            self.speed_set = True
            self.reached = True
        # Get Rotated Sprite And Move Into The Right X-Direction
        # Don't Let The Car Go Closer Than 20px To The Edge
        self.rotated_sprite = self.rotate_center(self.sprite, self.angle)
        self.position[0] += math.cos(math.radians(360 - self.angle)) * self.speed
        self.position[0] = max(self.position[0], 20)
        self.position[0] = min(self.position[0], WIDTH - 120)

        # Increase Distance and Time
        self.distance += self.speed
        self.time += 1
        
        # Same For Y-Position
        self.position[1] += math.sin(math.radians(360 - self.angle)) * self.speed
        self.position[1] = max(self.position[1], 20)
        self.position[1] = min(self.position[1], WIDTH - 120)

        # Calculate New Center
        self.center = [int(self.position[0]) + CAR_SIZE_X / 2, int(self.position[1]) + CAR_SIZE_Y / 2]

        # Calculate Four Corners
        # Length Is Half The Side
        length = 0.5 * CAR_SIZE_X
        left_top = [self.center[0] + math.cos(math.radians(360 - (self.angle + 30))) * length, self.center[1] + math.sin(math.radians(360 - (self.angle + 30))) * length]
        right_top = [self.center[0] + math.cos(math.radians(360 - (self.angle + 150))) * length, self.center[1] + math.sin(math.radians(360 - (self.angle + 150))) * length]
        left_bottom = [self.center[0] + math.cos(math.radians(360 - (self.angle + 210))) * length, self.center[1] + math.sin(math.radians(360 - (self.angle + 210))) * length]
        right_bottom = [self.center[0] + math.cos(math.radians(360 - (self.angle + 330))) * length, self.center[1] + math.sin(math.radians(360 - (self.angle + 330))) * length]
        self.corners = [left_top, right_top, left_bottom, right_bottom]

        # Check Collisions And Clear Radars
        self.check_collision(game_map)
        self.radars.clear()

        # From -90 To 120 With Step-Size 45 Check Radar
        for d in range(-90, 120, 45):
            self.check_radar(d, game_map)

    def get_data(self):
        x = self.center[0]-self.game_state.endPos[0]
        y = self.center[1]-self.game_state.endPos[1]

        angle_to_endpoint = math.atan2(y,x) * (180/math.pi) -180

        # Get Distances To Border
        radars = self.radars
        return_values = [0, 0, 0, 0, 0, self.center[0], self.center[1], self.angle, angle_to_endpoint]
        # print(return_values)


        for i, radar in enumerate(radars):
            return_values[i] = int(radar[1] / 30)

        return return_values

    def is_alive(self):
        # Basic Alive Function
        return self.alive


    def rotate_center(self, image, angle):
        # Rotate The Rectangle
        rectangle = image.get_rect()
        rotated_image = pygame.transform.rotate(image, angle)
        rotated_rectangle = rectangle.copy()
        rotated_rectangle.center = rotated_image.get_rect().center
        rotated_image = rotated_image.subsurface(rotated_rectangle).copy()
        return rotated_image

class Test2(State):
    def __init__(self, game_state):
        # Load the best genome and network
        with open("neat_best_genome.pkl", 'rb') as input_file:
            self.best_genome = pickle.load(input_file)

        with open("neat_best_network.pkl", 'rb') as input_file:
            self.best_network = pickle.load(input_file)

        self.endPointImage = pygame.image.load('endpoint.png').convert()
        self.game_map = pygame.image.load('newCity.png').convert()

        self.car = Car(self)  # Create a single car instance
        self.generation_font = pygame.font.SysFont("Arial", 30) 
        self.game_state = game_state

        self.current_generation = 0 # Generation counter
        self.indexEndPos = 0
        self.training_endPos = [ [1200 , 200], [1200 , 500], [200 , 250], [400, 600], [1350 , 150]]

        self.endPos = self.training_endPos[0]

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state.__setstate_menu__()

    def update(self):
        output = self.best_network.activate(self.car.get_data())  # Get the network's output
        choice = output.index(max(output))

        # Update the car based on the network's output (same logic as in the learning part)
        if choice == 0:
            self.car.angle += 10  # Left
        elif choice == 1:
            self.car.angle -= 10  # Right
        elif choice == 2:
            pass

        self.car.update(self.game_map)

        if self.car.reached or not(self.car.is_alive()):
            self.car = Car(self)
            if self.indexEndPos >= len(self.training_endPos):
                self.indexEndPos = 0

            self.endPos = self.training_endPos[self.indexEndPos]
            self.indexEndPos += 1

    def render_frame(self):
        self.game_state.screen.fill((0,0,0)) 
        self.game_state.screen.blit(self.game_map, (0, 0))
        self.game_state.screen.blit(self.endPointImage, self.endPos)
        self.car.draw(self.game_state.screen)

        text = self.generation_font.render("Press (R) to choose another point on the map", True, (255, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (900, 900)
        self.game_state.screen.blit(text, text_rect)
