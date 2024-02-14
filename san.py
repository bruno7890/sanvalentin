import flet as ft

list_rechazo = ['Segura ???',
                '...no lo esperaba',
                'oh nooo ...',
                'me duele tu rechazo',
                'por queee...',
                'deja de dar click',
                'NO DAR CLICK',
                'Iugg mi corazon']
rafa_lista =['rafa1,png',
             'rafa2,png',
             'rafa3,png',
             'rafa4,png',
             'rafa5,png',
             'rafa6,png',
             'rafa7,png',
             'rafa8,png',
             'rafa9,png']
rafa_feliz = 'rafa_feliz.png'

def main(page):
    def btn_click(e:ft.ControlEvent):

        if e.control.text != 'Si':
            e.control.text != list_rechazo.pop(0)
            rafa_img.src = rafa_lista.pop(0)
            if not len(list_rechazo):
                si_btn.disabled = True
                no_btn.disabled = True
                page.update()
            else:
                rafa_img.src = 'rafa_feliz.png'
                no_btn.disabled = True
            rafa_img.height = 300
            rafa_img.width=200
            page.update()
        choocho_img = ft.Image(src ='choochoo.png',
                               width=400,
                               height=400)
        rafa_img = ft.Image(src='choochoo.png')
        pregunta = ft.Text('¡¿Quieres salir conmigo?!',
                           size=20,
                           weight=ft.FontWeight.BOLD)
        si_btn = ft.ElevatedButton("Si", on_click = btn_click)
        no_btn = ft.ElevatedButton("No",on_click = btn_click)

        page.add(choocho_img,
                 pregunta,
                 ft.Row(spacing=0, controls=[si_btn,no_btn]),
                 rafa_img)
ft.app(target=main)