class PhotoAlbum:

	def __init__(self, pages: int):
		self.pages = pages
		self.photos = PhotoAlbum.create_matrix(self.pages)

	@staticmethod
	def create_matrix(sublists_count):

		matrix = []
		for r in range(sublists_count):
			matrix.append([])

		return matrix

	@classmethod
	def from_photos_count(cls, photos_count: int):
		pages_count = photos_count // 4
		return PhotoAlbum(pages_count)

	def search_next_possible_page(self):
		for page in range(len(self.photos)):
			if len(self.photos[page]) == 4:
				continue
			elif len(self.photos[page]) < 4:
				return page

		return False

	def add_photo(self, label: str):
		next_possible_position = self.search_next_possible_page()
		if type(next_possible_position) == bool:
			return 'No more free spots'
		self.photos[next_possible_position].append(label)
		return f'{label} photo added successfully onpage {next_possible_position + 1} ' \
			f'slot {len(self.photos[next_possible_position])}'


	def display(self):
		visualization = ''
		for page in self.photos:
			visualization += f'{"-" * 11}\n'
			if len(page) == 0:
				visualization += f'{"-" * 11}\n'
				continue
			visualization += f'{len(page) * "[] "}\n'

		visualization += f'{"-" * 11}'
		return visualization






album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())