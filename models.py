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
        managed = False
        db_table = 'acta'


class Campo(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    name = models.CharField(max_length=15)
    territorio = models.ForeignKey('Territorio', models.DO_NOTHING)
    operador = models.ForeignKey('Operador', models.DO_NOTHING)
    crudo_name = models.ForeignKey('Crudo', models.DO_NOTHING, db_column='crudo_name')

    class Meta:
        managed = False
        db_table = 'campo'


class Carrotanque(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    capacidad_litros = models.IntegerField()
    territorio = models.ForeignKey('Territorio', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'carrotanque'


class Contratista(models.Model):
    empleado = models.ForeignKey('Empleado', models.DO_NOTHING)
    supervisor = models.ForeignKey('Supervisor', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'contratista'


class Contrato(models.Model):
    id = models.IntegerField(primary_key=True)
    fecha_vigencia = models.CharField(max_length=10)
    fecha_caducidad = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'contrato'


class Crudo(models.Model):
    name = models.CharField(primary_key=True, max_length=15)
    gravedad = models.FloatField()
    porcentaje_azufre = models.FloatField()
    precio_promedio = models.IntegerField()
    equivalencia_brent = models.FloatField()

    class Meta:
        managed = False
        db_table = 'crudo'


class Departamento(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    name = models.CharField(max_length=25)
    area = models.CharField(max_length=30)

    class Meta:
        managed = False
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
        managed = False
        db_table = 'empleado'


class Factura(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    valor = models.FloatField()
    cantidad_barriles_kbpd = models.FloatField()
    porcentaje_produccion = models.IntegerField()
    campo = models.ForeignKey(Campo, models.DO_NOTHING)
    acta = models.ForeignKey(Acta, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factura'


class Gerente(models.Model):
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING)
    firma = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'gerente'


class HistoriaCarrotanque(models.Model):
    carrotanque_id = models.CharField(max_length=6)
    territorio = models.CharField(max_length=20, blank=True, null=True)
    territorio_id = models.CharField(max_length=6, blank=True, null=True)
    fecha_asignacion = models.DateField(blank=True, null=True)
    empleado = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historia_carrotanque'


class Indicador(models.Model):
    id = models.IntegerField(primary_key=True)
    brent = models.FloatField()
    trm = models.FloatField()

    class Meta:
        managed = False
        db_table = 'indicador'


class Oleoducto(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'oleoducto'


class OleoductoAtraviesa(models.Model):
    oleoducto = models.ForeignKey(Oleoducto, models.DO_NOTHING)
    territorio = models.ForeignKey('Territorio', models.DO_NOTHING)
    estacion = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'oleoducto_atraviesa'


class Operador(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    name = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'operador'


class Puerto(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    name = models.CharField(max_length=15)
    territorio = models.ForeignKey('Territorio', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'puerto'


class Refineria(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    name = models.CharField(max_length=15)
    capacidad_kbpd = models.CharField(max_length=3)
    territorio = models.ForeignKey('Territorio', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'refineria'


class Supervisor(models.Model):
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING)
    departamento = models.ForeignKey(Departamento, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'supervisor'


class Territorio(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'territorio'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
        

class UserProfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    cc = models.IntegerField()
    position = models.CharField(max_length=20)
    image = models.CharField(max_length=100)
    profile = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_profile'