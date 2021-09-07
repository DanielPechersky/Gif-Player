from dataclasses import dataclass
from typing import TypeAlias

SIDE_LENGTH = 16
PANEL_SIZE = SIDE_LENGTH ** 2

LineCoordinate: TypeAlias = int

ImageCoordinate: TypeAlias = int
ImageCoordinates: TypeAlias = tuple[ImageCoordinate, ImageCoordinate]

@dataclass(frozen=True)
class Up: pass
@dataclass(frozen=True)
class Down: pass
@dataclass(frozen=True)
class Left: pass
@dataclass(frozen=True)
class Right: pass

VerticalSide: TypeAlias = Up | Down
HorizontalSide: TypeAlias = Left | Right
Side = VerticalSide | HorizontalSide

flipped = {
    Left(): Right(),
    Right(): Left(),
    Up(): Down(),
    Down(): Up(),
}

clockwise = {
    Left(): Up(),
    Up(): Right(),
    Right(): Down(),
    Down(): Left(),
}

Orientation: TypeAlias = tuple[VerticalSide, HorizontalSide] | tuple[HorizontalSide, VerticalSide]

@dataclass
class Panel:
    offset: tuple[int, int]
    orientation: Orientation

    # assume entrance is on top left and image coordinates are from top left of image
    @staticmethod
    def coordinate_within_panel_unadjusted(x: LineCoordinate) -> ImageCoordinates:
        row, col = x // SIDE_LENGTH, x % SIDE_LENGTH
        if row % 2 == 1:
            col = SIDE_LENGTH - 1 - col
        return row, col

    def coordinate_within_panel(self, x: LineCoordinate) -> ImageCoordinates:
        def flipVertically(c: ImageCoordinates) -> ImageCoordinates:
            row, col = c
            return (SIDE_LENGTH - 1 - row, col)

        def rotateClockwise(c: ImageCoordinates) -> ImageCoordinates:
            row, col = c
            return (col, SIDE_LENGTH - 1 - row)

        coord = Panel.coordinate_within_panel_unadjusted(x)
        side, direction = self.orientation
        if clockwise[side] != direction:
            coord = flipVertically(coord)
            side = flipped[side]
        
        rotations = {
            Up(): 3,
            Right(): 2,
            Down(): 1,
            Left(): 0,
        }
        for _ in range(rotations[side]):
            coord = rotateClockwise(coord)
        
        return ImageCoordinates(c + o * SIDE_LENGTH for c, o in zip(coord, self.offset, strict=True))

def coordinate(panels: list[Panel], x: LineCoordinate) -> ImageCoordinates:
    panel, position = x // PANEL_SIZE, x % PANEL_SIZE
    panel = panels[panel]
    return panel.coordinate_within_panel(position)
