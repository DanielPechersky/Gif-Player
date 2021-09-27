from .display import display_gif, strip
from .load import load_gif


# gif = "https://c.tenor.com/1a6RFI10-oYAAAAd/butter-dog.gif"
gif = "https://media0.giphy.com/media/3pj7env3PlRjfIOjzh/giphy.gif?cid=790b76117336ba3a192af88839f82105c4b1ec855cfbb482&rid=giphy.gif&ct=g"

gif = list(load_gif(gif))

try:
    while True:
        display_gif(gif)
finally:
    strip.deinit()
