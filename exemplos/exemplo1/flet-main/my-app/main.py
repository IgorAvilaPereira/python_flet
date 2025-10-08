import flet as ft

#  https://flet.dev/docs/guides/python/testing-on-android/

# python3 -m venv .venv
# source .venv/bin/activate
# pip install flet --upgrade
# flet --version
# n precisa na segunda vez
# flet create my-app 
# cd my-app
# flet run --android

def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("Hello, Flet!")))

# android
# flet run --android
# desktop
# python main.py 
ft.app(main)
