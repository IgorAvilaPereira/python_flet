import flet as ft

def main(page: ft.Page):
    t = ft.Text(value="Hello, world!", color="green")
    page.controls.append(t)
    page.update()


# desktop
ft.app(target=main)
# no terminal: python teste.py

# android
# ft.app(target=main)
# no terminal: flet run teste.py

# web
# ft.app(target=main, view="web_browser")
# no terminal: python teste.py








