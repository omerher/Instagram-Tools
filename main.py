import PySimpleGUI as sg
from instagram_poster import instagram_poster
from upload_helper import upload_helper
import threading


def poster(niche):
    instagram_poster(niche)


def tabs(num_posts):
    upload_helper(num_tabs)


sg.theme('LightGrey1')  # Add a touch of color
# All the stuff inside your window.

niches = ["ENTER NICHE HERE"] # Enter your niches, for example: niches = ["Cars", "Luxury"]

layout = [  [sg.Text('To get daily posts:')],
            [sg.Listbox(niches, size=(25, len(niches)), key="-NICHES-")],
            [sg.Text('Start Instagram Poster')],
            [sg.Button("Start")],
            [sg.Text("")],
            [sg.Text("Number of tabs: ")],
            [sg.InputText(size=(25,), key="-NUM_TABS-")],
            [sg.Button("Open Tabs")],
            [sg.Text("")],
            [sg.Button('Exit')] ]

# Create the Window
window = sg.Window('Instagram Tools', layout, grab_anywhere=True)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    if event == "Start":
        thread1 = threading.Thread(target=poster, args=(values["-NICHES-"][0],))
        thread1.start()
    if event == "Open Tabs":
        num_tabs = int(values["-NUM_TABS-"])
        thread2 = threading.Thread(target=tabs, args=(num_tabs,))
        thread2.start()

    if event in (None, 'Exit'):  # if user closes window or clicks cancel
        break

window.close()
