import PySimpleGUI as sg

from scripts.download import Downloader
from scripts.reader import ReadFile

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

        status_elem.update("DONE!", text_color='Green')
