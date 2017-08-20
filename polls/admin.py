"""This module registers models an administrator can manage"""
from django.contrib import admin

from .models import Question

admin.site.register(Question)
