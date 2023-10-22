from collections import deque

tools = deque(int(x) for x in input().split())
substances = deque(int(x) for x in input().split())
challenges = deque(int(x) for x in input().split())

while tools and substances:
    tool = tools.popleft()
    substance = substances[-1]

    result = tool * substance

    if result in challenges:
        challenges.remove(result)
        substances.pop()
    else:
        tool += 1
        tools.append(tool)
        substance -= 1
        if substance > 0:
            substances[-1] = substance
        else:
            substances.pop()

if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
else:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print(f"Tools: {', '.join(map(str, tools))}")

if substances:
    print(f"Substances: {', '.join(map(str, substances))}")

if challenges:
    print(f"Challenges: {', '.join(map(str, challenges))}")