import subprocess
import os

def downloadVideo(link):

    if (link == ""):
        print("Try adding a link first!")
        exit()

    # seen as youtube has 2 main links, we need to check if link is youtu.be or youtube.com as both use a different denominator

    if ("youtube.com" in link):
        link_end = link.split("=")[1] # grab the specific identifier, denominator is =
    else:
        if ("youtu.be" in link):
            link_end = link.split("be/")[1] # grab the specific identifier, denominator is be/
        else:
            print("This link isn't a valid youtube link! Supported links are youtu.be and youtube.com!") # this or yt changed their link (unlikely)
            exit()

    # as you can tell i'm good friends with the yandere simulator dev!

    try:

        p = subprocess.Popen(["functions\download.bat", link_end]) # run the download.bat with link argument
        p.wait() # wait for process to terminate

        title = subprocess.getoutput(f"yt-dlp --print filename {link}")
        # print(title)

        # print(f"{os.getcwd()}\{title[:-4]}.mp4")
        # print(f"{os.getcwd()}\videos\{title[:-4]}.mp4")
        # shutil.move(f"{os.getcwd()}\{title[:-4]}.mp4", f"{os.getcwd()}\videos\{title[:-4]}.mp4")
        # I have many a problem with silent fails
        print(f"The video has been downloaded to {os.getcwd()}\{title[:-4]}.mp4")

    except:
        print("Something went wrong while downloading the video. Sorry!")