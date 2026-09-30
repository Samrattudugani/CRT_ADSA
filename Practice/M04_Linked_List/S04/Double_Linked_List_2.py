class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class dl:
    def __init__(self):
        self.head = None

    def inb(self, data):
        new = Node(data)

        new.next = self.head

        if self.head:
            self.head.prev = new

        self.head = new

    def ine(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            return

        curr = self.head

        while curr.next:
            curr = curr.next

        curr.next = new
        new.prev = curr

    def dib(self):
        if self.head is None:
            print("LIST IS EMPTY")
            return

        self.head = self.head.next

        if self.head:
            self.head.prev = None

    def die(self):
        if self.head is None:
            print("LIST IS EMPTY")
            return

        curr = self.head

        while curr.next:
            curr = curr.next

        if curr.prev:
            curr.prev.next = None
        else:
            self.head = None

    def cnd(self):
        if self.head is None:
            print("LIST IS EMPTY")
            return 0

        c = 0
        curr = self.head

        while curr:
            c += 1
            curr = curr.next

        return c

        # DELETE AT A POSITION:
    def dip(self, pos):
        if self.head is None:
            print("LIST IS EMPTY")
            return

        if pos <= 0:
            print("INVALID POSITION")
            return

        curr = self.head

        for i in range(pos - 1):
            if curr is None:
                print("INVALID POSITION")
                return
            curr = curr.next

        if curr is None:
            print("INVALID POSITION")
            return

        if curr.prev:
            curr.prev.next = curr.next
        else:
            self.head = curr.next

        if curr.next:
            curr.next.prev = curr.prev








    def trav(self):
        curr = self.head

        while curr:
            print(curr.data, end="<---->")
            curr = curr.next

        print("None")
    


dl = dl()

dl.inb(10)
dl.inb(20)
dl.inb(30)
dl.ine(908908)

dl.ine(40)
dl.ine(50)

dl.trav()

dl.dib()
dl.trav()

dl.die()
dl.trav()

print("COUNT =", dl.cnd())

dl.dip(2)
dl.trav()
