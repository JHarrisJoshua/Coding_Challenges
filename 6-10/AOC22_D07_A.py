from collections import deque
from math import inf


class TreeNode(object):
    def __init__(self, name, file_type, parent=None, size=0):
        self.parent = parent
        self.children = {}
        self.name = name
        self.size = size
        self.file_type = file_type


class ElvenDevice(object):
    def __init__(self):
        self.root = TreeNode('/', 'dir')
        self.curr = self.root
        self.space_avail = 70000000

    def make_file_tree(self, file_name):
        with open(file_name, 'r') as infile:
            queue = deque([line.strip().split(' ') for line in infile])
            while queue:
                if queue[0][0] == '$' and queue[0][1] == 'cd':
                    self.change_dir(queue.popleft()[2])
                if queue[0][0] == '$' and queue[0][1] == 'ls':
                    command, stack = queue.popleft(), []
                    while queue and queue[0][0] != '$':
                        stack.append(queue.popleft())
                    self.populate_dir(stack)

    def populate_dir(self, stack):
        while stack:
            size, name = stack.pop()
            (size,file_type) = (0,'dir') if size=='dir' else (int(size), 'file')
            node = TreeNode(name,file_type,self.curr, size)
            self.curr.children[name] = node

    def change_dir(self, go_to):
        if go_to == '/':
            self.curr = self.root
        elif go_to == '..':
            self.curr = self.curr.parent
        else:
            for child in self.curr.children:
                if child == go_to:
                    self.curr = self.curr.children[child]

    def index_size(self, node: TreeNode):
        if node.file_type == 'file':
            return node.size
        size = 0
        for child in node.children:
            size += self.index_size(node.children[child])
        node.size = size
        return size

    def get_small_dirs(self, root):
        queue = deque([root])
        total_size = 0
        while queue:
            curr: TreeNode = queue.popleft()
            if curr.file_type == 'dir' and curr.size < 100000:
                total_size += curr.size
            for child in curr.children:
                queue.append(curr.children[child])
        return total_size

    def dir_to_delete(self, root: TreeNode, space_needed):
        space_to_free = space_needed - (self.space_avail - root.size)
        dir_to_remove, min_file_size = None, inf

        queue = deque([root])
        while queue:
            curr: TreeNode = queue.popleft()
            if space_to_free <= curr.size < min_file_size:
                dir_to_remove, min_file_size = curr.name, curr.size
            for child in curr.children:
                if curr.children[child].file_type != 'dir':
                    continue
                queue.append(curr.children[child])
        return dir_to_remove, min_file_size


def main(file_name):
    d = ElvenDevice()
    d.make_file_tree(file_name)
    d.index_size(d.root)
    print(d.get_small_dirs(d.root))
    print(d.dir_to_delete(d.root, 30000000))


if __name__ == '__main__':
    main("AOC22_D07_inp.txt")
