# Generated by Django 2.2.17 on 2020-12-05 12:53

import adminsortable.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=300)),
                ('counter', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='AudioContent',
            fields=[
                ('basecontent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='page.BaseContent')),
                ('bitrate', models.PositiveIntegerField(default=0)),
            ],
            bases=('page.basecontent',),
        ),
        migrations.CreateModel(
            name='TextContent',
            fields=[
                ('basecontent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='page.BaseContent')),
                ('text', models.TextField()),
            ],
            bases=('page.basecontent',),
        ),
        migrations.CreateModel(
            name='VideoContent',
            fields=[
                ('basecontent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='page.BaseContent')),
                ('video_url', models.URLField()),
                ('subtitle_url', models.URLField()),
            ],
            bases=('page.basecontent',),
        ),
        migrations.CreateModel(
            name='PageContents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_order', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
                ('content', adminsortable.fields.SortableForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pgs', to='page.BaseContent')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.Page')),
            ],
            options={
                'ordering': ('content_order',),
            },
        ),
        migrations.AddField(
            model_name='page',
            name='contents',
            field=models.ManyToManyField(related_name='pages', through='page.PageContents', to='page.BaseContent'),
        ),
    ]