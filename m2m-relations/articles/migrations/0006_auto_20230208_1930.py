# Generated by Django 3.1.2 on 2023-02-08 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20230208_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(related_name='tag', through='articles.TagsTitle', to='articles.Tag'),
        ),
        migrations.AlterField(
            model_name='tagstitle',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article'),
        ),
        migrations.AlterField(
            model_name='tagstitle',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.tag'),
        ),
    ]
