# Generated by Django 1.11.24 on 2019-10-02 16:40


from django.db import migrations
import django_extensions.db.fields


def populate_slug(apps, schema_editor):
    Organization = apps.get_model('course_metadata', 'Organization')
    for org in Organization.objects.all():
        marketing_url = getattr(org, 'marketing_url_path')
        org.slug = marketing_url.rsplit('/')[-1] if marketing_url else getattr(org, 'key', '').lower()
        org.save()


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0200_auto_20191007_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='key'),
        ),
        migrations.RunPython(populate_slug, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name='organization',
            name='marketing_url_path',
        ),
    ]
