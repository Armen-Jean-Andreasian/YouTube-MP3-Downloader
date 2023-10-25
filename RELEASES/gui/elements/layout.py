from RELEASES.gui.elements.widgets import Widgets

left_column = Widgets.left_column()
middle_column = Widgets.middle_column()
right_column = Widgets.right_column()

downloads_list = Widgets.downloads_list()

download_status = Widgets.download_status()
bottom_panel = Widgets.bottom_panel()

submit_button = bottom_panel[0]
view_downloads_button = bottom_panel[1]


def get_layout():
    layout = [
        [
            left_column,
            middle_column,
            right_column,
        ],
        downloads_list,
        download_status,
        bottom_panel
    ]
    return layout
