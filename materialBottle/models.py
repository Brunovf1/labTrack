from tabnanny import verbose
from django.db import models

# Create your models here.

# class MyModel(models.Model):
#     name = models.CharField(max_length=250)


class Bottle(models.Model):
    BOTTLE_JAR = "Garrafa"
    BOTTlE_SYRINGE = "Seringa"
    BOTTLE_TYPES = [(BOTTLE_JAR,"Garrafa Ambar 1l"),
                    (BOTTlE_SYRINGE, "Seringa 50ml")]
    tag = models.CharField(max_length=8, unique=True)
    bt_type = models.CharField(choices=BOTTLE_TYPES,max_length=40)

    def __str__(self):
        return str(self.bt_type) +" "+ str(self.tag)

class Machine(models.Model):
    tag = models.CharField(max_length=8, unique=True)
    name = models.CharField(max_length=8)

    def __str__(self):
        return str(self.name)

class Batch(models.Model):
    code = models.CharField(unique=True, max_length=8)
    def __str__(self):
        return str(self.code)

class Sample(models.Model):
    SAMPLE_GAS = "GAS"
    SAMPLE_FQ = "Fisio-Quimi"
    SAMPLE_2Fal = "2Fal"
    SAMPLE_TYPE = [(SAMPLE_GAS,"Amostra para Analise de Gases"),
                   (SAMPLE_FQ,"Amostra para Analise de Fisico-Quimica"),
                   (SAMPLE_2Fal,"Amostra para Analise 2Fal")]


    sp_bottle = models.ForeignKey(Bottle, on_delete=models.SET_NULL ,null=True, blank=True)
    sp_machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    sp_batch = models.ForeignKey(Batch, on_delete=models.CASCADE)


    sp_type = models.CharField(choices=SAMPLE_TYPE, max_length=40)
    sp_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Material para analise de "+str(self.sp_type) +" na maquina"+ str(self.sp_machine)