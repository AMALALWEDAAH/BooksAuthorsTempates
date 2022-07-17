# Generated by Django 2.2.4 on 2022-07-16 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BooksAuthorsTempatesApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='uploaded_by',
        ),
        migrations.AddField(
            model_name='books',
            name='uploaded_by',
            field=models.ManyToManyField(related_name='Books', to='BooksAuthorsTempatesApp.Authors'),
        ),
    ]
