def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False
    first_lower = first_string.lower()
    second_lower = second_string.lower()
    first = list(first_lower)
    second = list(second_lower)
    half_first = first[len(first) // 2]
    half_second = second[len(second) // 2]
    smaller = [i for i in first if i < half_first]
    bigger = [i for i in first if i > half_first]
    equal = [i for i in first if i == half_first]
    smallerr = [i for i in first if i < half_second]
    biggerr = [i for i in first if i > half_second]
    equall = [i for i in first if i == half_second]
    string_first = ''.join(smaller + equal + bigger)
    string_second = ''.join(smallerr + equall + biggerr)
    and_anagram = string_first == string_second
    return (string_first, string_second, and_anagram)
