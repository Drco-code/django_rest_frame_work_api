from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from api_copy.models import *
from django.core.cache import cache


@receiver([post_save, post_delete], sender=Product)
def invalidate_product_cache(sender, instance, **kwargs):
    """
    Invalidate Porduct list caches when a product os created, update, deleted
    """
    print("Clearing product cache")

    # TODO
    # Clear Product list
    cache.delete_pattern('*product_list*')