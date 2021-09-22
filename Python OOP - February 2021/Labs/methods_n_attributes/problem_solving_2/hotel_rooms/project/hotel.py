from project.room import Room


class Hotel:

	def __init__(self, name: str):
		self.name = name
		self.rooms = []
		self.guests = 0

	@classmethod
	def from_stars(cls, stars_count):
		name = f'{stars_count} start Hotel'
		return Hotel(name)

	def find_room_by_number(self, number):
		for room in self.rooms:
			if room.number == number:
				return room

	def add_room(self, room):
		self.rooms.append(room)

	def take_room(self, room_nuber, people):
		room = self.find_room_by_number(room_nuber)
		if room:
			room.take_room(people)
			self.guests += people

	def free_room(self, room_number):
		room = self.find_room_by_number(room_number)
		if room:
			self.guests -= room.guests
			room.free_room()

	def print_status(self):
		free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
		taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]

		return f'Hotel {self.name} has {self.guests} total guests\n' \
			f'Free rooms: {", ".join(free_rooms)} \n' \
			f'Taken rooms: {", ".join(taken_rooms)}'



