# _*_ coding: utf-8 _*_

import os


class Trie(object):
    def __init__(self):
        self.root = {}
        self.end_of_word = '#'
        self.category = ''

    def insert(self, word, cate):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word
        node[self.category] = cate

 
    def search(self, word):
        node = self.root

        for char in word:
            if char not in node:
                return False
            node = node[char]

        if '#' in node.keys():
            return node[self.category]
        else:
            print('no such term')
            return False

    def remove(self, word):
        node = self.root
        node_list = []
        keys_list = []
        node_list.append(node)

        for c in word:
            #last_node = current_node
            node = node[c]
            node_list.append(node)
            keys_list.append(len(node.keys()))
            if '#' in node.keys():
                min_pos = keys_list.index(1)

                for pos, val in enumerate(keys_list):
                    if val == 1:
                        max_pos = pos
                if len(word) - 2 == max_pos:
                    node_list[min_pos].pop(word[min_pos])
                else:
                    node_list[len(word) - 1].pop(word[-1])


    def modify(self, source, target, category):
        self.remove(source)
        self.insert(target, category)

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True


def tranverseFolder(path):
    for (root, dirs, files) in os.walk(path):
        print(root, dirs, files)
    fs = map(lambda f: os.path.join(root, f), files)
    return fs


def readFile(file):
    data = []
    with open(file, 'r') as f:
        for line in f.readlines():
            terms = line.replace('\n', '').split(' ')[1:]
            if len(terms) > 1:
                data.append(terms)
    return data


if __name__ == '__main__':
    trie = Trie()

    data = [['人', '人民', '众人', '角色'], ['蝴蝶', '花大姐'],
            ['心前区疼痛', '心前区痛', '心前区绞痛', '心前区疼痛'],
            ['乙型病毒性肝炎', '乙肝', '乙型病毒性肝炎', '慢性乙型病毒性肝炎']]

    data = [['hello', 'hi', 'good morning', 'happen', 'happy'], ['time', 'clock', 'watch'], ['animal', 'cat', 'mouse']]
    for d in data:
        for t in d:
            t_k = d[0]
            trie.insert(t, t_k)

    print(trie.search('good morning'))
    print(trie.search('clock'))
    trie.remove('happ')
    trie.remove(('happy'))
    trie.remove('mouse')
    print(trie.search('happy'))
    print(trie.search('mouse'))
    print(trie.search('good morning'))
    print(trie.search('clock'))
    print(trie.search('time'))
    print(trie.search('happ'))
    print(trie.search('apple'))
    print(trie.search('c'))