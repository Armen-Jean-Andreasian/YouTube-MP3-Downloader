import PySimpleGUI as sg

sg.theme('DarkRed1')


class Widgets:
    @staticmethod
    def left_column() -> sg.Column:
        return sg.Column([
            [sg.Text("Choose the text file containing URL-s:")],
            [sg.Text("Choose the destination folder:")],
        ])

    @staticmethod
    def right_column() -> sg.Column:
        return sg.Column([
            [sg.FileBrowse(key='file', enable_events=True, target='file_input', file_types=(('Text Files', '*.txt'),))],
            [sg.FolderBrowse(key='folder', enable_events=True, target='folder_input')],
        ])

    @staticmethod
    def middle_column() -> sg.Column:
        return sg.Column([
            [sg.Input(key='file_input', disabled=True)],
            [sg.Input(key='folder_input', disabled=True)],
        ])

    @staticmethod
    def downloads_list():
        return [sg.Multiline(size=(89, 10), key='output', autoscroll=True, reroute_cprint=True, disabled=True,
                             sbar_trough_color="Red")]

    @staticmethod
    def download_status():
        return [sg.Text("", key='status', font='bold')]

    @staticmethod
    def bottom_panel():
        return [sg.Button("Submit"),
                sg.Button("View Downloads"),
                sg.Button("Exit"),
                ]
