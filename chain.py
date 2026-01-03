class Handler:
    def __init__(self, name):
        self.name = name
        self.next = None
    
    def set_next(self, handler):
        self.next = handler
        return handler
    
    def handle(self, request):
        if self.next:
            return self.next.handle(request)
        return f"Никто не обработал: {request}"

class Manager(Handler):
    def handle(self, request):
        if request == "отпуск":
            return f"{self.name}: Одобряю отпуск"
        return super().handle(request)

class Director(Handler):
    def handle(self, request):
        if request == "повышение":
            return f"{self.name}: Рассмотрю повышение"
        return super().handle(request)

if __name__ == "__main__":
    manager = Manager("Менеджер")
    director = Director("Директор")

    manager.set_next(director)
    print(manager.handle("отпуск"))
    print(manager.handle("повышение"))
