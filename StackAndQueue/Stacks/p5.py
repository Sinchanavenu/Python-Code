#Match the tags in html file using stack
import re
from collections import deque

def is_valid_html(file_path):
    with open(file_path, 'r') as file:
        html = file.read()

    tag_regex = r'<(/?[^/>]+)>' 

    stack = deque()

    tags = re.findall(tag_regex, html)

    
    for tag in tags:
        tag = tag.strip()

        if tag.startswith('/'):
            tag_name = tag[1:].strip()  
            if not stack or stack[-1] != tag_name:  
                return False
            stack.pop()  

        else:
            if tag.endswith('/'):
                continue

            tag_name = tag.split()[0]  
            stack.append(tag_name)

    
    return len(stack) == 0

file_path = 'example.html'  

if is_valid_html(file_path):
    print("The HTML file has properly matched tags.")
else:
    print("The HTML file has unmatched tags.")
