import PySimpleGUI as sg

import threading

from RELEASES.gui.elements.layout import get_layout

from RELEASES.gui.menu_bar.about import get_about
from RELEASES.gui.menu_bar.how_to_use import usage

from RELEASES.gui.gui_scripts.download_song import download_and_display
from RELEASES.gui.gui_scripts.open_folder import open_downloads_folder
from files.config import get_logo

# initialization
sg.theme('DarkRed1')
window = sg.Window("YouTube MP3 downloader", layout=get_layout(), icon=get_logo())


# functionality
def main():
    # Access the status elements for displaying status
    status_elem = window['status']

    window['Submit'].update(disabled=True)
    status_elem.update("Downloading...", text_color='Blue')

    # Create a thread for downloading and displaying
    download_thread = threading.Thread(target=download_and_display,
                                       args=(file_path, folder_path, window['output'], status_elem))
    download_thread.start()


threads_count = 0
while True:
    event, values = window.read()

    # unfreeze the buttons
    file_path_local = values['file']
    folder_path_local = values['folder']

    # Menu About
    if event == "About":
        get_about()
    # Menu Usage
    if event == "How to use?":
        usage()

    # Submit
    if event == "Submit" and threads_count == 0:
        file_path = values['file']
        folder_path = values['folder']

        if file_path and folder_path:
            main()
            threads_count += 1
        else:
            sg.popup_annoying("Empty value!")

    # View
    if event == "View Downloads":
        open_downloads_folder(values=values)

    # Exit
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

window.close()
