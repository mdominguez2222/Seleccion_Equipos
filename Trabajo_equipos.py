import flet as ft

def main(page: ft.Page):
    page.title="Trabajo equipos"
    page.update()

    def cambiar_imagen(e):
        if dropDown_Equipos.value=="Barça FC":
            imagen.src="barsa.png"  
        elif dropDown_Equipos.value=="Atlético de Madrid":
            imagen.src="atleti.png"       
        elif dropDown_Equipos.value=="Real Madrid":
            imagen.src="real.png"  
        elif dropDown_Equipos.value=="PSG":
            imagen.src="psg.png"  
        elif dropDown_Equipos.value=="Betis":
            imagen.src="betis.png"  
        page.update()        
    
    
    imagen= ft.Image(src=f"ed", width=100, height=100,fit=ft.ImageFit.CONTAIN)
    page.add(imagen)
    
    dropDown_Equipos = ft.Dropdown(width=300, hint_text="Equipos de fútbol", options=[ft.dropdown.Option("Barça FC")], on_change=cambiar_imagen)
    dropDown_Equipos.options.append(ft.dropdown.Option("Atlético de Madrid"))
    dropDown_Equipos.options.append(ft.dropdown.Option("Real Madrid"))
    dropDown_Equipos.options.append(ft.dropdown.Option("PSG"))
    dropDown_Equipos.options.append(ft.dropdown.Option("Betis"))
    page.update()
    page.add(dropDown_Equipos)



ft.app(target=main, assets_dir="Imagenes")