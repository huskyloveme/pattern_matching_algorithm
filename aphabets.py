class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

def build_trie(words):
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    return root

def aho_corasick(text, words):
    root = build_trie(words)
    results = []
    node = root

    for i in range(len(text)):
        char = text[i]
        while char not in node.children and node != root:
            node = node.failure_link

        if char in node.children:
            node = node.children[char]
        else:
            node = root

        if node.is_end_of_word:
            results.append((i - len(words) + 1, i))

    return results

# Bây giờ hãy xây dựng liên kết thất bại (failure link) cho các nút của cây Trie.
def build_failure_links(root):
    queue = [root]
    root.failure_link = root  # Điểm bắt đầu

    while queue:
        current_node = queue.pop(0)
        for char, child in current_node.children.items():
            queue.append(child)
            failure_node = current_node.failure_link

            while char not in failure_node.children and failure_node != root:
                failure_node = failure_node.failure_link

            if char in failure_node.children:
                child.failure_link = failure_node.children[char]
            else:
                child.failure_link = root

text = "The quick brown fox jumped over the lazy dog."
words = ["quick", "fox", "dog", "jumped"]

root = build_trie(words)
build_failure_links(root)
results = aho_corasick(text, words)

print(results)
