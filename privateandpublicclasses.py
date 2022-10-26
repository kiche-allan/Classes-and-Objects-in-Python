class _Private:
    def __init__(self, name):
        self.name = name

class NotPrivate:
    def __init__(self, name):
        self.name = name
        self.priv = _Private(name)
    def _display(self):
        print('Hello')
        #by using an underscore, u essentially say that it is private and shouldnt be used outseide the modifier
    def display(self):
        print('Hi')