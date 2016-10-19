from sounds import *
from soundplayer import SoundPlayer
def main():
    sound = song_closer
    SoundPlayer.play_beep(sound)

# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
