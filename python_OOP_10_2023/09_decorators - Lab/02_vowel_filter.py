def vowel_filter(function):

    def wrapper():
        vowels = [char for char in function() if char.lower() in ['a', 'o', 'i', 'u', 'e', 'y']]
        return vowels
    return wrapper

@vowel_filter 
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
