# Generated by Django 3.2.22 on 2023-10-19 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorBio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_bio', models.CharField(max_length=600)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='author_bio',
            field=models.CharField(default='author', max_length=600),
        ),
    ]
