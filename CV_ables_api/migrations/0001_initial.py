# Generated by Django 4.0.3 on 2022-03-09 02:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github_url', models.URLField(max_length=500, null=True)),
                ('portfolio_url', models.URLField(max_length=500, null=True)),
                ('linkedin_url', models.URLField(max_length=500, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=2, null=True)),
                ('zipcode', models.CharField(max_length=10, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='applicant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Framework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lable', models.CharField(max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jobtype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lable', models.CharField(max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lable', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission_text', models.CharField(max_length=500, null=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='missions', to='CV_ables_api.applicant')),
                ('jobtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='missions', to='CV_ables_api.jobtype')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, null=True)),
                ('github_url', models.URLField(max_length=500, null=True)),
                ('deploy_url', models.URLField(max_length=500, null=True)),
                ('image_url', models.URLField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prospect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prospect_name', models.CharField(max_length=100, null=True)),
                ('listing_url', models.URLField(max_length=500, null=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prospect', to='CV_ables_api.applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Vita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.BooleanField(default=False)),
                ('slug', models.SlugField(null=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vita', to='CV_ables_api.applicant')),
                ('job_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vita', to='CV_ables_api.jobtype')),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vita', to='CV_ables_api.mission')),
                ('prospect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vita', to='CV_ables_api.prospect')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100, null=True)),
                ('company', models.CharField(max_length=100, null=True)),
                ('start_yr', models.CharField(max_length=4, null=True)),
                ('end_yr', models.CharField(max_length=4, null=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='CV_ables_api.applicant')),
                ('framework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='CV_ables_api.framework')),
                ('job_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='CV_ables_api.jobtype')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=500, null=True)),
                ('state', models.CharField(max_length=2, null=True)),
                ('diploma', models.CharField(max_length=100, null=True)),
                ('grad_year', models.CharField(max_length=4, null=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education', to='CV_ables_api.applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_text', models.CharField(max_length=1000, null=True)),
                ('experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='descriptions', to='CV_ables_api.experience')),
            ],
        ),
    ]