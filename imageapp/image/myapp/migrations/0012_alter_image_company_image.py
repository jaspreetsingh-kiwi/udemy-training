# Generated by Django 4.1.4 on 2023-01-04 13:18

from django.db import migrations, models
import myapp.validators


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_image_company_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='company_image',
            field=models.ImageField(upload_to='myimage', validators=[myapp.validators.validate_image]),
        ),
    ]
