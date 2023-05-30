# Generated by Django 4.2.1 on 2023-05-30 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('horoscope', '0007_alter_category_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('language', models.CharField(choices=[('ru', 'russian'), ('by', 'белмова'), ('fr', 'french')], default='by', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('books', models.ManyToManyField(related_name='books', to='horoscope.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='tags', to='horoscope.tag'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='horoscope.publisher'),
        ),
    ]