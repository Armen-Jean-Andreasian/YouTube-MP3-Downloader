from scripts.reader import ReadFile
from scripts.download import Downloader

if __name__ == '__main__':
    try:
        text_one = "Input the full path to the text file with urls.\n" + r"Example: C:\Users\pc\Desktop\links.txt" + "\n> "
        custom_urls_file = input(text_one).strip()

        text_two = "\nInput the destination folder.\n" + r"Example: C:\\Users\pc\Desktop\playlist" + "\n\n> "
        custom_downloads_folder = input(text_two).strip()

        # invoking urls
        urls = ReadFile.read(file_with_urls=custom_urls_file)

        for url in urls:
            try:
                downloader = Downloader(url, downloads_folder=custom_downloads_folder)
                print(f'\n{downloader.download()}')
            except TypeError:
                print(f"The video is 18+. Try another url of the same song. E.g. clean version, or only song without a video clip.")
            continue

    except KeyboardInterrupt:
        exit()

    input("Press Enter to exit...")

r"""

C:\Users\pc\Desktop\dummy\links.txt
C:\Users\pc\Desktop\dummy
"""
# pyinstaller --onefile --icon=icon.ico cli.py
