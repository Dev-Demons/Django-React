# Generated by Django 4.0.4 on 2022-07-27 10:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SMMapp', '0032_submission_ext_rev'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='associated_content',
        ),
        migrations.AddField(
            model_name='submission',
            name='discipline_code',
            field=models.CharField(choices=[('AR', 'Architectural'), ('BD', 'Building Services'), ('CV', 'Civil'), ('LU', 'Landscape'), ('ST', 'Structural'), ('MA', 'Marine or Water Tributary'), ('RD', 'Roadworks'), ('DR', 'Drainage works'), ('MD', 'Multi Discipline'), ('GE', 'Geotechnical works'), ('SL', 'Slopworks'), ('ME', 'Mechanical-Electrical'), ('UU', 'Underground Utility'), ('NA', 'Not Applicable')], default='NA', max_length=100, verbose_name='Discipline Code'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='submission',
            name='name',
            field=models.CharField(default='Test', max_length=100, verbose_name='Submission name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='submission',
            name='person_in_charge',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='person_in_charge', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='submission',
            name='remark',
            field=models.TextField(blank=True, null=True, verbose_name='Remark'),
        ),
        migrations.AddField(
            model_name='submission',
            name='responsible_party',
            field=models.CharField(choices=[('Main Contractor', 'Main Contractor'), ('Sub Contractor', 'Sub Contractor'), ('Property Owner', 'Property Owner')], default=1, max_length=100, verbose_name='Responsible Party'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='submission',
            name='trade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='trade', to='SMMapp.trade'),
            preserve_default=False,
        ),
    ]