from django.db import models

PERMISSION_CHOICES = [
    ('FOLFER_TO_USER','Folder to User'),
    ('FOLDER_TO_GROUP','Folder to Group'),
    ('GROUP_TO_USER','Group to Folder')
]

class Report(models.Model):
    owner = models.CharField(max_length=100)
    is_basic_report = models.BooleanField()
    permission = models.CharField(max_length=100,choices=PERMISSION_CHOICES)
    file = models.FileField(upload_to='files/report')

    def __str__(self):
        return self.owner