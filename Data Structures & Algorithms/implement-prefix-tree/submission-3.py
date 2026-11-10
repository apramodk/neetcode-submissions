class Node:
    def __init__(self):
        self.sufx: list["Node | None"] = [None] * 26
        self.suffixCount = 0
        self.isEnd = False

    def __getitem__(self, char: str) -> "Node | None":
        return self.sufx[ord(char) - ord('a')]

    def __setitem__(self, char: str, node: "Node") -> None:
        self.sufx[ord(char) - ord('a')] = node
        self.suffixCount += 1

class PrefixTree:
    def __init__(self):
        # just initialize a Node, and some set of words
        self.sentinel = Node()

    def insert(self, word: str) -> None:
        cNode = self.sentinel

        # insert each char into each trie level as needed
        for char in word:
            if cNode[char] is None:
                cNode[char] = Node()

            cNode = cNode[char]
        cNode.isEnd = True

    def search(self, word: str) -> bool:
        cNode = self.sentinel

        for char in word:
            if cNode[char] is None:
                return False
            cNode = cNode[char]
        return cNode.isEnd

    def startsWith(self, prefix: str) -> bool:
        cNode = self.sentinel

        for char in prefix:
            if cNode[char] is None:
                return False
            cNode = cNode[char]

        return cNode.isEnd or cNode.suffixCount > 0
# for each character in a 