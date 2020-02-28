from django.db import models
from django.core.exceptions import ValidationError

PERMISSION_CHOICES = [
    ('FOLFER_TO_USER','Folder to User'),
    ('FOLDER_TO_GROUP','Folder to Group'),
    ('GROUP_TO_USER','Group to Folder')
]
def validate_file(value):
        if value.file.content_type != 'text/csv':
            raise ValidationError(u'File not supported')

class Report(models.Model):
    owner = models.CharField(max_length=100)
    is_basic_report = models.BooleanField(default=True)
    permission = models.CharField(max_length=100,choices=PERMISSION_CHOICES)
    file = models.FileField(upload_to='files/report', validators=[validate_file])

    def __str__(self):
        return self.owner

   
