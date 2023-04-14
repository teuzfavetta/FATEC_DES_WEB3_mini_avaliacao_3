from django.db import models

class FeriadoModel(models.Model):
    nome = models.CharField('Feriado',max_length=60)
    dia = models.IntegerField('Data')
    mes = models.IntegerField('Mês')

    modificado_em = models.DateTimeField(
        verbose_name='Foi modificado em: ',
        auto_now_add=False, auto_now=True
    )

    def __str__(self):
        return self.nome