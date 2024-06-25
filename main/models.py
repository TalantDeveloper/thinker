import os
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


def upload_image(instance, filename):
    # Get current date
    now = datetime.now()
    # Define the upload path
    year_month = now.strftime('%Y-%m')  # Format: YYYY-MM

    # Modify filename (example: adding timestamp)
    filename_without_ext, ext = os.path.splitext(filename)
    timestamp = now.strftime('%Y%m%d%H%M%S')
    new_filename = f"{timestamp}{ext}"

    return os.path.join('image', year_month, new_filename)


def upload_file(instance, filename):
    # Get current date
    now = datetime.now()
    # Define the upload path
    year_month = now.strftime('%Y-%m')  # Format: YYYY-MM

    # Modify filename (example: adding timestamp)
    filename_without_ext, ext = os.path.splitext(filename)
    timestamp = now.strftime('%Y%m%d%H%M%S')
    new_filename = f"{timestamp}{ext}"

    return os.path.join('file', year_month, new_filename)


class Newsletter(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    image = models.ImageField(upload_to=upload_image, verbose_name="Image")
    file = models.FileField(upload_to=upload_file, verbose_name="File")
    content = RichTextUploadingField(verbose_name="Content")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    def __str__(self):
        return self.name
