def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badges = [ badge_maker(name) for name in names]
    return badges

def assign_rooms(names):
    i = 1
    rooms = []
    while i < 9:
        rooms.append(f"Hello, {names[i-1]}! You'll be assigned to room {i}!")
        i +=1
    return rooms

def printer(names):
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)
    i = 0
    for badge in badges:
        print(badge)
    for room in rooms:
        print(room)
    return None
