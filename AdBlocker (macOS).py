import subprocess
import time

def open_spotify_and_play(playlist_uri):
    app_name = "Spotify"
    try:
        subprocess.call(["open", "-a", app_name])
    except FileNotFoundError:
        print(f"The application '{app_name}' was not found.")

    time.sleep(3)

    try:
        applescript = f'tell application "{app_name}" to play track "{playlist_uri}"'
        subprocess.call(["osascript", "-e", applescript])
    except subprocess.CalledProcessError:
        print(f"Failed to play playlist in '{app_name}'.")

def close_spotify():
    app_name = "Spotify"
    try:
        subprocess.call(["osascript", "-e", f'tell application "{app_name}" to quit'])
    except subprocess.CalledProcessError:
        print(f"Failed to close '{app_name}'.")

def get_track_duration():
    app_name = "Spotify"
    try:
        duration = subprocess.check_output(["osascript", "-e", f'tell application "{app_name}" to duration of current track as string'])
        return int(duration.decode("utf-8").strip())
    except subprocess.CalledProcessError:
        return 0
    
def is_spotify_running():
    return subprocess.call(["pgrep", "-x", "Spotify"]) == 0


playlist_uri = "spotify:playlist:YOUR_PLAYLIST_URI"


while True:

    if not is_spotify_running():
        open_spotify_and_play(playlist_uri)

    if is_spotify_running:
        current_duration = get_track_duration()
        print(f'Track Duration: {current_duration // 1000}')

        if current_duration // 1000 == 30 or current_duration // 1000 == 15:
            close_spotify()
            time.sleep(2)
            open_spotify_and_play(playlist_uri)

    time.sleep(5)


