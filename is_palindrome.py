def remove_spaces(old_string):
    new_str = ""
    for char in old_string:
        if not char == " ":
            new_str += char
    return new_str


def texto_reverse(text):
    new_text = ""
    for char in text:
        new_text = char + new_text
    return new_text


def is_palindrome(text):
    text_without_spaces = remove_spaces(text.lower())
    text_inverted = texto_reverse(text_without_spaces)
    return text_without_spaces == text_inverted


print("Abba", is_palindrome("abba"))
print("Hola Mundo", is_palindrome("Hola Mundo"))