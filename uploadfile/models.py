import hashlib
import base64
import uuid

from django.db import models

# Create your models here.
from django.db import models


def base_64_file(data):
    _format, _img_str = data.split(';base64,')
    _name, ext = _format.split('/')
    imgdata = base64.b64decode(_img_str)
    img_name = str(uuid.uuid4()) + '.' + ext
    filename = 'media/' + img_name  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)
    return filename


# def content_file_name(instance, filename):
#     print('filename: {}'.format(filename))
#     file = str(filename).split('.')
#     ext = file[len(file) - 1]
#     new_filename = ''.join(file[:len(file) - 1])
#     return '/'.join(['media', str(hashlib.md5(new_filename.encode()).hexdigest()) + '.' + ext])


class File(models.Model):
    file = models.CharField(max_length=200)

    def __str__(self):
        return self.file
