# Dockerを使ってDjangoとデータベースを起動すると、１つ問題がある。
# たとえ、depends on で app の前に db が起動するように設定しても、それは、データベースの初期化が終わるところまで保証していない。
# つまり、データベースが完全に立ち上がっていない状況でDJANGOが起動してしまい、crashしてしまう可能性があるのだ。
# よって、Djangoにはデータベースが完全に立ち上がるまで待機してもらうようにコードを書く。

"""
Django command to wait for the database to be available.
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))

# As soon as the exception stops being thrown, we can assume the database is now available.