import PySimpleGUI as pg

usage_text = """
    How it works:
    
    1. Create a .txt file with your video URL-s:
        - URL-s should be separated by commas
        - Each url on one line
        - Last URL should not be followed by a comma
        
    2. Select the text file. 
    3. Select the output destination.
    4. Press Submit

    Note:
        - Age-restricted content can't be downloaded.
"""


def usage():
    return pg.popup(usage_text, title="Usage")
