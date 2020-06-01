import PySimpleGUI as sg
from datetime import datetime
from os.path import isfile

#folder where dailies are stored
folder_path = '/Users/KailaNathaniel/Documents/dailies/'

#layout of input box
wayd_layout = [
    [sg.Text('What are you doing?')],
    [sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]

#create input box, take input
window = sg.Window('wayd', wayd_layout)
event, values = window.read()

#time that input was entered
time = datetime.now().strftime('%H:%M')

#today's date in two formats
date_dash = datetime.now().strftime('%Y-%m-%d')
date_dot = datetime.now().strftime('%d.%m.%Y')

#close input box
window.close()

#full path to daily note
full_path = folder_path + date_dash + '.md'

#if content has been entered
if values[0] != '':
    #if file already exists
    if isfile(full_path):
        f = open(folder_path + date_dash + '.md','a+')
        f.write('\n* ' + time + ': ' + values[0])
        f.close()
    #if file doesn't exist (aka program hasn't run today)
    else:
        f = open(folder_path + date_dash + '.md','w+')
        f.write('# ' + date_dot + '\n## today i will\n>==thrive==\n\n## ideas // thoughts // things i did\n* ' + time + ': ' + values[0])
        f.close()
#if no content entered
else:
    exit()
