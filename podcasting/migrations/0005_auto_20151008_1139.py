# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('podcasting', '0004_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique='True', verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='show',
            name='editor_email',
            field=models.EmailField(help_text="Email address of the person responsible for the feed's content.", max_length=254, verbose_name='editor email', blank=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique='True', verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='show',
            name='webmaster_email',
            field=models.EmailField(help_text='Email address of the person responsible for channel publishing.', max_length=254, verbose_name='webmaster email', blank=True),
        ),
    ]
