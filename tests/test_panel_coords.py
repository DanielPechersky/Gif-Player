from gifplayer.panel_coords import PANEL_SIZE, SIDE_LENGTH, coordinate, Panel, Up, Down, Left, Right

def test_coords_basic():
    panels = [Panel((0, 0), (Left(), Up())), Panel((1, 0), (Up(), Left())), Panel((1, 1), (Down(), Right()))]

    assert coordinate(panels, 0) == (0, 0)
    assert coordinate(panels, PANEL_SIZE - 1) == (SIDE_LENGTH - 1, 0)
    assert coordinate(panels, SIDE_LENGTH - 1 + 3) == (1, SIDE_LENGTH - 3)

    assert coordinate(panels, PANEL_SIZE * 2 - 5) == (SIDE_LENGTH - 1 + 5, SIDE_LENGTH - 1)
    assert coordinate(panels, PANEL_SIZE * 2) == (SIDE_LENGTH * 2 - 1, SIDE_LENGTH * 2 - 1)
    assert coordinate(panels, PANEL_SIZE * 2 + 18) == (SIDE_LENGTH - 1 + 3, SIDE_LENGTH * 2 - 1 - 1)
