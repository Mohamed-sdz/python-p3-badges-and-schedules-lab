def badge_maker(name):
    return "Hello, my name is {}.".format(name)

def batch_badge_creator(speakers):
    return [badge_maker(name) for name in speakers]

def assign_rooms(speakers):
    room_assignments = []
    for idx, name in enumerate(speakers, start=1):
        room_assignments.append("Hello, {}! You'll be assigned to room {}!".format(name, idx))
    return room_assignments

def printer(speakers):
    badges = batch_badge_creator(speakers)
    room_assignments = assign_rooms(speakers)
    
    for badge in badges:
        print(badge)
    for assignment in room_assignments:
        print(assignment)

 