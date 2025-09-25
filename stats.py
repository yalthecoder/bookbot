def get_num_words(book):
    with open(book) as f:
        return len(f.read().split())
def get_num_chars(booke):
    # i know there is a way easier way to do this but i couldn't care less 
    with open(booke) as bookthing:
        book = bookthing.read()
        thingy={
            "a": book.lower().count('a'),
            "b": book.lower().count('b'),
            "c": book.lower().count('c'),
            "d": book.lower().count('d'),
            "e": book.lower().count('e'),
            "f": book.lower().count('f'),
            "g": book.lower().count('g'),
            "h": book.lower().count('h'),
            "i": book.lower().count('i'),
            "j": book.lower().count('j'),
            "k": book.lower().count('k'),
            "l": book.lower().count('l'),
            "m": book.lower().count('m'),
            "n": book.lower().count('n'),
            "o": book.lower().count('o'),
            "p": book.lower().count('p'),
            "q": book.lower().count('q'),
            "r": book.lower().count('r'),
            "s": book.lower().count('s'),
            "t": book.lower().count('t'),
            "u": book.lower().count('u'),
            "v": book.lower().count('v'),
            "w": book.lower().count('w'),
            "x": book.lower().count('x'),
            "y": book.lower().count('y'),
            "z": book.lower().count('z'),
        } 
        return thingy