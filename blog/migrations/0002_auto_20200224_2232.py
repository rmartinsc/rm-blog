# Generated by Django 2.2.10 on 2020-02-24 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-published_date']},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='content',
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='none', max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
