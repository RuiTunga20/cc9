from django.db import models

# Create your models here.


class prelector(models.Model):
    nome=models.CharField(max_length=200, blank=False)
    Descricao=models.CharField(max_length=200, blank=False)
    foto=models.ImageField(upload_to="media/foto")
    def __str__(self):
        return self.nome+" - "+ self.Descricao


class moderador(models.Model):
    nome=models.CharField(max_length=200, blank=False)
    Descricao=models.CharField(max_length=200, blank=False)
    foto=models.ImageField(upload_to="media/foto")

    def __str__(self):
        return self.nome +" - "+ self.Descricao
    


class Programa1(models.Model):
    Titulo=models.CharField(max_length=200, blank=False)
    prelector=models.CharField(max_length=200, blank=True,null=True)
    Tempo=models.CharField(max_length=200,  blank=True,null=True)
    horario=models.CharField(max_length=200, blank=True,null=True)
    Descricao=models.CharField(max_length=200, blank=True,null=True)
    Titulo_break = models.CharField(max_length=50, choices=[('Sim', 'Sim'), ('Não', 'Não')],default="Não")
    Ppt=models.FileField(upload_to="media/ptt", blank=True,null=True)

    def __str__(self):
        return self.Titulo

class Programa2(models.Model):
    Titulo=models.CharField(max_length=200, blank=False)
    prelector=models.CharField(max_length=200, blank=True,null=True)
    Tempo=models.CharField(max_length=200,  blank=True,null=True)
    horario=models.CharField(max_length=200, blank=True,null=True)
    Descricao=models.CharField(max_length=200, blank=True,null=True)
    Titulo_break = models.CharField(max_length=50, choices=[('Sim', 'Sim'), ('Não', 'Não')],default="Não")
    Ppt=models.FileField(upload_to="media/ptt", blank=True,null=True)

    def __str__(self):
        return self.Titulo


class NOTICIA(models.Model):
    Titulo=models.CharField(max_length=200, blank=False)
    Descricao=models.CharField(max_length=200, blank=True,null=True)
    fotos=models.FileField(upload_to="media/noticia", blank=True,null=True)
    data=models.DateField()


    def __str__(self):
        return self.Titulo