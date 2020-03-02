from django.db import models
from django.core.exceptions import ValidationError
from upload_validator import FileTypeValidator
from multiselectfield import MultiSelectField

PERMISSION_CHOICES = [
    ('FOLFER_TO_USER','Folder to User'),
    ('FOLDER_TO_GROUP','Folder to Group'),
    ('GROUP_TO_USER','Group to Folder')
]
'''def validate_file(value):
        if value.file.content_type != 'text/csv':
            raise ValidationError(u'File not supported')'''

class Report(models.Model):
    owner = models.CharField(max_length=100)
    is_basic_report = models.BooleanField(default=True)
    permission = MultiSelectField(choices=PERMISSION_CHOICES)
    file = models.FileField(help_text="Formats accepted: CSV", 
    upload_to='files/report', 
    validators=[FileTypeValidator(
        allowed_types=['text/csv','application/vnd.ms-excel','text/plain','application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']
    )]
    )

    def __str__(self):
        return self.owner

   


