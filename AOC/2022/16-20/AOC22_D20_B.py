class ListNode(object):
    def __init__(self, val=0, nxt=None, prev=None):
        self.val, self.nxt, self.prev = val, nxt, prev


class LinkedList:
    def __init__(self, file_name, key):
        self.head, self.zero = None, None
        self.order, self._len = [], 0
        self.create_list(file_name, key)

    def __len__(self):
        return self._len

    def create_list(self, file_name, key):
        with open(file_name, 'r') as infile:
            for line in infile:
                new_node = ListNode(int(line.strip())*key)
                self.order.append(new_node)
                self._len += 1
                if self.head is None:
                    self.head, self.zero = new_node, new_node
                else:
                    new_node.prev = curr
                    curr.nxt = new_node
                    self.zero = self.zero if self.zero.val == 0 else new_node
                curr = new_node
            new_node.nxt = self.head
            self.head.prev = new_node

    def mixing(self, times):
        for _ in range(times):
            for curr in self.order:
                steps, move = curr.val, abs(curr.val) % (len(self) - 1)
                if 0 in [steps, move]:
                    continue

                curr_prev, curr_next = curr.prev, curr.nxt
                curr_prev.nxt, curr_next.prev = curr_next, curr_prev

                forward, new_prev = 1 if steps > 0 else 0, curr
                for _ in range(move):
                    new_prev = new_prev.nxt if forward else new_prev.prev
                if not forward:
                    new_prev = new_prev.prev

                curr.nxt, curr.prev = new_prev.nxt, new_prev
                new_prev.nxt, curr.nxt.prev = curr, curr

    def get_coords(self, idx1, idx2, idx3):
        curr, res, i = self.zero, [], 0
        while i <= idx3:
            curr, i = curr.nxt, i+1
            if i in [idx1, idx2, idx3]:
                res.append(curr.val)
        return res


if __name__ == '__main__':
    ll = LinkedList("AOC22_D20_inp.txt", 811589153)
    ll.mixing(10)
    print('Coords:')
    result = ll.get_coords(1000, 2000, 3000)
    print(result, "Sum: ", sum(result))
