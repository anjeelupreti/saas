import helpers
import requests

from typing import Any
from django.core.management.base import BaseCommand
from django.conf import settings

STATIC_FILES_VENDOR_DIR=getattr(settings,"STATIC_FILES_VENDOR_DIR"  )
VENDOR_STATICFILES ={
    'flowbite.css':'https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.css',
    'flowbite.js':'https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.js',
}

class Command(BaseCommand):
    def handle(self,*args:Any , **options:Any):
        self.stdout.write('Downloading vendor static files')
        completed_urls=[]

        for name , url in VENDOR_STATICFILES.items():
            out_path=STATIC_FILES_VENDOR_DIR /name
            print(name ,':',url)
            download_success=helpers.download_to_local(url, out_path)
            if download_success:
                completed_urls.append(url)
            else:
                self.stdout.write(
                    self.style.ERROR(f'Failed to download {url}')
                )
        if set(completed_urls)==set(VENDOR_STATICFILES.values()):
            self.stdout.write(
                self.style.SUCCESS('Successfully updated vendor static files ! ')
            )
        else:
            self.stdout.write(
                self.style.WARNING('Error in updating some files !! ')
            )

