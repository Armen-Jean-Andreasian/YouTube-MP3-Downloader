import os

import PySimpleGUI as sg


def open_downloads_folder(values):
    # checks if destination is given

    folder_path = values['folder']
    if not folder_path:
        sg.popup_annoying("No specified destination folder")
    else:
        if os.path.exists(folder_path):
            os.startfile(folder_path)
