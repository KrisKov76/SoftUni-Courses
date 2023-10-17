def gather_credits(credits, *args):
    collection = {}
    current_credits = 0

    for arg in args:
        course_name = arg[0]
        course_credits = int(arg[1])

        if current_credits >= credits:
            break

        if course_name in collection:
            continue

        if course_name not in collection:
            collection[course_name] = 0
        collection[course_name] += course_credits
        current_credits += course_credits

    result = ''
    keys = sorted([key for key in collection])

    if current_credits >= credits:
        result += f"Enrollment finished! Maximum credits: {current_credits}.\n"
        result += f"Courses: {', '.join(keys)}"
    else:
        result += f"You need to enroll in more courses! You have to gather {credits - current_credits} credits more."

    return result

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))


