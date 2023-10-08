import subprocess
import time

# Function to open Spotify and play the playlist
def open_spotify_and_play(playlist_uri):
    app_name = "Spotify"
    try:
        subprocess.call(["open", "-a", app_name])
    except FileNotFoundError:
        print(f"The application '{app_name}' was not found.")
    
    # Wait for a few seconds to give Spotify time to open
    time.sleep(3)
    
    # Play the specified playlist using AppleScript
    try:
        applescript = f'tell application "{app_name}" to play track "{playlist_uri}"'
        subprocess.call(["osascript", "-e", applescript])
    except subprocess.CalledProcessError:
        print(f"Failed to play playlist in '{app_name}'.")

# Function to close Spotify
def close_spotify():
    app_name = "Spotify"
    try:
        subprocess.call(["osascript", "-e", f'tell application "{app_name}" to quit'])
    except subprocess.CalledProcessError:
        print(f"Failed to close '{app_name}'.")

# Function to check the current track's duration in seconds
def get_track_duration():
    app_name = "Spotify"
    try:
        duration = subprocess.check_output(["osascript", "-e", f'tell application "{app_name}" to duration of current track as string'])
        return int(duration.decode("utf-8").strip())
    except subprocess.CalledProcessError:
        return 0
    
def is_spotify_running():
    return subprocess.call(["pgrep", "-x", "Spotify"]) == 0


# Replace with the actual Spotify playlist URI you want to play
playlist_uri = "spotify:playlist:https://open.spotify.com/playlist/3eDgZy7hcDzbRTVGAEOjLz?si=6d2739b3878a4bce"


# Continuously monitor Spotify's state
while True:

    if not is_spotify_running():
        open_spotify_and_play(playlist_uri)

    if is_spotify_running:
        # Get the current track's duration in seconds
        current_duration = get_track_duration()
        print(f'Track Duration: {current_duration // 1000}')
        
        # If the current duration is 30 seconds or less, close Spotify
        if current_duration // 1000 == 30:
            close_spotify()
            time.sleep(2)
            open_spotify_and_play(playlist_uri)
    
    # Sleep for a short interval (e.g., 5 seconds) before checking again
    time.sleep(5)


