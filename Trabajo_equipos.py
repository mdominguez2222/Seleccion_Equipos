import flet as ft

def main(page: ft.Page):
    page.title="Trabajo equipos"
    page.update()


    atleti = ft.Image(src=f"/Imagenes/atleti-removebg-preview.png", width=100, height=100,fit=ft.ImageFit.CONTAIN)
    barsa = ft.Image(src=f"/Imagenes/barsa-removebg-preview(1).png", width=100, height=100,fit=ft.ImageFit.CONTAIN)
    betis = ft.Image(src=f"/Imagenes/betis-removebg-preview.png", width=100, height=100,fit=ft.ImageFit.CONTAIN)
    psg = ft.Image(src=f"/Imagenes/psg-removebg-preview.png", width=100, height=100,fit=ft.ImageFit.CONTAIN)
    real_madrid = ft.Image(src=f"/Imagenes/real_madrid-removebg-preview.png", width=100, height=100,fit=ft.ImageFit.CONTAIN)
    page.add(atleti,barsa, betis, psg, real_madrid)









    
ft.app(target=main, assets_dir="Imagenes")