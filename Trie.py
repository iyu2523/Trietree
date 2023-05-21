class Trie:
    class Node:
        def __init__(self, letter) -> None:
            self.letter = letter
            self.next = dict()

    def  __init__(self) -> None:
        self.root_node = self.Node(" ")

    def insert(self, item):
        if type(item) != str:
            item = str(item)
        node = self.root_node
        for letter in item:
            if letter in node.next.keys():
                node = node.next[letter]
            else:
                next_node = self.Node(letter)
                node.next[letter] = next_node
                node = next_node

    def search(self, item):
        node = self.root_node
        for letter in item:
            if letter in node.next.keys():
                node = node.next[letter]
            else:
                return False
        return True

if __name__ == "__main__":
    trie = Trie()
    trie.insert("test")
    trie.insert("trie")
    print(trie.search("test"))
    print(trie.search("hoge"))
