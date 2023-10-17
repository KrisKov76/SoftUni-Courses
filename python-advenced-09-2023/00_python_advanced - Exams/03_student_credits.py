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

    # трябваше да съобразя, че може да си направя дикт само с една стойност - тази, по която ще сортирам
    sorted_list = sorted(collection.items(), key=lambda a: -a[1])

    for subject, credits in sorted_list:
        result += f"{subject} - {credits:.1f}\n"

    return result

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)






