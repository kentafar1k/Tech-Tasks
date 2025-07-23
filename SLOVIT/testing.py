def longest_palindrome(s: str) -> int:
    count_letters = {}
    for char in s:
        count_letters[char] = count_letters.get(char, 0) + 1

    for value in count_letters.values():
        if
    return count_letters

print(longest_palindrome("abccccdd"))