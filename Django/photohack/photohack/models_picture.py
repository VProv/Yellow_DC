from django.db import models


class Picture(models.Model):
    """
    Our awesome Picture model!
    Feel free to add new fields!
    """
    source = models.ImageField(null=True, default=None, upload_to='pictures_upload/')
    processed = models.ImageField(null=True, default=None, upload_to='pictures_download/')
    processing_finished = models.BooleanField(default=False)
    id = models.AutoField(primary_key=True)
