class Library:
    def __init__(self):
        self.NoOfBooks = 0
        self.BookList = []
    def answer(self,bookname):
        self.BookList.append(bookname)

    def totalbooks(self):
        blength = len(self.BookList)
        print(f'We have only {blength} books')



obj = Library()
obj.answer('The Sky 1')
obj.answer('The Sky 2')
obj.answer('The Sky 3')
obj.totalbooks()
