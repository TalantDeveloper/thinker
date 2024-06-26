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

    sees = models.IntegerField(verbose_name="Sees", default=3)

    def __str__(self):
        return self.name


class Announcement(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    image = models.ImageField(upload_to=upload_image, verbose_name="Image", default='/image/elon.jpg')
    content = RichTextUploadingField(verbose_name="Content")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    def __str__(self):
        return self.name


class Pages(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    short = models.CharField(max_length=200)
    content = RichTextUploadingField(verbose_name="Content")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    def __str__(self):
        return self.name


# class Welcome(models.Model):
#     name_1 = models.CharField(max_length=255, verbose_name="Name 1")
#     title_1 = models.TextField(verbose_name="Title 1")
#     image_1 = models.ImageField(upload_to=upload_image, verbose_name="Image 1")
#     name_2 = models.CharField(max_length=255, verbose_name="Name 2")
#     title_2 = models.TextField(verbose_name="Title 2")
#     image_2 = models.ImageField(upload_to=upload_image, verbose_name="Image 2")
#
#     def __str__(self):
#         return self.name_1 + self.name_2
