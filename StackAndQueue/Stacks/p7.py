#Implement "Forward" and "Back" buttons of browser using Stacks. Elements need to be stored are URLs.
class Browser:
    def __init__(self):
        self.back_stack = []  
        self.forward_stack = []  
        self.current_url = None 

    def visit(self, url):
        if self.current_url:
            self.back_stack.append(self.current_url)  
        self.current_url = url  
        self.forward_stack.clear()  
        print("Visited:", self.current_url)

    def back(self):
        if self.back_stack:
            self.forward_stack.append(self.current_url)  
            self.current_url = self.back_stack.pop()  
            print("Moved back to:", self.current_url)
        else:
            print("No pages in back history.")

    def forward(self):
        if self.forward_stack:
            self.back_stack.append(self.current_url)  
            self.current_url = self.forward_stack.pop() 
            print("Moved forward to:", self.current_url)
        else:
            print("No pages in forward history.")


browser = Browser()

browser.visit("google.com")
browser.visit("youtube.com")
browser.visit("github.com")

browser.back()  
browser.back()  

browser.forward()  

browser.visit("stackoverflow.com")  

browser.back()  
browser.forward()  
