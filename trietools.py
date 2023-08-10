# Inserts a string into a trie.

def insert(trie: dict, string: str) -> None:
    for char in string:
        trie = trie.setdefault(char, {})
    
    trie["end"] = True


# Converts a List[str] to a trie.

def list_to_trie(ls) -> dict:
    trie = {}

    for string in ls:
        insert(trie, string)
    
    return trie


# Returns True if the trie has the key else False

def has(trie: dict, key):
    for char in key:
        if not char in trie:
            return False

        trie = trie[char]
    
    return True


# Returns the first string that is a prefix of key.

def match(trie: dict, key):
    string = ""

    for char in key:
        if not char in trie:
            return

        string += char
        trie = trie[char]
        
        if "end" in trie:
            return string
    
    return


if __name__ == "__main__":
    ls = [ "Hi", "Hey", "Heya!" ]
    print(f'Using example list "{ls}"')
    print("Output =>", list_to_trie(ls))