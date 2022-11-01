import pygame


class LampDisplay:
    BACKGROUND = (76, 45, 28)
    LAMP_ON = (242, 201, 159)
    LAMP_OFF = (173, 101, 62)
    BORDER_RATIO = 0.15

    def __init__(self, size: tuple[int, int], pixels_per_lamp: int) -> None:
        self.size = size
        self.pixels_per_lamp = pixels_per_lamp

        pygame.display.set_caption("Lamp Display")

        self.screen = pygame.display.set_mode(
            (
                size[0] * pixels_per_lamp,
                size[1] * pixels_per_lamp,
            )
        )

        self.clear()

    def clear(self) -> None:
        self.screen.fill(LampDisplay.BACKGROUND)

        for y in range(self.size[1]):
            for x in range(self.size[0]):
                self.set_pixel((x, y), False)

    def set_pixel(self, pixel: tuple[int, int], on: bool) -> None:
        border = self.pixels_per_lamp * 0.5 * LampDisplay.BORDER_RATIO

        pygame.draw.rect(
            self.screen,
            LampDisplay.LAMP_ON if on else LampDisplay.LAMP_OFF,
            pygame.Rect(
                round(pixel[0]) * self.pixels_per_lamp + border,
                round(pixel[1]) * self.pixels_per_lamp + border,
                self.pixels_per_lamp - 2 * border,
                self.pixels_per_lamp - 2 * border,
            ),
        )

    def update(self) -> bool:
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        return True
