from reader import ReadFile
from download import Downloader

if __name__ == '__main__':
    custom_urls_file = r"C:\Users\pc\Desktop\links.txt"
    custom_downloads_folder = r'C:\Users\pc\Desktop\playlist'

    # invoking urls
    urls = ReadFile.read(file_with_urls=custom_urls_file)

    for url in urls:
        try:
            downloader = Downloader(url, downloads_folder=custom_downloads_folder)
            downloader.download()
        except TypeError:
            print(f"The video is 18+. Try another url of the same song. E.g. clean version, or only song without a video clip.")
        continue
