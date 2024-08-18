class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    def __init__(self, file_name='products.txt'):
        self.file_name = file_name

    def get_products(self):
        with open(self.file_name, 'r') as file:
            products = file.read()
        return products

    def add(self, *products):
        ex_products = self.get_products()
        with open(self.file_name, 'a+') as file:
            for product in products:
                if product.name not in ex_products:
                    file.write(str(product) + '\n')
                else:
                    print(f'Продукт {product.name}, {product.weight}, {product.category} уже есть в магазине')
        file.close()

# Пример использования
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())