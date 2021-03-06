# Generated by Django 3.0.9 on 2020-09-28 20:25

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(default=1, verbose_name='iin chandomie?')),
                ('title', models.CharField(default='', max_length=100)),
                ('summary', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='انتشار')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='ساخت')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='آپدیت')),
                ('status', models.CharField(choices=[('draft', 'در حال انتظار'), ('published', 'منتشر شده')], default='draft', max_length=60, verbose_name='وضعیت')),
                ('developed_by', models.URLField(blank=True, null=True)),
                ('is_framework', models.BooleanField(default=False)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Blogger')),
            ],
        ),
        migrations.CreateModel(
            name='FrameWork',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='language.Post')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('lang', models.CharField(choices=[('HTML5', 'HTML'), ('Bootstrap4', 'Bootstrap4'), ('Css3', 'Css3'), ('Js', 'js'), ('Kotlin', 'Kotlin'), ('Java', 'java'), ('C++', 'C++'), ('Perl', 'Perl'), ('C-Sharp', 'C-Sharp'), ('Python', 'Python'), ('GraphQL', 'GraphQL'), ('REST', 'REST'), ('PostgreSQL', 'PostgreSQL'), ('MySQL', 'MySQL'), ('SQLServer', 'SQLServer'), ('linux', 'linux'), ('git', 'git'), ('ducker', 'ducker')], default='HTML', max_length=100)),
            ],
            bases=('language.post',),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='language.Post')),
                ('name', models.CharField(choices=[('HTML5', 'HTML'), ('Bootstrap4', 'Bootstrap4'), ('Css3', 'Css3'), ('Js', 'js'), ('Kotlin', 'Kotlin'), ('Java', 'java'), ('C++', 'C++'), ('Perl', 'Perl'), ('C-Sharp', 'C-Sharp'), ('Python', 'Python'), ('GraphQL', 'GraphQL'), ('REST', 'REST'), ('PostgreSQL', 'PostgreSQL'), ('MySQL', 'MySQL'), ('SQLServer', 'SQLServer'), ('linux', 'linux'), ('git', 'git'), ('ducker', 'ducker')], default='HTML', max_length=100)),
            ],
            options={
                'ordering': ('created',),
            },
            bases=('language.post',),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='language.Comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='language.Post')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
