import flet as ft

def main(page: ft.Page):
    page.title="Trabajo equipos"
    vEquiposSeleccionados = []
    
    def cargarEquipos():
        vEquipos= []
        f = open("Equipos.txt", "r")

        for linea in f:
            vEquipos.append(linea)
            
        f.close()
        return vEquipos
    
    vEquipos = cargarEquipos()
    
    
    def guardarEquipos (e):
        equipo = dropDown_Equipos.value
        
        if vEquiposSeleccionados.count(equipo)== 0:
            foto= ft.Image(src= imagen.src, width=50, height=50)
            texto= ft.Text(equipo)
            fila= ft.Row(controls=[foto, texto])
            vEquiposSeleccionados.append(equipo)
            page.add(fila)
        else:
           dlg = ft.AlertDialog(title=ft.Text(f"{equipo} repetido, ERROR "),on_dismiss=lambda e: print("Dialog dismissed!"))
           page.dialog = dlg
           dlg.open = True
           page.update()
        
        print(vEquiposSeleccionados)

    def cambiar_imagen(e):
        if dropDown_Equipos.value=="Barça FC\n":
            imagen.src="barsa.png"  
        elif dropDown_Equipos.value=="Atlético de Madrid\n":
            imagen.src="atleti.png"       
        elif dropDown_Equipos.value=="Real Madrid":
            imagen.src="real.png"  
        elif dropDown_Equipos.value=="PSG\n":
            imagen.src="psg.png"  
        elif dropDown_Equipos.value=="Betis\n":
            imagen.src="betis.png"  
        page.update()    
        return(imagen.src)
        
        
    imagen= ft.Image(src=f"ed", width=100, height=100,fit=ft.ImageFit.CONTAIN)
    
    #boton

    boton=ft.FloatingActionButton(
        icon=ft.icons.ADD, on_click= guardarEquipos, 
        bgcolor=ft.colors.BLUE_300)


    
    dropDown_Equipos = ft.Dropdown(width=300, hint_text="Equipos de fútbol", on_change=cambiar_imagen)
    
    for equipo in vEquipos:
        dropDown_Equipos.options.append(ft.dropdown.Option(equipo))

      
    page.add(dropDown_Equipos, imagen, boton)
    


ft.app(target=main, assets_dir="Imagenes")