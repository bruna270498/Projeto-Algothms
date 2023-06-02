def quick_sort(string):
    if len(string) <= 1:
        return string
    position = string[0]
    smaller = [i for i in string if i < position]
    bigger = [i for i in string if i > position]
    equal = [i for i in string if i == position]
    return (
         quick_sort(''.join(smaller))
         + ''.join(equal)
         + quick_sort(''.join(bigger))
            )


def is_anagram(first_string, second_string):
    first_lower = first_string.lower()
    second_lower = second_string.lower()
    string_first = quick_sort(first_lower)
    string_second = quick_sort(second_lower)
    if first_string == '' or second_string == '':
        return (string_first, string_second, False)
    and_anagram = string_first == string_second
    return (string_first, string_second, and_anagram)
