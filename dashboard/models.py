from django.db import models

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Acta(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    month = models.IntegerField()
    year = models.IntegerField()
    indicador = models.ForeignKey('Indicador', models.DO_NOTHING)
    contrato = models.ForeignKey('Contrato', models.DO_NOTHING)
    gerente = models.ForeignKey('Gerente', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'acta'


class Campo(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    name = models.CharField(max_length=15)
    territorio = models.ForeignKey('Territorio', models.DO_NOTHING)
    operador = models.ForeignKey('Operador', models.DO_NOTHING)
    crudo_name = models.ForeignKey('Crudo', models.DO_NOTHING, db_column='crudo_name')

    class Meta:
        managed = True
        db_table = 'campo'

    def __str__(self):
        return f'{self.name}'


class Carrotanque(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    capacidad_litros = models.IntegerField()
    territorio = models.ForeignKey('Territorio', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'carrotanque'

    def __str__(self):
        return f'{self.id}'


class Contratista(models.Model):
    empleado = models.ForeignKey('Empleado', models.DO_NOTHING)
    supervisor = models.ForeignKey('Supervisor', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'contratista'


class Contrato(models.Model):
    id = models.IntegerField(primary_key=True)
    fecha_vigencia = models.CharField(max_length=10)
    fecha_caducidad = models.CharField(max_length=10)

    class Meta:
        managed = True
        db_table = 'contrato'


class Crudo(models.Model):
    name = models.CharField(primary_key=True, max_length=15)
    gravedad = models.FloatField()
    porcentaje_azufre = models.FloatField()
    precio_promedio = models.IntegerField()
    equivalencia_brent = models.FloatField()

    class Meta:
        managed = True
        db_table = 'crudo'
    def __str__(self):
        return f'{self.name}'


class Departamento(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    name = models.CharField(max_length=25)
    area = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'departamento'


class Empleado(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    sexo = models.CharField(max_length=1)
    fecha_ingreso = models.CharField(max_length=10)
    nacimiento = models.CharField(max_length=10)
    salario = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'empleado'


class Factura(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    valor = models.FloatField()
    cantidad_barriles_kbpd = models.FloatField()
    porcentaje_produccion = models.IntegerField()
    campo = models.ForeignKey(Campo, on_delete = models.CASCADE, null=False)
    acta = models.ForeignKey(Acta, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'factura'


class Gerente(models.Model):
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING)
    firma = models.CharField(max_length=8)

    class Meta:
        managed = True
        db_table = 'gerente'


class HistoriaCarrotanque(models.Model):
    id = models.AutoField(primary_key=True)
    carrotanque_id = models.CharField(max_length=6)
    territorio = models.CharField(max_length=20, blank=True, null=True)
    territorio_id = models.CharField(max_length=6, blank=True, null=True)
    fecha_asignacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'historia_carrotanque'


class Indicador(models.Model):
    id = models.IntegerField(primary_key=True)
    brent = models.FloatField()
    trm = models.FloatField()

    class Meta:
        managed = True
        db_table = 'indicador'


class Oleoducto(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    name = models.CharField(max_length=10)

    class Meta:
        managed = True
        db_table = 'oleoducto'


class OleoductoAtraviesa(models.Model):
    id = models.AutoField(primary_key=True)
    oleoducto = models.ForeignKey(Oleoducto, models.DO_NOTHING)
    territorio = models.ForeignKey('Territorio', models.DO_NOTHING)
    estacion = models.CharField(max_length=15)

    class Meta:
        managed = True
        db_table = 'oleoducto_atraviesa'


class Operador(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    name = models.CharField(max_length=15)

    class Meta:
        managed = True
        db_table = 'operador'
        
    def __str__(self):
        return f'{self.name}'

class Puerto(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    name = models.CharField(max_length=15)
    territorio = models.ForeignKey('Territorio', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'puerto'


class Refineria(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    name = models.CharField(max_length=15)
    capacidad_kbpd = models.CharField(max_length=3)
    territorio = models.ForeignKey('Territorio', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'refineria'


class Supervisor(models.Model):
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING)
    departamento = models.ForeignKey(Departamento, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'supervisor'


class Territorio(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    name = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'territorio'

    def __str__(self):
        return f'{self.name}'