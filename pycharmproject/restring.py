def is_palindrome(text):
    processed_text = "".join(text.split()).lower()
    return processed_text == processed_text[::-1]

print(is_palindrome("потоп"))