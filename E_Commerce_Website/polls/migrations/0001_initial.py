# Generated by Django 2.0.1 on 2020-04-26 20:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('status', models.CharField(default='Inactive', max_length=200)),
                ('created_at', models.DateTimeField()),
                ('modified_at', models.DateTimeField()),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete='models.CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]