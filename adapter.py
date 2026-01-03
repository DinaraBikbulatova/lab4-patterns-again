class OldPrinter:
    def print_text(self, text):
        return f"Печатаю: {text}"

class NewPrinter:
    def print_document(self, document):
        pass

class PrinterAdapter(NewPrinter):
    def __init__(self):
        self.old_printer = OldPrinter()
    
    def print_document(self, document):
        return self.old_printer.print_text(document)

if __name__ == "__main__":
    printer = PrinterAdapter()
    print(printer.print_document("Hello World"))
