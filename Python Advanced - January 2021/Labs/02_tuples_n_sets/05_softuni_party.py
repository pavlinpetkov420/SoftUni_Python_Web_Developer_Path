def input_lines(count):
    reservations_guests = set()
    for _ in range(count):
        reservations_guests.add(input())

    END_CMD = 'END'
    guest_arrived = set()
    while True:
        cmd = input()
        if cmd == END_CMD:
            break
        guest_arrived.add(cmd)

    return reservations_guests, guest_arrived


def is_vip(guest):
    return guest[0].isdigit()


def separate_into_vip_n_regular(guests_not_arrived):
    vip, regular = [], []

    for guest in guests_not_arrived:
        if is_vip(guest):
            vip.append(guest)
        else:
            regular.append(guest)

    return vip, regular


def print_result(guests_not_arrived):
    print(len(guests_not_arrived))
    (vip_guests, regular_guests) = separate_into_vip_n_regular(guests_not_arrived)

    for guest in sorted(vip_guests):
        print(guest)

    for guest in sorted(regular_guests):
        print(guest)


reservations, guests_arrived = input_lines(int(input()))
#
# for guest in guests_arrived:
#     reservations.remove(guest)

guests_not_arrived = reservations.difference(guests_arrived)

print_result(guests_not_arrived)
