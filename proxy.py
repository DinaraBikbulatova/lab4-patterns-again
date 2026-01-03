class RealImage:
    def display(self):
        return "Показываю тяжелое изображение"

class ProxyImage:
    def __init__(self):
        self.real_image = None
        self.cached = False
    
    def display(self):
        if not self.cached:
            print("Загружаю изображение...")
            self.real_image = RealImage()
            self.cached = True
        return self.real_image.display()

if __name__ == "__main__":
    image = ProxyImage()
    print(image.display())
    print(image.display())
