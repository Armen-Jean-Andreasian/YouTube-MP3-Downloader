from reader import ReadFile
from download import Downloader

if __name__ == '__main__':
    urls = ReadFile.read()
    for url in urls:
        downloader = Downloader(url)
        downloader.download()
        continue
