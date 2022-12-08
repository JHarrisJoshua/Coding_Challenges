from collections import deque
from math import inf
from time_this import time_this


class TreeNode(object):
    def __init__(self, name, file_type, parent=None, size=0):
        self.name = name
        self.file_type = file_type
        self.size = size
        self.parent = parent
        self.children = {}

    def __repr__(self):
        keys = ['Name', 'File Type', 'Size', 'Parent', 'Children']
        values = [self.name, self.file_type, self.size,
                  self.parent.name if self.parent else self.parent,
                  {key for key in self.children}]
        output = dict(zip(keys, values))
        return output.__repr__()


class ElvenDevice(object):
    def __init__(self):
        self.root = TreeNode('/', 'dir')
        self.curr = self.root
        self.space_avail = 70000000

    def __repr__(self):
        return self.root.__repr__()

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
            node = TreeNode(name, file_type, self.curr, size)
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

    def get_small_dirs_bfs(self, root: TreeNode) -> int:
        queue = deque([root])
        total_size = 0
        while queue:
            curr: TreeNode = queue.popleft()
            if curr.file_type == 'dir' and curr.size < 100000:
                total_size += curr.size
            for child in curr.children:
                queue.append(curr.children[child])
        return total_size

    def get_small_dirs_dfs(self, root):
        stack = [root]
        total_size = 0
        while stack:
            curr: TreeNode = stack.pop()
            if curr.file_type == 'dir' and curr.size < 100000:
                total_size += curr.size
            for child in curr.children:
                stack.append(curr.children[child])
        return total_size

    def dir_to_delete_bfs(self, root: TreeNode, space_needed):
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

    def dir_to_delete_dfs(self, root: TreeNode, space_needed):
        space_to_free = space_needed - (self.space_avail - root.size)
        dir_to_remove, min_file_size = None, inf

        stack = [root]
        while stack:
            curr: TreeNode = stack.pop()
            if space_to_free <= curr.size < min_file_size:
                dir_to_remove, min_file_size = curr.name, curr.size
            for child in curr.children:
                if curr.children[child].file_type != 'dir':
                    continue
                stack.append(curr.children[child])
        return dir_to_remove, min_file_size


def main(file_name):
    device = ElvenDevice()
    device.make_file_tree(file_name)
    device.index_size(device.root)
    print(f'File System Root: {device}')
    print(f'Problem 1 Answer BFS: {device.get_small_dirs_bfs(device.root)}')
    print(f'Problem 2 Answer BFS: {device.dir_to_delete_bfs(device.root, 30000000)}')
    print(f'Problem 1 Answer DFS: {device.get_small_dirs_dfs(device.root)}')
    print(f'Problem 2 Answer DFS: {device.dir_to_delete_dfs(device.root, 30000000)}')

    # Time Trials
    print(f'P1 Answer BFS trial: {time_trial(device.get_small_dirs_bfs,device)}')
    print(f'P2 Answer BFS trial: {time_trial(device.dir_to_delete_bfs,device, 30000000)}')
    print(f'P1 Answer DFS trial: {time_trial(device.get_small_dirs_dfs,device)}')
    print(f'P2 Answer DFS trial: {time_trial(device.dir_to_delete_dfs,device,30000000)}')


@time_this
def time_trial(func, obj: ElvenDevice, space=None):
    if space:
        func(obj.root, space)
    else:
        func(obj.root)


if __name__ == '__main__':
    main("AOC22_D07_inp.txt")
