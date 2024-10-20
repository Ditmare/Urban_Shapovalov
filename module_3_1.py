calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    length = len(string)
    upper_ = string.upper()
    lower_ = string.lower()
    return length, upper_, lower_

def is_contains(string, list_):
    count_calls()
    lower_string = string.lower()
    lower_list = [string.lower() for string in list_]
    return lower_string in lower_list


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)