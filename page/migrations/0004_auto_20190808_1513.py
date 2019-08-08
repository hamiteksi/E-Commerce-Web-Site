# Generated by Django 2.2.2 on 2019-08-08 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_auto_20190806_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='carousel')),
                ('status', models.CharField(choices=[('draft', 'Taslak'), ('published', 'Yayinlandi'), ('deleted', 'Silindi')], default='draft', max_length=10)),
                ('createt_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='page',
            name='coverimage',
            field=models.ImageField(blank=True, null=True, upload_to='page'),
        ),
    ]