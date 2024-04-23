# Generated by Django 4.2.11 on 2024-04-22 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on', 'author']},
        ),
        migrations.AddField(
            model_name='post',
            name='field_2',
            field=models.IntegerField(default=42),
        ),
        migrations.AddField(
            model_name='post',
            name='field_3',
            field=models.CharField(null=True),
        ),
    ]
