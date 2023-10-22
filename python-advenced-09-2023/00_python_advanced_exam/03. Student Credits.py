def students_credits(*args):
    collection = {}
    total_credits = 0
    result = ''

    for arg in args:
        parts = arg.split('-')
        subject, *numbers = parts

        avg_res = (float(numbers[2])/float(numbers[1])) * float(numbers[0])
        collection[subject] = avg_res
        total_credits += avg_res


    if total_credits >= 240:
        result += f"Diyan gets a diploma with {total_credits:.1f} credits.\n"
    else:
        result += f"Diyan needs {(240 - total_credits):.1f} credits more for a diploma.\n"

    sorted_list = sorted(collection.items(), key=lambda a: -a[1])

    for subject, credits in sorted_list:
        result += f"{subject} - {credits:.1f}\n"

    return result