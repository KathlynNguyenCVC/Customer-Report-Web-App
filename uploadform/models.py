from django.db import models
from django.core.exceptions import ValidationError
from upload_validator import FileTypeValidator

PERMISSION_CHOICES = [
    ('FOLFER_TO_USER','Folder to User'),
    ('FOLDER_TO_GROUP','Folder to Group'),
    ('GROUP_TO_USER','Group to Folder')
]
'''def validate_file(value):
        if value.file.content_type != 'text/csv':
            raise ValidationError(u'File not supported')'''

class Report(models.Model):
    is_basic_report = models.BooleanField(default=True)

    #Basic input
    owner = models.CharField(max_length=100)

    #Pivot input
    pivot_perm_folder_to_user = models.BooleanField(default=True)
    pivot_perm_folder_to_group = models.BooleanField(default=False)
    pivot_perm_group_to_user = models.BooleanField(default=False)

    file = models.FileField(help_text="Formats accepted: CSV", 
    upload_to='files/report', 
    validators=[FileTypeValidator(
        allowed_types=['text/csv','application/vnd.ms-excel','text/plain','application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']
    )]
    )

    def __str__(self):
        return self.owner

   


