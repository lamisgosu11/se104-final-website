from django.conf import settings
from django.core.cache import cache, caches


# generate cache for items
def app_cache():
    return caches["admin_notification"] if "admin_notification" in settings.CACHES else cache

# delete notification


def del_cached_active_item():
    app_cache().delete("admin_notification_item")

# get notification


def get_cached_active_item():
    return app_cache().get("admin_notification_item", None)

# set notification to save in cache


def set_cached_active_item(item):
    app_cache().set("admin_notification_item", item)
