import flet as ft

def main(page: ft.Page):
    page.title="Trabajo equipos"
    page.update()


    dropDown_Equipos = ft.Dropdown(width=300, hint_text="Equipos de fútbol", options=[ft.dropdown.Option("Barça FC")])
    dropDown_Equipos.options.append(ft.dropdown.Option("Atlético de Madrid"))
    dropDown_Equipos.options.append(ft.dropdown.Option("Real Madrid"))
    dropDown_Equipos.options.append(ft.dropdown.Option("PSG"))
    dropDown_Equipos.options.append(ft.dropdown.Option("Betis"))
    page.update()
    page.add(dropDown_Equipos)








    
ft.app(target=main)