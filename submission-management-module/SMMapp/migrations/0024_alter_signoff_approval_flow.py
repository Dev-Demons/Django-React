# Generated by Django 4.0.4 on 2022-07-17 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SMMapp', '0023_submission_document_srm_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signoff',
            name='approval_flow',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='signoff_approval_flow', to='SMMapp.approvalflow'),
        ),
    ]
