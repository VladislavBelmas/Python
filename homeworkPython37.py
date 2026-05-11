from _collections_abc import Iterable


class AudioFileMixin:

    def play_audio(self):
        if not hasattr(self, "audio_tracks"):
            raise AttributeError("Нет audio_tracks")

        if not isinstance(self.audio_tracks, Iterable):
            raise TypeError("audio_tracks должен быть списком")

        return (f"Воспроизведение аудио для {self.__class__.__name__}:\n"
                + "\n".join(self.audio_tracks))




class VideoFileMixin:

    def play_video(self):
        if not hasattr(self, "video_files"):
            raise AttributeError("Нет video_files")

        if not isinstance(self.video_files, Iterable):
            raise TypeError("video_files должен быть списком")

        return (f"Воспроизведение видео для {self.__class__.__name__}:\n"
                + "\n".join(self.video_files))




class MediaPlayer(AudioFileMixin):
    def __init__(self, audio_tracks):
        self.audio_tracks = audio_tracks


class Laptop(VideoFileMixin, AudioFileMixin):
    def __init__(self, audio_tracks, video_files):
        self.audio_tracks = audio_tracks
        self.video_files = video_files



media = MediaPlayer(["track1.mp3", "track2.mp3"])
laptop = Laptop(["track1.mp3", "track2.mp3"], ["movie.mp4", "trailer.mov"])


print(media.play_audio())
print(laptop.play_audio())
print(laptop.play_video())









