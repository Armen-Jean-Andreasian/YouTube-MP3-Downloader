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
    ],

    [sg.Multiline(size=(80, 10), key='output', reroute_cprint=True, disabled=True)],  # Create a multiline element to display output
    [sg.Text("", key='status', size=(30, 1), text_color='green')],  # Status text

    [sg.Button("Submit", button_color='Gray'), sg.Button("View Downloads", button_color='Black')]

]
window = sg.Window("YouTube MP3", layout)

downloaded_songs = []  # List to store downloaded song names


def download_and_display(file_path, folder_path, output_elem, status_elem):
    if file_path and folder_path:
        urls = ReadFile.read(file_with_urls=file_path)

        for url in urls:
            try:
                downloader = Downloader(url, downloads_folder=folder_path)
                downloader.download()

                # Append the downloaded song name to the list
                downloaded_songs.append(downloader.filename)
                # Display the download progress in the PySimpleGUI window
                output_elem.update(downloader.filename + ' - Done.\n')

            except TypeError:
                sg.popup_error(
                    "The video is 18+. Try another URL of the same song, e.g., clean version or only the song without a video clip.")
            except Exception as e:
                output_elem.update("An error occurred: " + str(e) + '\n')

        # Update the status text when all songs are downloaded
        status_elem.update("DONE!")


def main():
    file_path = values['file']
    folder_path = values['folder']

    if file_path and folder_path:
        # Access the multiline and status elements for displaying output and status
        output_elem = window['output']
        status_elem = window['status']

        window['Submit'].update(disabled=True)
        window['status'].update("Downloading...")

        # Create a thread for downloading and displaying
        download_thread = threading.Thread(target=download_and_display,
                                           args=(file_path, folder_path, output_elem, status_elem))
        download_thread.start()
    else:
        sg.popup_error("Empty value!")


def open_downloads_folder(folder_path):
    if os.path.exists(folder_path):
        os.startfile(folder_path)


thread_count = 0
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "Submit" and thread_count == 0:
        main()
        thread_count += 1


    if event == "View Downloads":
        open_downloads_folder(values['folder'])

window.close()
