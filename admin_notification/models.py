from __future__ import unicode_literals
from django.contrib.auth.models import User
from admin_notification.cache import del_cached_active_item
from django.db import models
from django.db.models.signals import post_delete, post_save, pre_save
from six import python_2_unicode_compatible