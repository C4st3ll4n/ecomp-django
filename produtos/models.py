from django.db import models


class Category(models.Model):
    name = models.CharField("Nome", max_length=50)
    description = models.TextField("Descrição")

    def __str__(self):
        return f"{self.name} tem {self.products.count()}"


class Product(models.Model):
    name = models.CharField("Nome", max_length=100)
    description = models.TextField("Descrição")
    price = models.DecimalField("Preço", max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="products")

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField("Nome do Cliente", max_length=100)
    payment = models.CharField("Meio de Pagamento", max_length=40)
    products = models.ManyToManyField(Product)

    @property
    def total_amount(self):
        return sum([prod.price for prod in self.products.all()])

    def __str__(self):
        return f"{self.name} === {self.total_amount}"
