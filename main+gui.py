import PySimpleGUI as sg
from reader import ReadFile
from download import Downloader
import threading
import os

sg.theme('LightGrey1')

layout = [
    [sg.Titlebar(title="YouTube MP3 downloader", background_color='Black')],
    [
        sg.Column([
            [sg.Text("Choose the text file with URLs")],
            [sg.Text("Choose the destination folder")],
        ]),
        sg.Column([
            [sg.FileBrowse(key='file')],
            [sg.FolderBrowse(key='folder')],
        ]),
        sg.Column([
            [sg.Text("Chosen URl FIle", key='file_text')],
            [sg.Text("Chosen output directory", key='folder_text')],
        ]),
    ],
    [sg.Multiline(size=(80, 10), key='output', reroute_cprint=True, disabled=True)],
    [sg.Text("", key='status', size=(30, 1), font='bold', text_color='green')],
    [sg.Button("Submit", button_color='Black'), sg.Button("View Downloads", button_color='Black'), sg.Button("Exit", button_color='Black')]
]

window = sg.Window("YouTube MP3", layout)

downloaded_songs = []  # List to store downloaded song names


def download_and_display(file_path, folder_path, output_elem, status_elem):
    if file_path and folder_path:
        urls = ReadFile.read(file_with_urls=file_path)

        for url in urls:
            try:
                downloader = Downloader(url, downloads_folder=folder_path)
                downloading_song = downloader.download()

                # Append the downloaded song name to the list
                downloaded_songs.append(downloading_song)
                # Update the display in the PySimpleGUI window with the entire list
                output_elem.print(downloading_song + '\n')

            except TypeError:
                error_message = "The video is 18+. Try another URL of the same song, e.g., clean version or only the song without a video clip."
                sg.popup_error(error_message, title='Error', font=('Helvetica', 12, 'bold'), non_blocking=True)
            except Exception as e:
                error_message = "An error occurred: " + str(e)
                output_elem.print(error_message)

        # Update the status text when all songs are downloaded
        status_elem.update("DONE!", text_color='Green')
        sg.popup_notify("Downloads are complete.")


def main():
    file_path = values['file']
    folder_path = values['folder']

    if file_path and folder_path:
        # Access the status elements for displaying status
        status_elem = window['status']

        window['Submit'].update(disabled=True)
        status_elem.update("Downloading...", text_color='Blue')

        # Create a thread for downloading and displaying
        download_thread = threading.Thread(target=download_and_display,
                                           args=(file_path, folder_path, window['output'], status_elem))
        download_thread.start()
    else:
        sg.popup_notify("Empty value!")


def open_downloads_folder():

    if event['folder']:
        folder_path = values['folder']
        if os.path.exists(folder_path):
            os.startfile(folder_path)
    else:
        sg.popup_annoying("Choose the destination folder")



thread_count = 0
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

    if event == "Submit" and thread_count == 0:
        main()
        thread_count += 1

    if event == "View Downloads":
        open_downloads_folder()

window.close()
