def str_to_trie(string, d = None, length = None):
    if length is None:
        length = len(string)
    
    if length <= 0:
        return True
    
    if d is None:
        d = {}
    
    char = string[:1]
    d[char] = str_to_trie(string[1:], d[char] if char in d else None, length-1)
    return d


def strlist_to_trie(ls):
    d = {}
    
    for string in ls:
        str_to_trie(string, d)
    
    return d


if __name__ == "__main__":
    ls = [ "Hello", "Hey", "Hi" ]
    print(f'Using example list "{ls}"')
    print("Output =>", strlist_to_trie(ls))