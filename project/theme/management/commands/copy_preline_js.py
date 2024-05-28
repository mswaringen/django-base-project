# project/theme/management/commands/copy_preline_js.py

import os
import shutil
from django.core.management.base import BaseCommand
from pathlib import Path

class Command(BaseCommand):
    help = 'Copy and replace preline.js from node_modules to static directory'

    def handle(self, *args, **kwargs):
        base_dir = Path(__file__).resolve().parent.parent.parent.parent.parent
        origin = base_dir / 'project/theme/static_src/node_modules/preline/dist/preline.js'
        destination_dir = base_dir / 'project/static/js'
        destination = destination_dir / 'preline.js'

        if not origin.exists():
            self.stderr.write(f"Source file {origin} does not exist.")
            return

        if not destination_dir.exists():
            destination_dir.mkdir(parents=True, exist_ok=True)

        try:
            shutil.copyfile(origin, destination)
            self.stdout.write(self.style.SUCCESS(f'Successfully copied {origin} to {destination}'))
        except Exception as e:
            self.stderr.write(f"Error copying file: {e}")
