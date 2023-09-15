from collections import deque

queue = deque(['Eric', 'John', 'Michael'])

# добавяме Terry, като използваме команда append. Всичко добавено отива на опашката отзад
queue.append('Terry')
print(queue)
# резултат - deque(['Eric', 'John', 'Michael', 'Terry'])

# изтриваме първия на опашката - Eric, с командата popleft
name = queue.popleft()
print(name)
print(queue)


