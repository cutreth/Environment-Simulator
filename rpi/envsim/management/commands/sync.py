from django.core.management.base import BaseCommand

import envsim.do as do


class Command(BaseCommand):

    def handle(self, *args, **options):
        do.sync()
        return None
