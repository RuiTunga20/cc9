# Generated by Django 4.1.5 on 2023-05-10 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landpage', '0006_rename_ppt_noticia_imagem_remove_moderador_data_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noticia',
            old_name='imagem',
            new_name='fotos',
        ),
    ]
