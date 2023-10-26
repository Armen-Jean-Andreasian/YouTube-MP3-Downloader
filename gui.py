import PySimpleGUI as sg
import threading
from elements.layout import get_layout
from menu_bar.about import get_about
from menu_bar.how_to_use import usage
from gui_scripts.download_song import download_and_display
from gui_scripts.open_folder import open_downloads_folder


sg.theme('DarkRed1')
window = sg.Window(title="YouTube MP3 downloader", layout=get_layout(), icon='files/logo_.ico')


def main():
    status_elem = window['status']

    window['Submit'].update(disabled=True)
    status_elem.update("Downloading...", text_color='Blue')
    download_thread = threading.Thread(target=download_and_display,
                                       args=(file_path, folder_path, window['output'], status_elem))
    download_thread.start()


threads_count = 0
while True:
    event, values = window.read()

    file_path_local = values['file']
    folder_path_local = values['folder']

    if event == "About":
        get_about()
    if event == "How to use?":
        usage()

    if event == "Submit" and threads_count == 0:
        file_path = values['file']
        folder_path = values['folder']

        if file_path and folder_path:
            main()
            threads_count += 1
        else:
            sg.popup_annoying("Empty value!")

    if event == "View Downloads":
        open_downloads_folder(values=values)
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

window.close()
