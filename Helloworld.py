
def match(filename, pattern):
    if pattern == '*' or pattern == '**':
        return True

    if len(filename) < len(pattern):
        return False

    if filename == pattern:
        return True

    if unique(pattern):
        return True

    if pattern == '*.*' and '.' in filename:
        return True

    if '*' in pattern and '?' in pattern:
        while True:
            for index, letter in enumerate(pattern):
                if letter != '?' and letter !='*':
                    if letter != filename[index]:
                        return False
                else:
                    num = len(pattern[index + 1:])
                    if letter == '?':
                        break
                    else:
                        if '*' in pattern[index + 1:]:
                            idx = index
                            break
                        else:
                            pattern = pattern[index + 1:]
                            filename = filename[-num:]

                            for index,letter in enumerate(pattern):
                                if letter != '?':
                                    if letter != filename[index]:
                                        return False
                            return True
            pattern = pattern[index + 1:]
            filename = filename[-num:]

    if '*' in pattern:
        while True:
            for index, letter in enumerate(pattern):
                if letter != '*':
                    if letter != filename[index]:
                        return False
                else:
                    num = len(pattern[index + 1:])
                    if '*' in pattern[index + 1:]:
                        idx = index
                        break
                    else:
                        if num == 0:
                            return True
                        if filename[-num:] == pattern[index+1:]:
                            return True
                        else:
                            return False
            pattern = pattern[index+1:]
            filename = filename[-num:]

    if '?' in pattern:
        for index, letter in enumerate(pattern):
            if letter != '?':
                if letter != filename[index]:
                    return False
        return True

    for index, letter in enumerate(pattern):
        if letter == '.':
            idx = index
            break
    if pattern[:idx] == filename[:idx] and pattern[idx+1:] == filename[idx+1:]:
        return True
    else:
        return False


def unique(s):
    n = len(s)
    for i in range(1, n):
        if s[i] != '?' or s[i] != '*':
            return False
    return True

print(match('file.txt', '**?t'))
print(match('log12.txt', 'log?.txt'))
print(match('log12.txt', 'log??.tx?'))
print(match("my.txt","*.*x*"))
print(match("l.txt","???*"))
print(match("name.txt","name.exe"))
print(match("apache1.log","*.*"))