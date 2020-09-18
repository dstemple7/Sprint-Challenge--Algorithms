'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    s = 0
    f = 1
    w = word
    target = "th"
    max = len(word)

    if max < 2:
        return 0
    if w[s:s+2] == target:
        return count_th(w[f:])+1
    else:
        return count_th(w[f:])
