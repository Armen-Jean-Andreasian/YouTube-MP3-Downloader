import sys
from cx_Freeze import setup, Executable

logo = 'logo_.ico'
build_exe_options = {
    "packages": ["pytube", "moviepy", "PySimpleGUI"],
    "includes": ["atexit"],
    "excludes": [],
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable("gui.py", base=base, icon=logo)
]

setup(
    name="YouTube MP3 downloader",
    version="1.0",
    description="This application allows you to easily download audio from YouTube videos in MP3 format.",
    options={"build_exe": build_exe_options},
    executables=executables
)
