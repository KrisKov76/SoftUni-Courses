import os

while True:
    line = input()
    if line == 'End':
        break

    command, file_name, *other = line.split('-')

    if command == 'Create':
        open(file_name, 'w').close() # да не забравя да затворя файла!
    elif command == 'Add':
        with open(file_name, 'a') as f: # работим с with open ... as f:
            f.write(other[0] + '\n')
    elif command == 'Replace':
        try:
            with open(file_name) as f:
                content = f.read() # прочитаме съдържанието на файла и го пращаме в content
                with open(file_name, 'w') as f: # отварям файла за писане
                    content = content.replace(other[0], other[1]) # замествам съдържанието
                    f.write(content) # презаписвам новото съдържание във файла
        except FileNotFoundError:
            print("An error occurred")
    elif command == 'Delete':
        if os.path.exists(file_name): # използваме библиотека os, за да проверим дали файлът съществува и да го премахнем
            os.remove(file_name)
        else:
            print("An error occurred")



