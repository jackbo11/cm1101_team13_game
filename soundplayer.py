import winsound
import sounds


class SoundPlayer:
    @staticmethod
    def play_beep(sound):
        for d in sound:
            winsound.Beep(int(SoundPlayer.__note_to_frequency(SoundPlayer.__read_sound_note(d))), int(SoundPlayer.__read_sound_time(d)))

    @staticmethod
    def play_error():
        winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)

    @staticmethod
    def play_wav(filename):
        winsound.PlaySound(filename, winsound.SND_FILENAME)

    @staticmethod
    def __note_to_frequency(note):
        return sounds.note_frequency_mapping[note]

    @staticmethod
    def __read_sound_note(sound_dict):
        return next(iter(sound_dict.values()))

    @staticmethod
    def __read_sound_time(sound_dict):
        return next(iter(sound_dict.keys())) * 1000
