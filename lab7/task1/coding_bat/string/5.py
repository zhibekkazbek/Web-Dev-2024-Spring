def extra_end(str):
    if len(str) < 3:
        return str
    return str[3:] * 3

print(extra_end("Hello"))