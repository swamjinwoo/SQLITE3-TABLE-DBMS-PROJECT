import PySimpleGUI as sg
import sqlite3
from showDataWindow import ShowDataWindow
class homeWindow(): 
    def __init__(self) -> None:
        self.layout = [ 
                       [sg.Text('Book ID'), sg.Push(),sg.InputText(key='BID')],
                       [sg.Text('Book Name'), sg.Push(),sg.InputText(key='BNAME')],
                       [sg.Text('Author Name'), sg.Push(),sg.InputText(key='AUTHOR')],
                       [sg.Text('Student Name'), sg.Push(),sg.InputText(key='STUDENT')],
                       [sg.Text('Student Roll'), sg.Push(),sg.InputText(key='ROLL')],
                       [sg.Button('Insert', key='INSERT'), sg.Button('View')]
            ]
        self.window = sg.Window('Main',self.layout)
            
    def run(self): 
        try: 
            while True: 
                event, values = self.window.read()
                if event == 'INSERT': 
                    conn = sqlite3.connect('records.db')
                    cursor = conn.cursor()
                    sql = '''INSERT INTO library
                                VALUES(?,?,?,?,?)'''
                    data = (values['BID'],values['BNAME'], values['AUTHOR'], values['STUDENT'], values['ROLL'])
                    try:
                        cursor.execute(sql,data)
                        conn.commit()
                        sg.Popup('Data insert success')
                        self.window['BID'].update('')
                        self.window['BNAME'].update('')
                        self.window['ROLL'].update('')
                        self.window['AUTHOR'].update('')
                        self.window['STUDENT'].update('')
                    except Exception as ex: 
                        sg.Popup(ex)
                elif event == 'View': 
                    ShowDataWindow().run()
                elif event == sg.WIN_CLOSED: 
                    break
                    
        except Exception as exception: 
            sg.Popup(exception)