import copy

def eliminate_comments(lines):
    sep = '//'
    result = copy.copy(lines)

    for i, line in enumerate(lines):
        if sep == line[0:2]:
            result.remove(line)

    for i, line in enumerate(result):
        if sep in line:
            temp = line.split(sep)
            temp = temp[0].strip()
            result[i] = temp
  
    return result

def eliminate_newlines(lines):
    sep = '\n'
    result = copy.copy(lines)

    for i, line in enumerate(lines):
        if sep == line:
            result.remove(line)

    for i, line in enumerate(result):
        result[i] = line.strip()

    return result