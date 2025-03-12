from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import uuid



class User(AbstractUser):
    pass


class Product(models.Model):
    name = models.CharField(_("Name"), max_length=200)
    description = models.TextField(_("Description"))
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(_("Stock"))
    image = models.ImageField(_("Image"), upload_to='products/',  blank=True, null=True)

    """
    @property
    def in_stock(self):
        if self.stock > 0:
            print(f"{self.name} has {self.stock} items left")
        else:
            print(f"{self.name} is out of stock")
    """
    
    @property
    def in_stock(self):
        return self.stock > 0
    
    def __str__(self):
        return self.name
    

class Order(models.Model):

    class StatusChoices(models.TextChoices):
        PENDING = 'Pending'
        CONFIRMED = 'Confirmed'
        CANCELLED = 'Cancelled'

    order_id = models.UUIDField(_("Oder ID"), primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(_("Order Creation Date"), auto_now_add=True)
    status = models.CharField(_("Order Status"), max_length=10, choices=StatusChoices.choices, default=StatusChoices.PENDING)
    products = models.ManyToManyField(Product, through="OrderItem", verbose_name=_("Products"), related_name="orders")

    def __str__(self):
        return f"Order {self.order_id} by {self.user.username}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='items', verbose_name=_("Order"), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_("Product"), on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(_("Quantity"))


    @property
    def item_subtotal(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.order_id}"

