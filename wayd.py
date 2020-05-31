import PySimpleGUI as sg
from datetime import datetime
import schedule
import time


#TODO not working? if I run this, then it only runs once, when i call just jobs(), it doesn't make it into the while loop
# settings_layout = [[sg.Text('Where do you want your files kept?')],
#       [sg.Text('wayd folder', size=(15, 1)), sg.InputText(), sg.FolderBrowse(initial_folder = '~/Documents')],
#       [sg.Submit(), sg.Cancel()]]
#
# settings_window = sg.Window('Settings', settings_layout)
#
# settings_event, settings_values = settings_window.read()
# settings_window.close()
# folder_path = settings_values[0]     # get the data from the values dictionary


folder_path = 'your/desired/path'

def job():
    # Very basic window.  Return values using auto numbered keys
    wayd_layout = [
        [sg.Text('What are you doing?')],
        [sg.InputText()],
        [sg.Submit(), sg.Cancel()]
    ]

    window = sg.Window('wayd', wayd_layout)
    event, values = window.read()
    window.close()

    date = datetime.now().strftime('%Y-%m-%d')
    time = datetime.now().strftime('%H:%M')

    if values[0] != '':
        f = open(folder_path + date + '.md','a+')
        f.write('\n' + time + '\t' + values[0])
        f.close()

job()

schedule.every(15).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
