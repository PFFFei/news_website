# Generated by Django 2.0.5 on 2018-06-22 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entertainment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='新闻标题')),
                ('number', models.CharField(max_length=32, verbose_name='点击量排名')),
                ('clicks', models.CharField(max_length=32, verbose_name='点击量')),
                ('time', models.CharField(max_length=32, verbose_name='时间')),
                ('participate', models.CharField(max_length=32, verbose_name='参与人数')),
                ('comment_num', models.CharField(max_length=32, verbose_name='评论人数')),
                ('comment', models.TextField(verbose_name='评论内容')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
            ],
        ),
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='新闻标题')),
                ('number', models.CharField(max_length=32, verbose_name='点击量排名')),
                ('clicks', models.CharField(max_length=32, verbose_name='点击量')),
                ('time', models.CharField(max_length=32, verbose_name='时间')),
                ('participate', models.CharField(max_length=32, verbose_name='参与人数')),
                ('comment_num', models.CharField(max_length=32, verbose_name='评论人数')),
                ('comment', models.TextField(verbose_name='评论内容')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='新闻标题')),
                ('number', models.CharField(max_length=32, verbose_name='点击量排名')),
                ('clicks', models.CharField(max_length=32, verbose_name='点击量')),
                ('time', models.CharField(max_length=32, verbose_name='时间')),
                ('participate', models.CharField(max_length=32, verbose_name='参与人数')),
                ('comment_num', models.CharField(max_length=32, verbose_name='评论人数')),
                ('comment', models.TextField(verbose_name='评论内容')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
            ],
        ),
        migrations.CreateModel(
            name='Military',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='新闻标题')),
                ('number', models.CharField(max_length=32, verbose_name='点击量排名')),
                ('clicks', models.CharField(max_length=32, verbose_name='点击量')),
                ('time', models.CharField(max_length=32, verbose_name='时间')),
                ('participate', models.CharField(max_length=32, verbose_name='参与人数')),
                ('comment_num', models.CharField(max_length=32, verbose_name='评论人数')),
                ('comment', models.TextField(verbose_name='评论内容')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
            ],
        ),
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='新闻标题')),
                ('number', models.CharField(max_length=32, verbose_name='点击量排名')),
                ('clicks', models.CharField(max_length=32, verbose_name='点击量')),
                ('time', models.CharField(max_length=32, verbose_name='时间')),
                ('participate', models.CharField(max_length=32, verbose_name='参与人数')),
                ('comment_num', models.CharField(max_length=32, verbose_name='评论人数')),
                ('comment', models.TextField(verbose_name='评论内容')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
            ],
        ),
    ]
