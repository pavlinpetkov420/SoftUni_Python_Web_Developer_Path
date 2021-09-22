from spoopify.project.album import Album


class Band:

    def __init__(self, name, *args):
        self.name = name
        self.albums = [album for album in args]

    def add_album(self, album: Album):
        for a in self.albums:
            if a == album:
                return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for alb in self.albums:
            if alb == album_name:
                if alb.published:
                    return "Album has been published. It cannot be removed."
                else:
                    self.albums.remove(alb)
                    return f"Album {album_name.name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        band_details = f"Band {self.name}\n"
        for album in self.albums:
            band_details += f'{album.details()}\n'
        return band_details



