# Generated by Django 3.1.3 on 2022-03-23 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioSeg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=200)),
                ('seg_id', models.IntegerField()),
                ('start_time', models.FloatField()),
                ('end_time', models.FloatField()),
                ('length', models.FloatField()),
                ('norm_length', models.FloatField()),
                ('transcript', models.TextField()),
                ('importance', models.FloatField()),
                ('match_scores', models.CharField(max_length=1000)),
                ('score', models.FloatField()),
                ('norm_score', models.FloatField()),
                ('silence_detection', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='DescriptionAudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=200)),
                ('seg_id', models.IntegerField()),
                ('start_time', models.FloatField()),
                ('end_time', models.FloatField()),
                ('length', models.FloatField()),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='DescriptionVisual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=200)),
                ('seg_id', models.IntegerField()),
                ('start_time', models.FloatField()),
                ('end_time', models.FloatField()),
                ('length', models.FloatField()),
                ('type', models.CharField(choices=[('IN', 'Inline'), ('EX', 'Extended')], default='IN', max_length=2)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.CharField(max_length=50)),
                ('event', models.CharField(max_length=50)),
                ('video_id', models.CharField(max_length=200)),
                ('audio_visual', models.CharField(max_length=50)),
                ('seg_id', models.CharField(max_length=50)),
                ('seg_timestamp', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=1000)),
                ('value', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=200)),
                ('problem_description', models.CharField(max_length=1000)),
                ('visual_seg_id', models.IntegerField()),
                ('audio_seg_id', models.IntegerField()),
                ('start_time', models.FloatField()),
                ('end_time', models.FloatField()),
                ('length', models.FloatField()),
                ('describe_visual', models.BooleanField()),
                ('describe_audio', models.BooleanField()),
                ('is_ignored', models.BooleanField()),
                ('is_fixed', models.BooleanField()),
            ],
            options={
                'ordering': ['start_time'],
            },
        ),
        migrations.CreateModel(
            name='VisualSeg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=200)),
                ('seg_id', models.IntegerField()),
                ('start_time', models.FloatField()),
                ('end_time', models.FloatField()),
                ('length', models.FloatField()),
                ('norm_length', models.FloatField()),
                ('importance', models.FloatField()),
                ('match_scores', models.CharField(max_length=1000)),
                ('score', models.FloatField()),
                ('norm_score', models.FloatField()),
                ('detected_visuals', models.CharField(max_length=1000)),
                ('detected_texts', models.CharField(max_length=1000)),
                ('presenter_detection', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=200)),
                ('visual_seg_id', models.IntegerField()),
                ('audio_seg_id', models.IntegerField()),
                ('start_time', models.FloatField()),
                ('end_time', models.FloatField()),
                ('length', models.FloatField()),
                ('word', models.CharField(max_length=200)),
            ],
        ),
    ]
