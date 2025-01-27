#Reverse the content of file using stack
class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        else:
            return None

    def __str__(self):
        return str(self.data)


def reverse_text(text):
    stack = Stack()
    
    for char in text:
        stack.push(char)
    
    reversed_text = []
    while not stack.is_empty():
        reversed_text.append(stack.pop())
    
    return ''.join(reversed_text)


def reverse_file_content(input_file_path, output_file_path):
    with open(input_file_path, 'r') as infile:
        lines = infile.readlines()
    
    with open(output_file_path, 'w') as outfile:
        for line in lines:
            reversed_line = reverse_text(line.strip())  
            outfile.write(reversed_line + '\n') 


if __name__ == "__main__":
    input_file = 'input.txt' 
    output_file = 'reversed_output.txt' 
    reverse_file_content(input_file, output_file)
    print("Content reversed and written to", output_file)