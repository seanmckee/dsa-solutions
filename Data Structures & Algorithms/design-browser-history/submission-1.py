class Page:
    def __init__(self, url:str, next = None, prev = None):
        self.url = url
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Page(homepage)
        self.tail = self.head
        self.length = 1
        self.current = self.head
        

    def visit(self, url: str) -> None:
        new_page = Page(url)
        new_page.prev = self.current
        self.current.next = new_page
        self.tail = new_page
        self.current = new_page
        

    def back(self, steps: int) -> str:

        for _ in range(steps):
            if self.current.prev == None:
                return self.current.url
            self.current = self.current.prev
        return self.current.url
        

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.current.next == None:
                return self.current.url
            self.current = self.current.next
        return self.current.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)