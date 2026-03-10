class TextEditor:
    def __init__(self):
        self.text = ""
        self.stack = []

    def add(self, c):
        self.text += c
        self.stack.append(("ADD", c))
        print("Current Text:", self.text)

    def delete(self):
        if len(self.text) == 0:
            print("Nothing to delete.")
            return

        removed = self.text[-1]
        self.text = self.text[:-1]
        self.stack.append(("DELETE", removed))
        print("Current Text:", self.text)

    def undo(self):
        if len(self.stack) == 0:
            print("Nothing to undo.")
            return

        operation, char = self.stack.pop()

        if operation == "ADD":
            self.text = self.text[:-1]
        elif operation == "DELETE":
            self.text += char

        print("Current Text:", self.text)


editor = TextEditor()

editor.add('A')
editor.add('B')
editor.add('C')

editor.delete()
editor.delete()
editor.delete()

editor.undo()
editor.undo()
editor.undo()