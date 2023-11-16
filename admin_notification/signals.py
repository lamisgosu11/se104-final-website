from django.db.models.signals import post_delete, post_save, pre_save
from django.apps.registry import Apps
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import HttpResponse, redirect
from django.apps import apps as django_apps
from admin_notification.models import Notification
from django.dispatch import receiver
from django import dispatch