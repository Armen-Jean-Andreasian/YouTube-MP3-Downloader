from scripts.reader import ReadFile
from scripts.download import Downloader

if __name__ == '__main__':
    custom_urls_file = r"C:\Users\pc\Desktop\dummy\links.txt"
    custom_downloads_folder = r'C:\Users\pc\Desktop\dummy'

    # invoking urls
    urls = ReadFile.read(file_with_urls=custom_urls_file)

    for url in urls:
        try:
            downloader = Downloader(url, downloads_folder=custom_downloads_folder)
            print(downloader.download())
        except TypeError:
            print(
                f"The video is 18+. Try another url of the same song. E.g. clean version, or only song without a video clip.")
        except Exception:
            print("Could not connect to YouTube. Try again in 30 seconds.")
        continue
