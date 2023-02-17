def replaceSpace(s):
    return ''.join(c if c!=' ' else '%20' for c in s)

print(replaceSpace('dsasd sd'))