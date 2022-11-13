import flet
from flet import *
from flet import icons, colors

def main(page: Page):
    page.window_width = 300
    page.window_height = 300
    page.add(
        TextField(label="Isming nima: ")
    )

flet.app(target=main)