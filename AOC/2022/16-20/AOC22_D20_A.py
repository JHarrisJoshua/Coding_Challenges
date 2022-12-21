from collections import deque


class ListNode(object):
    def __init__(self, val=0, nxt=None, prev=None):
        self.val = val
        self.nxt = nxt
        self.prev = prev


class LinkedList:
    def __init__(self, file_name):
        self.head: ListNode = None
        self.tail = None
        self._len = 0
        self.create_list(file_name)

    def __len__(self):
        return self._len

    def create_list(self, file_name):
        with open(file_name, 'r') as infile:
            for line in infile:
                new_node = ListNode(int(line.strip()))
                self._len += 1
                if self.head is None:
                    self.head = new_node
                else:
                    new_node.prev = curr
                    curr.nxt = new_node
                curr = new_node
            self.tail = new_node
            self.tail.nxt = self.head
            self.head.prev = self.tail

    def mixing(self):
        orig_list = deque([self.head])
        curr = self.head.nxt
        while curr is not self.head:
            orig_list.append(curr)
            curr=curr.nxt

        print(self._len, len(orig_list))
        while orig_list:
            curr: ListNode = orig_list.popleft()
            if (steps := curr.val) == 0:
                continue
            curr_prev, curr_next = curr.prev, curr.nxt
            curr_prev.nxt, curr_next.prev = curr_next, curr_prev

            forward = 1 if steps > 0 else 0
            new_prev = curr
            for _ in range(abs(steps)):
                new_prev = new_prev.nxt if forward else new_prev.prev
            if not forward:
                new_prev = new_prev.prev
            if not forward and new_prev is curr:
                new_prev = new_prev.prev

            curr.nxt, curr.prev = new_prev.nxt, new_prev
            new_prev.nxt, curr.nxt.prev = curr, curr

        # print('test')
        # curr = self.head
        # print(curr.val)
        # curr = curr.nxt
        # while curr != self.head:
        #     print(curr.val)
        #     curr = curr.nxt

    def get_coords(self, idx1, idx2, idx3):
        curr, result = self.head, []
        while curr.val != 0:
            curr = curr.nxt
        i = 0
        while i <= idx3:
            curr = curr.nxt
            i += 1
            if i == idx1:
                result.append(curr.val)
            if i == idx2:
                result.append(curr.val)
            if i == idx3:
                result.append(curr.val)
        return result


if __name__ == '__main__':
    ll = LinkedList("AOC22_D20_inp.txt")
    ll.mixing()
    print('----')
    print(len(ll))
    result = ll.get_coords(1000, 2000, 3000)
    print(result, "Sum: ", sum(result))
