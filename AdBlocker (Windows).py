import subprocess
import time

def open_spotify_and_play(playlist_uri):
    app_name = "Spotify"
    try:
        subprocess.Popen(["spotify.exe"])
    except FileNotFoundError:
        print(f"The application '{app_name}' was not found.")

    time.sleep(5)

    try:
        subprocess.Popen(["spotify.exe", f'--uri="{playlist_uri}"'])
    except subprocess.CalledProcessError:
        print(f"Failed to play playlist in '{app_name}'.")

def close_spotify():
    app_name = "Spotify"
    try:
        subprocess.Popen(["taskkill", "/f", "/im", "spotify.exe"])
    except subprocess.CalledProcessError:
        print(f"Failed to close '{app_name}'.")

def is_spotify_running():
    try:
        output = subprocess.check_output(["tasklist", "/fi", "imagename eq spotify.exe"]).decode("utf-8")
        return "Spotify.exe" in output
    except subprocess.CalledProcessError:
        return False

def get_track_duration():

    return 0

playlist_uri = "spotify:playlist:YOUR_PLAYLIST_URI"

if not is_spotify_running():
    open_spotify_and_play(playlist_uri)

while True:
    if is_spotify_running():
        current_duration = get_track_duration()

        print(f"Current Duration: {current_duration} seconds")

        if current_duration <= 30:
            close_spotify()

            time.sleep(2)
            
            open_spotify_and_play(playlist_uri)

    time.sleep(5)
