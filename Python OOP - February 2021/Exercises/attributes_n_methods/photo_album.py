class PhotoAlbum:

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = self.create_matrix(pages)

    def __repr__(self):
        page_sep = '-'*11
        result = ""
        for p in self.photos:
            pictures = "[] " * len(p)
            result += f"{page_sep}\n"
            result += f"{pictures}\n"
        result += f"{page_sep}\n"

        return result

    @staticmethod
    def create_matrix(rows_cols_count):
        matrix = []
        for r in range(rows_cols_count):
            matrix.append([])
        return matrix

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = photos_count // 4
        return cls(pages)

    def check_for_available_slots(self):
        matrix_len = len(self.photos)
        for r in range(matrix_len):
            col_len = len(self.photos[r])
            if col_len < 4:
                return r
        return False

    def add_photo(self, label: str):
        check_result = self.check_for_available_slots()
        if check_result is False:
            return "No more free spots"
        row = check_result
        self.photos[row].append(label)
        col = len(self.photos[row])
        return f"{label} photo added successfully on page {row + 1}" \
               f" slot {col}"

    def display(self):
        return self.__repr__()


# album = PhotoAlbum(2)
#
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
#
# print(album.display())
