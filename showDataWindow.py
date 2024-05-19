import PySimpleGUI as sg
import sqlite3
from updateWindow import UpdateWindow

class ShowDataWindow():
    def __init__(self):
        self.layout = [
            [
                sg.Table(values=self.connectme(),
                         headings=['Book ID', 'Book Name', 'Author Name', 
                                   'Student Name', 'Student Roll'],
                         auto_size_columns=False, 
                         num_rows=10,
                         key='TABLE', 
                         enable_events=True, 
                         ), 
                sg.Button('Delete'), 
                sg.Button('Update')
             ],
            [
                sg.Button('Exit')
            ]
        ]
        self.window = sg.Window('View Data', self.layout)
        self.selected_row = None
        
    def connectme(self): 
        conn = sqlite3.connect('records.db')
        cursor = conn.cursor()
        sql = '''SELECT * FROM library'''
        cursor.execute(sql)
        data = cursor.fetchall()
        conn.close()
        return data
    
    def deleteRecord(self):
        data = self.connectme()
        book_id = data[self.selected_row][0]
        conn = sqlite3.connect("records.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM library WHERE bookID=?", (book_id,))
        conn.commit()
        conn.close()
        
    def refreshTable(self): 
        data = self.connectme()
        self.window['TABLE'].update(values=data)
        
    def update(self,old_bookID, new_bookID, bookName, author, studentName, studentRoll): 
        conn = sqlite3.connect('records.db')
        cursor = conn.cursor()
        cursor.execute('''UPDATE library 
                          SET bookID = ?,bookName = ?, author = ?, studentName = ?, studentRoll = ?
                          WHERE bookID = ?;''', 
                       (new_bookID,bookName, author, studentName, studentRoll, old_bookID))
        conn.commit()
        conn.close()
        self.refreshTable()
    
    
    def run(self): 
        while True: 
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'Exit': 
                break
            elif event == 'TABLE': 
                if values['TABLE']:
                    self.selected_row = values['TABLE'][0]
            elif event == 'Delete' and self.selected_row is not None: 
                self.deleteRecord()
                self.refreshTable()
            elif event == 'Update' and self.selected_row is not None: 
                book_id = self.connectme()[self.selected_row][0]
                update_window = UpdateWindow(self, book_id)
                update_window.run()
        
        self.window.close()

if __name__ == '__main__':
    
    window = ShowDataWindow()
    window.run()