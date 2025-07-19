def curtail_str(letters: str) -> str:
    if not letters:
        return letters

    result = []
    current_char = letters[0]
    count = 1

    for char in letters[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(current_char + (str(count) if count > 1 else ''))
            current_char = char
            count = 1
    result.append(current_char + (str(count) if count > 1 else ''))

    return ''.join(result)


print("Hello Tochka")

assert curtail_str('') == ''
assert curtail_str("A") == "A"
assert curtail_str('ABC') == 'ABC'
assert curtail_str('AAA') == 'A3'
assert curtail_str('AAABBXYZDDDDA') == 'A3B2XYZD4A'
assert curtail_str('ABCABCABCCCCC') == 'ABCABCABC5'
print('done')