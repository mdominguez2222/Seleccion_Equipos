import flet as ft

vEquiposSeleccionados = []

def main(page: ft.Page):
    page.title="Trabajo equipos"
    vEquipos = ["Real Madrid", "Barça FC", "PSG","Atlético de Madrid", "Betis"]


    def guardarEquipos (e):
        equipo = dropDown_Equipos.value
        if vEquiposSeleccionados.count(equipo)== 0:
            vEquiposSeleccionados.append(equipo)
        else:
           dlg = ft.AlertDialog(title=ft.Text(f"{equipo} repetido, ERROR "),on_dismiss=lambda e: print("Dialog dismissed!"))
           page.dialog = dlg
           dlg.open = True
           page.update()
        
        print(vEquiposSeleccionados)

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
    
    #boton

    boton=ft.FloatingActionButton(
        icon=ft.icons.ADD, on_click= guardarEquipos, 
        bgcolor=ft.colors.LIME_300)


    
    dropDown_Equipos = ft.Dropdown(width=300, hint_text="Equipos de fútbol", on_change=cambiar_imagen)
    
    for equipo in vEquipos:
        dropDown_Equipos.options.append(ft.dropdown.Option(equipo))


    
    page.add(dropDown_Equipos, imagen, boton)

    


ft.app(target=main, assets_dir="Imagenes")