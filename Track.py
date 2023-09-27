class Track:

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def show(self):
        print(f'{self.name}-{self.duration}')


class Album:

    def __init__(self, name, group, tracks):
        self.name = name
        self.group = group
        self.tracks = tracks

    def get_tracks(self):
        for track in self.tracks:
            track.show()

    def add_track(self, track):
        self.tracks.append(track)

    def get_duration(self):
        album_duration = 0
        for track in self.tracks:
            album_duration += track.duration
        print('Длительность альбома', album_duration)


violator_tracks = [Track('Personal Jesus', 5), Track('Enjoy the Silence', 4), Track('Clean', 3)]
violator = Album('Violator', 'Depeche Mode', violator_tracks)
violator.get_duration()

smiths_tracks = [Track('Reel Around the Fountain', 7), Track('Miserable Lie', 4), Track('Pretty Girls Make Graves', 3)]
smiths_album = Album('The Smiths', 'The Smiths', smiths_tracks)
smiths_album.get_duration()
