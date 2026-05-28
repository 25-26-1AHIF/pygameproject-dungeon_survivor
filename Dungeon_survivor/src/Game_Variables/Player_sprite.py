import pygame



class Sprite:

    def __init__(self, filepath: str, image_count: int, image_rect: pygame.Rect, animation_speed: int):
        self.filepath = filepath
        self.image_count = image_count
        self.image_rect = image_rect
        self.animation_speed = animation_speed


        self.images: list[pygame.Surface] = []

    def load_spritesheet(self):

        sprite_sheet = pygame.image.load(self.filepath).convert_alpha()

        for image_index in range(self.image_count):

            image_surface = pygame.Surface(self.image_rect.size, pygame.SRCALPHA)
            image_surface = image_surface.convert_alpha()


            image_surface.blit(
                sprite_sheet,
                (0, 0),
                pygame.Rect(
                    self.image_rect.x,
                    image_index * self.image_rect.height,
                    self.image_rect.width,
                    self.image_rect.height
                )
            )

            image_surface = pygame.transform.scale(image_surface, (100, 100))
            self.images.append(image_surface)

    def draw(self, screen: pygame.Surface, xpos: float, ypos: float, frame_counter: int):
        frame = (frame_counter // self.animation_speed) % self.image_count

        screen.blit(self.images[frame], (xpos, ypos))