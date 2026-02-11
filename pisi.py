import flet as ft 
from flet import *
import sqlite3
from sqlite3 import *
import datetime
from datetime import *

def main(page: ft.Page):
    
    page.title = 'Antismoke'
    
    page.theme_mode = "#000000"

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    page.window.width = 768
    page.window.height = 1024


    def chan(e):

        if all([user_log.value, user_pas.value]):
            butt.disabled = False
            butt_aut.disabled = False
        else:
            butt.disabled = True
            butt_aut.disabled = True


        page.update()


    def regis(e):

        db = sqlite3.connect('Antismoker')

        cur = db.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY,
                    login TEXT,
                    password TEXT
                    )""")
   
        cur.execute(f"""INSERT INTO users VALUES(NULL, '{user_log.value}', '{user_pas.value}')""")

        db.commit()
        db.close()

        user_pas.value = ''
        user_log.value = ''

        page.update()


    def adds(e):
        
        textik.value += 1

        page.update


    def auth_us(e):
        pass


    btn = ft.Button('НАЖМИ', bgcolor="#ffffff", width=150, height=150, color='#000000', on_click=adds)
    
    textik = ft.Text(value=0, size=200)
    
    butt = ft.OutlinedButton('Добавить', icon=ft.Icons.ADD, width=150, height=50, disabled=True, style=ft.ButtonStyle(color='#de9191'),icon_color='#de9191', on_click=regis)
    butt_aut = ft.OutlinedButton('Войти', icon=ft.Icons.ADD, width=150, height=50, disabled=True, style=ft.ButtonStyle(color='#de9191'),icon_color='#de9191', on_click=auth_us)
 
    user_log = ft.TextField('', bgcolor='#ffffff', color='#000000', cursor_color='#de9191', autofocus=True, on_change=chan)
    log_text = ft.Text('Логин', size=20, color='#de9191')

    user_pas = ft.TextField('', bgcolor='#ffffff', color='#000000', cursor_color='#de9191', autofocus=True, password=True, on_change=chan)
    pas_text = ft.Text('Пароль', size=20, color='#de9191')


    coloms = ft.Row(
        [
            ft.Column(
                [
                    ft.Text('Регистрация', size=50, color="#de9191"),
                    log_text,
                    user_log
                ]
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    coloms1 = ft.Row(
        [
            ft.Column(
                [
                    pas_text,
                    user_pas
                ]
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    coloms_aut = ft.Row(
        [
            ft.Column(
                [
                    ft.Text('Авторизация', size=50, color="#de9191"),
                    log_text,
                    user_log
                ]
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    coloms1_aut = ft.Row(
        [
            ft.Column(
                [
                    pas_text,
                    user_pas
                ]
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )


    page.add(coloms_aut, coloms1_aut, butt_aut)


ft.app(target=main)