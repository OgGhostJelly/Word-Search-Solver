def insert(trie: dict, string: str) -> None:
    for char in string:
        trie = trie.setdefault(char, {})
    
    trie["end"] = True


def list_to_trie(ls) -> dict:
    trie = {}

    for string in ls:
        insert(trie, string)
    
    return trie


if __name__ == "__main__":
    ls = [ "Hello", "Hey", "Hi" ]
    print(f'Using example list "{ls}"')
    print("Output =>", list_to_trie(ls))