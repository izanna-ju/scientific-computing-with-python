def add_time(start, duration, *args):
    [T, meridiem] = start.split(" ")
    [H, M] = T.split(":")
    [DH, DM] = duration.split(":")

    total_hours = int(H) + int(DH)
    total_minutes = int(M) + int(DM)

    day_of_week = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"]

    future_day = 0

    if total_minutes > 60:
        total_minutes -= 60
        total_hours += 1
    if total_hours >= 12:
        (t, r) = divmod(total_hours, 12)
        total_hours = r if r else total_hours
        # Calculate total hours in multiples of 12 if total_hours is 24, 36, 48 etc.
        if total_hours > 12:
            total_hours = total_hours - ((t - 1) * 12)

        if t > 0:
            if meridiem == "PM":
                future_day = ((t - 1) // 2) + 1
            else:
                future_day = t // 2

        if t > 0 and t % 2 != 0:
            meridiem = "AM" if meridiem == "PM" else "PM"
    new_time = str(total_hours) + ":" + str(total_minutes).zfill(
        2) + " " + meridiem

    if args:
        day = args[0].title()
        if future_day > 0:
            index = day_of_week.index(day)
            index += future_day % 7
            if index > 6:
                index -= 7
            day = day_of_week[index]
            
        new_time += f", {day}"
            
    if future_day == 1:
        new_time += " (next day)"
    elif future_day > 1:
        new_time += f" ({future_day} days later)"

    return new_time

