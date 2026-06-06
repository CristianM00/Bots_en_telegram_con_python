class Todo:
    def __init__(self, titulo):
        self.titulo = titulo
        self.is_completed = False

    def set_completed(self):
        self.is_completed = True

    