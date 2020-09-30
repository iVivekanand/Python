def regex_checker(s, p):
    str_len = len(s)
    pattern_len = len(p.replace('*', ''))
    str_traverse = 0
    char_before_star = ''
    last_checked = False

    for index, char in enumerate(p):
        if str_traverse == str_len:
            if char == '*':
                continue
            elif char == '.' and not last_checked:
                if s[str_len - 1] == char_before_star:
                    last_checked = True
                    continue
                else:
                    return False
            else:
                return False
        if char == '.':
            str_traverse += 1
            continue
        if char == '*':
            if index > 0:
                char_before_star = p[index-1] if  p[index-1] != '*' else char_before_star
                while str_traverse < str_len and s[str_traverse] == s[str_traverse-1]:
                    str_traverse += 1
            else:
                continue
        elif char == s[str_traverse]:
            str_traverse += 1
        else:
            return False

    if str_traverse == str_len:
        return True

    return False


print(regex_checker('aasdfabbasdfasdfwaa', 'a*.'))