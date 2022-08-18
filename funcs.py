def print_blocks(block):
    node = block
    print(node.get_data())
    while node.next:
        node = node.next
        print(node.get_data())