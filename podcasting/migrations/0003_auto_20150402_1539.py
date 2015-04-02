# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import podcasting.models


class Migration(migrations.Migration):

    dependencies = [
        ('podcasting', '0002_auto_20140914_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='original_image',
            field=sorl.thumbnail.fields.ImageField(help_text='\n            A podcast must have 1400 x 1400 pixel cover art in JPG or PNG\n            format using RGB color space. See our technical spec for\n            details. To be eligible for featuring on iTunes Stores,\n            choose an attractive, original, and square JPEG (.jpg) or\n            PNG (.png) image at a size of 1400x1400 pixels. The image\n            will be scaled down to 50x50 pixels at smallest in iTunes.\n            For reference see the <a\n            href="http://www.apple.com/itunes/podcasts/specs.html#metadata">iTunes\n            Podcast specs</a>.<br /><br /> For episode artwork to\n            display in iTunes, image must be <a\n            href="http://answers.yahoo.com/question/index?qid=20080501164348AAjvBvQ">\n            saved to file\'s <strong>metadata</strong></a> before\n            enclosure uploading!', upload_to=podcasting.models.get_episode_upload_folder, verbose_name='image', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='show',
            name='original_image',
            field=sorl.thumbnail.fields.ImageField(help_text='\n            A podcast must have 1400 x 1400 pixel cover art in JPG or PNG\n            format using RGB color space. See our technical spec for\n            details. To be eligible for featuring on iTunes Stores,\n            choose an attractive, original, and square JPEG (.jpg) or\n            PNG (.png) image at a size of 1400x1400 pixels. The image\n            will be scaled down to 50x50 pixels at smallest in iTunes.\n            For reference see the <a\n            href="http://www.apple.com/itunes/podcasts/specs.html#metadata">iTunes\n            Podcast specs</a>.<br /><br /> For episode artwork to\n            display in iTunes, image must be <a\n            href="http://answers.yahoo.com/question/index?qid=20080501164348AAjvBvQ">\n            saved to file\'s <strong>metadata</strong></a> before\n            enclosure uploading!', upload_to=podcasting.models.get_show_upload_folder, verbose_name='image', blank=True),
            preserve_default=True,
        ),
    ]
