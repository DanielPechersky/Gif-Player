from typing import Iterable
import imageio

from .display import Frame

def load_gif(gif) -> Iterable[Frame]:
    gif: list[imageio.core.util.Array] = imageio.mimread(gif)
    for frame in gif:
        yield Frame(frame, frame.meta['duration'] / 100)
