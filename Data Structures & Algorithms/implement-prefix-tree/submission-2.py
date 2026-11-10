class Node:
    def __init__(self):
        self.sufx: list["Node | None"] = [None] * 26
        self.suffixCount = 0

    def __getitem__(self, char: str) -> "Node | None":
        return self.sufx[ord(char) - ord('a')]

    def __setitem__(self, char: str, node: "Node") -> None:
        self.sufx[ord(char) - ord('a')] = node
        self.suffixCount += 1

class PrefixTree:
    def __init__(self):
        # just initialize a Node, and some set of words
        self.sentinel = Node()
        self.words = set()

    def insert(self, word: str) -> None:
        cNode = self.sentinel
        self.words.add(word)

        # insert each char into each trie level as needed
        for char in word:
            if cNode[char] is None:
                cNode[char] = Node()

            cNode = cNode[char]

    def search(self, word: str) -> bool:
        return True if word in self.words else False

    def startsWith(self, prefix: str) -> bool:
        cNode = self.sentinel
        if prefix in self.words:
            return True

        for char in prefix:
            if cNode[char] is None:
                return False
            cNode = cNode[char]

        return cNode.suffixCount > 0
# for each character in a 