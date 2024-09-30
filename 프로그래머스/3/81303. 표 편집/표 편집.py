#doubly linkedlist 

class LinkedList :
    def __init__(self,val,prev = None,next = None):
        self.val = val
        self.prev = prev
        self.next = next
        
def solution(n, k, cmd):
    stack = []
    head = LinkedList(0)
    cur_node = head
    
    for i in range(1,n):
        new_node = LinkedList(i)
        new_node.prev = cur_node
        cur_node.next = new_node
        cur_node = cur_node.next
    
    while True:
        cur_node = cur_node.prev
        if cur_node.val == k:
            break
    
    def up(x):
        nonlocal cur_node
        cnt = 0
        while cnt < x:
            cur_node = cur_node.prev
            cnt += 1
    
    def down(x):
        nonlocal cur_node
        cnt = 0
        while cnt < x:
            cur_node = cur_node.next
            cnt += 1
        
    def non_last_delete():
        nonlocal cur_node
        nonlocal stack
        new_next_node = cur_node.next
        if cur_node.prev:
            new_prev_node = cur_node.prev
            new_next_node.prev = new_prev_node
            new_prev_node.next = new_next_node
        else:
            new_next_node.prev = None
        
        stack.append(cur_node)
        cur_node = new_next_node
    
    def last_delete():
        nonlocal cur_node
        new_node = cur_node.prev
        new_node.next = None
        
        stack.append(cur_node)
        cur_node = new_node
    
    def insert(insert_node):
        new_prev_node = insert_node.prev
        new_next_node = insert_node.next
        
        if new_prev_node:
            new_prev_node.next = insert_node
        if new_next_node:
            new_next_node.prev = insert_node
    
    for c in cmd:
        c = c.split()
        if c[0] == 'U':
            cur = up(int(c[1]))
        elif c[0] == 'D':
            cur = down(int(c[1]))
        elif c[0] == 'C':
            if cur_node.next:
                non_last_delete()
            else:
                last_delete()
        else:
            insert_node = stack.pop()
            insert(insert_node)
    
    ans = ['O']*n
    
    for i in stack:
        ans[i.val] = 'X'
    
    return ''.join(ans)