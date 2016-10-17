import winsound
import sounds


class SoundPlayer:
    @staticmethod
    def play(sound):
        for d in sound:
            winsound.Beep(int(SoundPlayer.__note_to_frequency(SoundPlayer.__read_sound_note(d))), SoundPlayer.__read_sound_time(d))

    @staticmethod
    def __note_to_frequency(note):
        return sounds.note_frequency_mapping[note]

    @staticmethod
    def __read_sound_note(sound_dict):
        return next(iter(sound_dict.values()))

    @staticmethod
    def __read_sound_time(sound_dict):
        return next(iter(sound_dict.keys())) * 1000
