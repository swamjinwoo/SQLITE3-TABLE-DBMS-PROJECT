import PySimpleGUI as sg 

class UpdateWindow: 
    def __init__(self, main_window, book_id):
        self.main_window = main_window 
        self.old_book_id = book_id
        self.col1 = [ 
                       [sg.Text('Book ID'), sg.InputText(key='bookID',default_text=int(book_id))], 
                       [sg.Text('Book Name'), sg.InputText(key='BookName')], 
                       [sg.Text('Author'), sg.InputText(key='Author')], 
                       [sg.Text('Student Name'), sg.InputText(key='StudentName')], 
                       [sg.Text('Student Roll'), sg.InputText(key='Roll')]
                       ]
        self.col2 = [     
                     [sg.Button('Update')]
                     ]
        self.layout=[self.col1,self.col2]
        self.window = sg.Window('Update Window', self.layout)
        
    def run(self): 
        while True: 
            event , values = self.window.read()
            if event == sg.WIN_CLOSED: 
                break 
            elif event == 'Update': 
                try: 
                    new_bookID = int(values['bookID'])
                    bookName = values['BookName']
                    author = values['Author']
                    studentName = values['StudentName']
                    studentRoll = int(values['Roll'])
                    self.main_window.update(self.old_book_id, new_bookID, bookName, author, studentName, studentRoll)
                    break
                except Exception as ex: 
                    sg.Popup(ex)
                    
        self.window.close()