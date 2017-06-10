# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
#my imports
from blog.models import Post

# Register your models here.
admin.site.register(Post)