"""
Django command to wait for the database to be available
"""
import time

from django.core.management.base import BaseCommand

from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2OpError

class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        db_up = False
        while db_up is False:
            self.stdout.write('Entered WHILE')
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable.')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available'))

