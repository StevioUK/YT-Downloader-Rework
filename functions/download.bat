@echo off 
@REM echo %1 
@REM echo %2 
@REM echo %3
yt-dlp -f "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=mp3]/best[ext=mp4]/best" %1
@REM pause