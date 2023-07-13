import PySimpleGUI as gui

# gui imports
import gui_theme
import gui_layouts
import gui_debug
import YTDownloader as ytd

import os

def window():

    gui_debug.window()

    config = gui_layouts.Layouts()
    
    layout = config.layout_base()

    window = gui.Window("Youtube Video Downloader", layout, icon=f"{os.getcwd()}/crow_1.ico", size=(400, 100), element_justification='c', finalize=True)

    window.set_title("Youtube Video Downloader")

    return window

def event_handlers(window_a):

    while True:
        window, event, values = gui.read_all_windows()

        if (window == window_a and event == gui.WIN_CLOSED):
            break

        match event:
            case gui.WIN_CLOSED:
                window.close()

            case "video_download":
                link = values['video_input']
                print(link)
                # ytd.downloadVideo(link)
                window.perform_long_operation(lambda : ytd.downloadVideo(link), "download_video")

            case "video_directory":
                path = directory.grab_directory()

                # if (os.path.isfile(f"{os.getcwd()}/settings.json")):
                x = {
                    "directory": path,
                }

                gui_settings.save_to_json(x, "settings")

def window_init():

    # if (os.path.isfile(f"{os.getcwd()}/settings.json")):
    #     print("Settings file found")

    #     json = gui_settings.read_from_json("settings")

    #     if "theme" in json:
    #         print("Theme found")
    #         gui_theme.change(json["theme"])
    #     else:
    #         print("Theme not found, using default")
            
    #         x = {
    #             "theme": "Dark",
    #         }

    #         gui_settings.update_to_json(x, "settings")
    # else:

    #     gui_theme.change("Dark")

    #     x = {
    #         "init": "active",
    #     }

    #     gui_settings.save_to_json(x, "settings")

    #     gui_settings.select_tools()

    # window_b = gui_debug.window_debug()

    gui_theme.change("DarkAmber")

    window_a = window()
    event_handlers(window_a)

window_init()