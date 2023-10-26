import PySimpleGUI as pg


def get_about():
    about_text = """
    YouTube MP3 Downloader

    This application allows you to easily download audio from YouTube videos in MP3 format. 
    Simply provide the URL of the YouTube video, and the downloader will take care of the rest.

    Enjoy downloading your favorite music from YouTube with ease!

    Author: Armen-Jean Andreasian
    Version: 1.0
    """
    return pg.popup(about_text, title="About")
