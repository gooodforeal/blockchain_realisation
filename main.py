from funcs import *
from Block import Block


Head = Block("006acd34172f6ac83d93a7f615b92356723bc80293e9c7aeccc9240f6bed18b1", "Ivan", 100, 1)
Head.append("Alex", 144)
print_blocks(Head)