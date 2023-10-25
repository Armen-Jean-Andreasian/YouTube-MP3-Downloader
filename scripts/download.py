import os
import pytube
import time
from moviepy.editor import AudioFileClip


class Downloader:
    def __init__(self, url: str, downloads_folder: os.path = None):
        self.yt = pytube.YouTube(url)
        self.filename = self.yt.streams[0].title

        if not downloads_folder:
            downloads_folder = "downloads"
            self.downloads_folder_path = os.path.join(os.curdir, downloads_folder)
        else:
            self.downloads_folder_path = downloads_folder


        # Creates the downloads folder if it doesn't exist
        os.makedirs(self.downloads_folder_path, exist_ok=True)

        self.mp3_output_path = self.downloads_folder_path + self.filename + '.mp3'

    def download(self):
        """
        1. Switches the directory to downloads folder
        2. Creates a video stream
        3. Downloads it as an mp4 file at specified downloads folder
        4. Invokes the content of the file
        5. Transforms into mp3
        6. Saves as filename + .mp3
        7. Deletes the .mp4 leftovers
        """

        # switching dir to downloads
        original_directory = os.getcwd()
        os.chdir(self.downloads_folder_path)

        # creating a video stream, downloading in .mp4 format
        video_stream = self.yt.streams.filter(only_audio=True).first()
        mp4_file_fullpath = video_stream.download(output_path=os.curdir)

        # converting mp3 -> mp4
        file = AudioFileClip(mp4_file_fullpath)
        file.write_audiofile(self.filename + '.mp3')
        file.close()
        time.sleep(3)
        try:
            # deleting mp4 leftovers
            os.remove(self.filename + '.mp4')
            os.chdir(original_directory)
        except FileNotFoundError:
            return f"{self.filename} | Status: Done. However, the deletion of the .mp4 file failed. You may need to delete the .mp4 file manually."

        except pytube.exceptions.AgeRestrictedError as error:
            return f"Error {error} occurred during proceeding of the track {self.filename}"

        except TypeError:
            return "The video is 18+"

        return f"{self.filename} | Status: Done"


if __name__ == '__main__':
    link = "https://www.youtube.com/watch?v=Lg35jIwoWcQ"
    downloader = Downloader(link)
    print(downloader.download())
