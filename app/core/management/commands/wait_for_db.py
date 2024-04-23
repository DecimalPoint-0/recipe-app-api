"""Django command to wait for database to be availbale"""
from typing import Any
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for db"""

    def handle(self, *args, **options):
        pass