from project.room import Room


class Hotel:

    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @staticmethod
    def find_room(rooms, room_number):
        room = list(filter(lambda room: room.number == room_number, rooms))[0]
        return room

    @classmethod
    def from_stars(cls, stars_count):
        name = f"{stars_count} stars Hotel"
        return cls(name)

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        result = self.find_room(self.rooms, room_number).take_room(people)

        if result:
            return result
        self.guests += people

    def free_room(self):
        room = self.find_room(self.rooms, room_number)
        guest_to_remove = room.guests
        result = room.free_room()

        if result:
            return result
        self.guests -= guest_to_remove

    def print_status(self):
        free_room_numbers = [str(room) for room in self.rooms if not room.is_taken]
        taken_room_numbers = [str(room) for room in self.rooms if room.is_taken]
        print(f'Hotel {self.name} has {self.guests} total guests\n' 
              f'Free rooms: {", ".join(free_room_numbers)}\n' 
              f'Taken rooms: {", ".join(taken_room_numbers)}')
