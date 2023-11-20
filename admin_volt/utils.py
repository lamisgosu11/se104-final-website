import datetime
import json
from django.template import Context
from django.utils import translation

try:
    from django.apps.registry import apps
except ImportError:
    try:
        from django.apps import apps  # Fix Django 1.7 import issue
    except ImportError:
        pass
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse

try:
    from django.core.urlresolvers import reverse, resolve, NoReverseMatch
except ImportError:  # Django 1.11
    from django.urls import reverse, resolve, NoReverseMatch

from django.contrib.admin import AdminSite
from django.utils.text import capfirst
from django.contrib import messages
from django.contrib.admin.options import IncorrectLookupParameters
from django.contrib import admin
from django.utils.text import slugify

try:
    from django.utils.translation import ugettext_lazy as _
except ImportError:
    from django.utils.translation import gettext_lazy as _  # Django 4.0.0 and more

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict  # Python 2.6


default_apps_icon = {
    'auth': 'fa fa-users'
}
