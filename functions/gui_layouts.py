import PySimpleGUI as gui

class Layouts:

    def __init__(self):
        print("Running")

    def layout_console(self):
        frame_layout = [[gui.Multiline("", size=(80, 20), autoscroll=True, reroute_stdout=True, reroute_stderr=True, key='console_output')]]

        layout = [
            [gui.Frame("Output console", frame_layout)]
        ]

        return layout
    
    def layout_base(self):

        layout = [
            [gui.Text("Video Link", pad=(0,0))],

            [gui.Input("", pad=(0,0), key='video_input')],

            [gui.Button("Download Video", pad=(0,10), key="video_download")],

            # [gui.Button("Download Directory", pad=(0,10), key="video_directory")],
        ]

        return layout