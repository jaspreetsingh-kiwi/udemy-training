from django.core.exceptions import ValidationError


def validate_image(image_obj):
    imagesize = image_obj.file.size
    kilobyte_limit = 20480
    if imagesize > kilobyte_limit:
        raise ValidationError("Max file size is 20KB")
