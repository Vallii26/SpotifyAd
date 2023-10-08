import subprocess
import time

# Function to open Spotify and play the playlist
def open_spotify_and_play(playlist_uri):
    app_name = "Spotify"
    try:
        subprocess.Popen(["spotify.exe"])
    except FileNotFoundError:
        print(f"The application '{app_name}' was not found.")
    
    # Wait for a few seconds to give Spotify time to open
    time.sleep(5)
    
    # Play the specified playlist using Spotify URI (requires Spotify Premium)
    try:
        subprocess.Popen(["spotify.exe", f'--uri="{playlist_uri}"'])
    except subprocess.CalledProcessError:
        print(f"Failed to play playlist in '{app_name}'.")

# Function to close Spotify
def close_spotify():
    app_name = "Spotify"
    try:
        subprocess.Popen(["taskkill", "/f", "/im", "spotify.exe"])
    except subprocess.CalledProcessError:
        print(f"Failed to close '{app_name}'.")

# Function to check if Spotify is running
def is_spotify_running():
    try:
        output = subprocess.check_output(["tasklist", "/fi", "imagename eq spotify.exe"]).decode("utf-8")
        return "Spotify.exe" in output
    except subprocess.CalledProcessError:
        return False

# Function to get the current track's duration in seconds
def get_track_duration():
    # Unfortunately, directly querying track duration is not straightforward in the Spotify desktop app on Windows
    # You may need to explore using Spotify's Web API for better track duration retrieval

    # For simplicity, this function returns a dummy value (0 seconds)
    return 0

# Replace with the actual Spotify playlist URI you want to play
playlist_uri = "spotify:playlist:YOUR_PLAYLIST_URI"

# Check if Spotify is running; if not, open it
if not is_spotify_running():
    open_spotify_and_play(playlist_uri)

# Continuously monitor Spotify's state
while True:
    # Check if Spotify is running
    if is_spotify_running():
        # Get the current track's duration in seconds (dummy value)
        current_duration = get_track_duration()
        
        # Print the current duration for debugging purposes
        print(f"Current Duration: {current_duration} seconds")
        
        # If the current duration is 30 seconds or less, close Spotify
        if current_duration <= 30:
            close_spotify()
            
            # Wait for about 2 seconds before reopening the app
            time.sleep(2)
            
            open_spotify_and_play(playlist_uri)
    
    # Sleep for a short interval (e.g., 5 seconds) before checking again
    time.sleep(5)
