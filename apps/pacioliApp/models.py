#from django.db import models
# Create your models here.
#---------------------------------------------------
#-------------------------------------------------

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
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
    action_flag = models.SmallIntegerField()
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


class PgActivo(models.Model):
    ccod_acti = models.CharField(max_length=10, blank=True, null=True)
    cdsc = models.CharField(max_length=40, blank=True, null=True)
    ffecha_ad = models.DateField(blank=True, null=True)
    lestado = models.BooleanField(blank=True, null=True)
    ffecha_ba = models.DateField(blank=True, null=True)
    cubicacion = models.CharField(max_length=30, blank=True, null=True)
    ccod_costo = models.CharField(max_length=9, blank=True, null=True)
    nmeses = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    ntasadep = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nvalor = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nresidual = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndepre = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ccod_cue = models.CharField(max_length=10, blank=True, null=True)
    ccue_dep = models.CharField(max_length=10, blank=True, null=True)
    ccue_gas = models.CharField(max_length=10, blank=True, null=True)
    ndep1 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndep2 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndep3 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndep4 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndep5 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndep6 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndep7 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndep8 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndep9 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndep10 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndep11 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndep12 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    najus1 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    najus2 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ldepre = models.BooleanField(blank=True, null=True)
    mdsc = models.CharField(max_length=500, blank=True, null=True)
    ccod_presu = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_activo'


class PgAdicion(models.Model):
    ncod = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    cdsc = models.CharField(max_length=200, blank=True, null=True)
    npot1 = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cdetalle = models.CharField(max_length=2, blank=True, null=True)
    nextraer = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nfiltrado = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ncontable = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ncalculo = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ntributa = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nadicion = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npot2 = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_adicion'


class PgAsicab(models.Model):
    ccod_asi = models.CharField(max_length=5, blank=True, null=True)
    cid = models.CharField(max_length=8, blank=True, null=True)
    cdsc = models.CharField(max_length=30, blank=True, null=True)
    cdebe = models.CharField(max_length=10, blank=True, null=True)
    chaber = models.CharField(max_length=10, blank=True, null=True)
    lrango = models.BooleanField(blank=True, null=True)
    nubic = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    lpedir = models.BooleanField(blank=True, null=True)
    nitem = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    cformula = models.CharField(max_length=250, blank=True, null=True)
    lcancela = models.BooleanField(blank=True, null=True)
    lcaja = models.BooleanField(blank=True, null=True)
    ntipocam = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    ldifcam = models.BooleanField(blank=True, null=True)
    ccod_doc = models.CharField(max_length=2, blank=True, null=True)
    cnumero = models.CharField(max_length=12, blank=True, null=True)
    ccod_cli = models.CharField(max_length=11, blank=True, null=True)
    ccod_costo = models.CharField(max_length=9, blank=True, null=True)
    cglosa = models.CharField(max_length=30, blank=True, null=True)
    ffechadoc = models.DateField(blank=True, null=True)
    ffechaven = models.DateField(blank=True, null=True)
    lautoinc = models.BooleanField(blank=True, null=True)
    cserinc = models.CharField(max_length=6, blank=True, null=True)
    cdocinc = models.CharField(max_length=2, blank=True, null=True)
    ccod_flujo = models.CharField(max_length=4, blank=True, null=True)
    ldespliega = models.BooleanField(blank=True, null=True)
    cdatregesp = models.CharField(max_length=5, blank=True, null=True)
    cdatdoc = models.CharField(max_length=5, blank=True, null=True)
    lresp = models.BooleanField(blank=True, null=True)
    lcobesp = models.BooleanField(blank=True, null=True)
    cdatcosto = models.CharField(max_length=5, blank=True, null=True)
    ccod_pagsu = models.CharField(max_length=3, blank=True, null=True)
    ccod_camp1 = models.CharField(max_length=3, blank=True, null=True)
    ccod_camp2 = models.CharField(max_length=3, blank=True, null=True)
    ccod_presu = models.CharField(max_length=10, blank=True, null=True)
    lmostrar = models.BooleanField(blank=True, null=True)
    ccod_vend = models.CharField(max_length=4, blank=True, null=True)
    ccod_cos2 = models.CharField(max_length=9, blank=True, null=True)
    ccod_clabs = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_asicab'


class PgAsidet(models.Model):
    cid = models.CharField(max_length=8, blank=True, null=True)
    npor = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    ccod_asi = models.CharField(max_length=5, blank=True, null=True)
    ccod_cue = models.CharField(max_length=10, blank=True, null=True)
    ccod_costo = models.CharField(max_length=9, blank=True, null=True)
    cformula = models.CharField(max_length=250, blank=True, null=True)
    ccod_presu = models.CharField(max_length=10, blank=True, null=True)
    ccod_cos2 = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_asidet'


class PgAsiento(models.Model):
    ccod_asi = models.CharField(max_length=5, blank=True, null=True)
    cdsc = models.CharField(max_length=60, blank=True, null=True)
    ccod_ori = models.CharField(max_length=2, blank=True, null=True)
    cglosa = models.CharField(max_length=30, blank=True, null=True)
    cregis = models.CharField(max_length=1, blank=True, null=True)
    limp = models.BooleanField(blank=True, null=True)
    ccod_rep = models.CharField(max_length=5, blank=True, null=True)
    mdsc = models.CharField(max_length=500, blank=True, null=True)
    cdesenc = models.CharField(max_length=5, blank=True, null=True)
    t2008_8 = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_asiento'


class PgAsimodel(models.Model):
    cmes = models.CharField(max_length=2, blank=True, null=True)
    nasiento = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    ccod_cue = models.CharField(max_length=10, blank=True, null=True)
    ndebe = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    cglosa = models.CharField(max_length=60, blank=True, null=True)
    ccod_ori = models.CharField(max_length=2, blank=True, null=True)
    cregis = models.CharField(max_length=1, blank=True, null=True)
    ffecha = models.DateField(blank=True, null=True)
    ffechadoc = models.DateField(blank=True, null=True)
    cnumero = models.CharField(max_length=20, blank=True, null=True)
    ffechaven = models.DateField(blank=True, null=True)
    ccod_doc = models.CharField(max_length=2, blank=True, null=True)
    ccod_cli = models.CharField(max_length=11, blank=True, null=True)
    nina = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nexo = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nnet = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nimp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ntot = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ccod_user = models.CharField(max_length=4, blank=True, null=True)
    ffechareg = models.DateField(blank=True, null=True)
    cmesc = models.CharField(max_length=2, blank=True, null=True)
    cdestino = models.CharField(max_length=3, blank=True, null=True)
    cdes = models.CharField(max_length=1, blank=True, null=True)
    ccod_costo = models.CharField(max_length=9, blank=True, null=True)
    cmoneda = models.CharField(max_length=1, blank=True, null=True)
    ntc = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    ndebed = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ninad = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nexod = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nnetd = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nimpd = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ntotd = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    cmreg = models.CharField(max_length=1, blank=True, null=True)
    lcomp = models.BooleanField(blank=True, null=True)
    ntcc = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    ncajas = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ncajad = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    lajusdif = models.BooleanField(blank=True, null=True)
    lcaja = models.BooleanField(blank=True, null=True)
    cid = models.CharField(max_length=10, blank=True, null=True)
    ccod_asi = models.CharField(max_length=5, blank=True, null=True)
    ccadpdt = models.CharField(max_length=60, blank=True, null=True)
    ccod_flujo = models.CharField(max_length=4, blank=True, null=True)
    nbase2 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nigv2 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nbase3 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nigv3 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nisc = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nbase2d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nigv2d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nbase3d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nigv3d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    niscd = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    lresp = models.BooleanField(blank=True, null=True)
    nresp = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    nporresp = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cserresp = models.CharField(max_length=6, blank=True, null=True)
    cnumresp = models.CharField(max_length=15, blank=True, null=True)
    fguiaresp = models.DateField(blank=True, null=True)
    cserguia = models.CharField(max_length=6, blank=True, null=True)
    cnumguia = models.CharField(max_length=13, blank=True, null=True)
    nrets = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nretd = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    cdocf = models.CharField(max_length=2, blank=True, null=True)
    cnumf = models.CharField(max_length=20, blank=True, null=True)
    ffecf = models.DateField(blank=True, null=True)
    fdocdet = models.DateField(blank=True, null=True)
    cdoc_ndom = models.CharField(max_length=20, blank=True, null=True)
    cdoc_refnc = models.CharField(max_length=20, blank=True, null=True)
    fpagimpret = models.DateField(blank=True, null=True)
    fpagimport = models.DateField(blank=True, null=True)
    ldiferido = models.BooleanField(blank=True, null=True)
    ffechadif = models.DateField(blank=True, null=True)
    ccod_pagsu = models.CharField(max_length=3, blank=True, null=True)
    ccod_camp1 = models.CharField(max_length=3, blank=True, null=True)
    ccod_camp2 = models.CharField(max_length=3, blank=True, null=True)
    t2008_11 = models.CharField(max_length=3, blank=True, null=True)
    ffecdua = models.DateField(blank=True, null=True)
    t2008_8 = models.CharField(max_length=2, blank=True, null=True)
    ccod_presu = models.CharField(max_length=10, blank=True, null=True)
    cdocmodi = models.CharField(max_length=2, blank=True, null=True)
    cserext = models.CharField(max_length=20, blank=True, null=True)
    cnumext = models.CharField(max_length=20, blank=True, null=True)
    ncoddes = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    nnumdes = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cnumdet = models.CharField(max_length=8, blank=True, null=True)
    cexttpo = models.CharField(max_length=2, blank=True, null=True)
    cextser = models.CharField(max_length=10, blank=True, null=True)
    cextnum = models.CharField(max_length=20, blank=True, null=True)
    fextfec = models.DateField(blank=True, null=True)
    nextbas = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nextigv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    cperser = models.CharField(max_length=4, blank=True, null=True)
    cpernum = models.CharField(max_length=15, blank=True, null=True)
    ntpcv = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    dua_año = models.CharField(db_column='dua_aÑo', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dua_num = models.CharField(max_length=6, blank=True, null=True)
    dua_fregu = models.DateField(blank=True, null=True)
    dua_valor = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ccod_vend = models.CharField(max_length=4, blank=True, null=True)
    cdocc = models.CharField(max_length=2, blank=True, null=True)
    cnumc = models.CharField(max_length=20, blank=True, null=True)
    ccod_user1 = models.CharField(max_length=4, blank=True, null=True)
    ffechareg1 = models.DateField(blank=True, null=True)
    nestado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    ccod_cos2 = models.CharField(max_length=9, blank=True, null=True)
    cmesple = models.CharField(max_length=1, blank=True, null=True)
    coriple = models.CharField(max_length=2, blank=True, null=True)
    nasiple = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ccodruc = models.CharField(max_length=11, blank=True, null=True)
    npigv = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cglosa2 = models.CharField(max_length=60, blank=True, null=True)
    cregpdb = models.CharField(max_length=2, blank=True, null=True)
    ctpcv = models.CharField(max_length=1, blank=True, null=True)
    ccoddes = models.CharField(max_length=1, blank=True, null=True)
    cnumdes = models.CharField(max_length=1, blank=True, null=True)
    cinddet = models.CharField(max_length=1, blank=True, null=True)
    ccoddet = models.CharField(max_length=5, blank=True, null=True)
    cindret = models.CharField(max_length=1, blank=True, null=True)
    cperind = models.CharField(max_length=1, blank=True, null=True)
    cpercod = models.CharField(max_length=2, blank=True, null=True)
    cref = models.CharField(max_length=1, blank=True, null=True)
    cmle = models.CharField(max_length=2, blank=True, null=True)
    cale = models.CharField(max_length=4, blank=True, null=True)
    ncorrelat = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    cnumero2 = models.CharField(max_length=13, blank=True, null=True)
    ncorrecb = models.CharField(max_length=1, blank=True, null=True)
    cmle2 = models.CharField(max_length=2, blank=True, null=True)
    cale2 = models.CharField(max_length=4, blank=True, null=True)
    lperden = models.BooleanField(blank=True, null=True)
    nmonperbas = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ccorre40 = models.CharField(max_length=6, blank=True, null=True)
    nrentanet = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nimpreten = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndeduc = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ntasreten = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    ccod_renta = models.CharField(max_length=2, blank=True, null=True)
    ccod_mone = models.CharField(max_length=3, blank=True, null=True)
    ntcamsnd = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_asimodel'


class PgAsiuser(models.Model):
    ccod_asi = models.CharField(max_length=5, blank=True, null=True)
    ccod_user = models.CharField(max_length=4, blank=True, null=True)
    lblotc = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_asiuser'


class PgCampat1(models.Model):
    ccod_camp = models.CharField(max_length=3, blank=True, null=True)
    cdsc = models.CharField(max_length=100, blank=True, null=True)
    ccod_csev = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_campat1'


class PgCampat2(models.Model):
    ccod_camp = models.CharField(max_length=3, blank=True, null=True)
    cdsc = models.CharField(max_length=100, blank=True, null=True)
    ccod_csev = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_campat2'


class PgCatesfin(models.Model):
    ccod_catef = models.CharField(max_length=2, blank=True, null=True)
    cdsc = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_catesfin'


class PgCieCaja(models.Model):
    ccod_cue = models.CharField(max_length=10, blank=True, null=True)
    ffecha = models.DateField(blank=True, null=True)
    nmonto = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmontod = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_cie_caja'


class PgCierre(models.Model):
    ffecha = models.DateField(blank=True, null=True)
    lcierre = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_cierre'


class PgClabieser(models.Model):
    ccod_clabs = models.CharField(max_length=1, blank=True, null=True)
    cdsc = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_clabieser'


class PgCliPro(models.Model):
    ccod_cli = models.CharField(max_length=11, blank=True, null=True)
    crazon = models.CharField(max_length=100, blank=True, null=True)
    cdir = models.CharField(max_length=150, blank=True, null=True)
    ctel = models.CharField(max_length=20, blank=True, null=True)
    ntipo = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    nsaldo = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nsaldod = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ccod_tip = models.CharField(max_length=3, blank=True, null=True)
    nlimites = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nlimited = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    cpaterno = models.CharField(max_length=20, blank=True, null=True)
    cmaterno = models.CharField(max_length=20, blank=True, null=True)
    cnombre1 = models.CharField(max_length=20, blank=True, null=True)
    cnombre2 = models.CharField(max_length=20, blank=True, null=True)
    nnatjur = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    ntipodoc = models.CharField(max_length=1, blank=True, null=True)
    lbuenc = models.BooleanField(blank=True, null=True)
    lagret = models.BooleanField(blank=True, null=True)
    lagper = models.BooleanField(blank=True, null=True)
    lmoroso = models.BooleanField(blank=True, null=True)
    nlimiadi = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nlimiadid = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    lanulado = models.BooleanField(blank=True, null=True)
    lhabi = models.BooleanField(blank=True, null=True)
    lnohabi = models.BooleanField(blank=True, null=True)
    lnohalla = models.BooleanField(blank=True, null=True)
    ccod_pais = models.CharField(max_length=4, blank=True, null=True)
    ccod_conve = models.CharField(max_length=2, blank=True, null=True)
    cncomer = models.CharField(max_length=80, blank=True, null=True)
    npenlims = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npenlimd = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_cli_pro'


class PgCliProno(models.Model):
    ccod_ite = models.CharField(max_length=10, blank=True, null=True)
    ccod_cli = models.CharField(max_length=11, blank=True, null=True)
    ccod_con = models.CharField(max_length=2, blank=True, null=True)
    ffec_ini = models.DateField(blank=True, null=True)
    ffec_fin = models.DateField(blank=True, null=True)
    ccod_mes = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_cli_prono'


class PgComncxml(models.Model):
    ccod_doc = models.CharField(max_length=2, blank=True, null=True)
    ccod_cli = models.CharField(max_length=11, blank=True, null=True)
    cser = models.CharField(max_length=6, blank=True, null=True)
    cnum = models.CharField(max_length=13, blank=True, null=True)
    ffechadoc = models.DateField(blank=True, null=True)
    ntot = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    crazsoc = models.CharField(max_length=100, blank=True, null=True)
    mobser = models.CharField(max_length=500, blank=True, null=True)
    carchivo = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_comncxml'


class PgComxml(models.Model):
    ccod_doc = models.CharField(max_length=2, blank=True, null=True)
    ccod_cli = models.CharField(max_length=11, blank=True, null=True)
    cser = models.CharField(max_length=6, blank=True, null=True)
    cnum = models.CharField(max_length=13, blank=True, null=True)
    ffechadoc = models.DateField(blank=True, null=True)
    ntot = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nestado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cresusunat = models.CharField(max_length=254, blank=True, null=True)
    crazsoc = models.CharField(max_length=100, blank=True, null=True)
    cmes = models.CharField(max_length=2, blank=True, null=True)
    ctot = models.CharField(max_length=20, blank=True, null=True)
    mobser = models.CharField(max_length=500, blank=True, null=True)
    carchivo = models.CharField(max_length=254, blank=True, null=True)
    nfase = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_comxml'


class PgConsisple(models.Model):
    canio = models.CharField(max_length=4, blank=True, null=True)
    ccod = models.CharField(max_length=6, blank=True, null=True)
    cdsc = models.CharField(max_length=254, blank=True, null=True)
    nmes01 = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    nmes02 = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    nmes03 = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    nmes04 = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    nmes05 = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    nmes06 = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    nmes07 = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    nmes08 = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    nmes09 = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    nmes10 = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    nmes11 = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    nmes12 = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    mobser = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_consisple'


class PgContacto(models.Model):
    ccod_cli = models.CharField(max_length=11, blank=True, null=True)
    mobs_emp = models.CharField(max_length=500, blank=True, null=True)
    ccod_con = models.CharField(max_length=2, blank=True, null=True)
    cdes_con = models.CharField(max_length=50, blank=True, null=True)
    ccar_con = models.CharField(max_length=50, blank=True, null=True)
    ctel_con = models.CharField(max_length=80, blank=True, null=True)
    cmai_con = models.CharField(max_length=80, blank=True, null=True)
    mobs_con = models.CharField(max_length=500, blank=True, null=True)
    ldefecto = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_contacto'


class PgConveniodt(models.Model):
    ccod_conve = models.CharField(max_length=2, blank=True, null=True)
    cdsc = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_conveniodt'


class PgCostos(models.Model):
    ccod_costo = models.CharField(max_length=9, blank=True, null=True)
    cdsc = models.CharField(max_length=100, blank=True, null=True)
    cdebe = models.CharField(max_length=10, blank=True, null=True)
    chaber = models.CharField(max_length=10, blank=True, null=True)
    lbloquea = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_costos'


class PgCostos2(models.Model):
    ccod_costo = models.CharField(max_length=9, blank=True, null=True)
    cdsc = models.CharField(max_length=100, blank=True, null=True)
    cdebe = models.CharField(max_length=10, blank=True, null=True)
    chaber = models.CharField(max_length=10, blank=True, null=True)
    lbloquea = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_costos2'


class PgCtabanco(models.Model):
    citecod = models.CharField(max_length=3, blank=True, null=True)
    nempcli = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    ccod_ac = models.CharField(max_length=2, blank=True, null=True)
    cctacod = models.CharField(max_length=3, blank=True, null=True)
    cctanum = models.CharField(max_length=30, blank=True, null=True)
    nctamon = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cempcod = models.CharField(max_length=10, blank=True, null=True)
    cempdt1 = models.CharField(max_length=10, blank=True, null=True)
    cempdt2 = models.CharField(max_length=10, blank=True, null=True)
    ccod_cli = models.CharField(max_length=11, blank=True, null=True)
    cclidt1 = models.CharField(max_length=10, blank=True, null=True)
    ffecini = models.DateField(blank=True, null=True)
    ffecfin = models.DateField(blank=True, null=True)
    cbanage = models.CharField(max_length=10, blank=True, null=True)
    nbanoks = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    nctaoks = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_ctabanco'


class PgCtrlple(models.Model):
    ncod = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    cdsc = models.CharField(max_length=200, blank=True, null=True)
    l1 = models.BooleanField(blank=True, null=True)
    l2 = models.BooleanField(blank=True, null=True)
    l3 = models.BooleanField(blank=True, null=True)
    l4 = models.BooleanField(blank=True, null=True)
    l5 = models.BooleanField(blank=True, null=True)
    l6 = models.BooleanField(blank=True, null=True)
    l7 = models.BooleanField(blank=True, null=True)
    l8 = models.BooleanField(blank=True, null=True)
    l9 = models.BooleanField(blank=True, null=True)
    l10 = models.BooleanField(blank=True, null=True)
    l11 = models.BooleanField(blank=True, null=True)
    l12 = models.BooleanField(blank=True, null=True)
    cmesple30 = models.CharField(max_length=2, blank=True, null=True)
    cperple30 = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_ctrlple'


class PgDiario(models.Model):
    cmes = models.CharField(max_length=2, blank=True, null=True)
    nasiento = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    ccod_cue = models.CharField(max_length=10, blank=True, null=True)
    ndebe = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    cglosa = models.CharField(max_length=60, blank=True, null=True)
    ccod_ori = models.CharField(max_length=2, blank=True, null=True)
    cregis = models.CharField(max_length=1, blank=True, null=True)
    ffecha = models.DateField(blank=True, null=True)
    ffechadoc = models.DateField(blank=True, null=True)
    cnumero = models.CharField(max_length=20, blank=True, null=True)
    ffechaven = models.DateField(blank=True, null=True)
    ccod_doc = models.CharField(max_length=2, blank=True, null=True)
    ccod_cli = models.CharField(max_length=11, blank=True, null=True)
    nina = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nexo = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nnet = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nimp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ntot = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ccod_user = models.CharField(max_length=4, blank=True, null=True)
    ffechareg = models.DateField(blank=True, null=True)
    cmesc = models.CharField(max_length=2, blank=True, null=True)
    cdestino = models.CharField(max_length=3, blank=True, null=True)
    cdes = models.CharField(max_length=1, blank=True, null=True)
    ccod_costo = models.CharField(max_length=9, blank=True, null=True)
    cmoneda = models.CharField(max_length=1, blank=True, null=True)
    ntc = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    ndebed = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ninad = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nexod = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nnetd = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nimpd = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ntotd = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    cmreg = models.CharField(max_length=1, blank=True, null=True)
    lcomp = models.BooleanField(blank=True, null=True)
    ntcc = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    ncajas = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ncajad = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    lajusdif = models.BooleanField(blank=True, null=True)
    lcaja = models.BooleanField(blank=True, null=True)
    cid = models.CharField(max_length=10, blank=True, null=True)
    ccod_asi = models.CharField(max_length=5, blank=True, null=True)
    ccadpdt = models.CharField(max_length=60, blank=True, null=True)
    ccod_flujo = models.CharField(max_length=4, blank=True, null=True)
    nbase2 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nigv2 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nbase3 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nigv3 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nisc = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nbase2d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nigv2d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nbase3d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nigv3d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    niscd = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    lresp = models.BooleanField(blank=True, null=True)
    nresp = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    nporresp = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cserresp = models.CharField(max_length=6, blank=True, null=True)
    cnumresp = models.CharField(max_length=15, blank=True, null=True)
    fguiaresp = models.DateField(blank=True, null=True)
    cserguia = models.CharField(max_length=6, blank=True, null=True)
    cnumguia = models.CharField(max_length=13, blank=True, null=True)
    nrets = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nretd = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    cdocf = models.CharField(max_length=2, blank=True, null=True)
    cnumf = models.CharField(max_length=20, blank=True, null=True)
    ffecf = models.DateField(blank=True, null=True)
    fdocdet = models.DateField(blank=True, null=True)
    cdoc_ndom = models.CharField(max_length=20, blank=True, null=True)
    cdoc_refnc = models.CharField(max_length=20, blank=True, null=True)
    fpagimpret = models.DateField(blank=True, null=True)
    fpagimport = models.DateField(blank=True, null=True)
    ldiferido = models.BooleanField(blank=True, null=True)
    ffechadif = models.DateField(blank=True, null=True)
    ccod_pagsu = models.CharField(max_length=3, blank=True, null=True)
    ccod_camp1 = models.CharField(max_length=3, blank=True, null=True)
    ccod_camp2 = models.CharField(max_length=3, blank=True, null=True)
    t2008_11 = models.CharField(max_length=3, blank=True, null=True)
    ffecdua = models.DateField(blank=True, null=True)
    t2008_8 = models.CharField(max_length=2, blank=True, null=True)
    ccod_presu = models.CharField(max_length=10, blank=True, null=True)
    cdocmodi = models.CharField(max_length=2, blank=True, null=True)
    cserext = models.CharField(max_length=20, blank=True, null=True)
    cnumext = models.CharField(max_length=20, blank=True, null=True)
    ncoddes = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    nnumdes = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cnumdet = models.CharField(max_length=8, blank=True, null=True)
    cexttpo = models.CharField(max_length=2, blank=True, null=True)
    cextser = models.CharField(max_length=10, blank=True, null=True)
    cextnum = models.CharField(max_length=20, blank=True, null=True)
    fextfec = models.DateField(blank=True, null=True)
    nextbas = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nextigv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    cperser = models.CharField(max_length=4, blank=True, null=True)
    cpernum = models.CharField(max_length=15, blank=True, null=True)
    ntpcv = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    dua_año = models.CharField(db_column='dua_aÑo', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dua_num = models.CharField(max_length=6, blank=True, null=True)
    dua_fregu = models.DateField(blank=True, null=True)
    dua_valor = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ccod_vend = models.CharField(max_length=4, blank=True, null=True)
    cdocc = models.CharField(max_length=2, blank=True, null=True)
    cnumc = models.CharField(max_length=20, blank=True, null=True)
    ccod_user1 = models.CharField(max_length=4, blank=True, null=True)
    ffechareg1 = models.DateField(blank=True, null=True)
    nestado = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    ccod_cos2 = models.CharField(max_length=9, blank=True, null=True)
    cmesple = models.CharField(max_length=1, blank=True, null=True)
    coriple = models.CharField(max_length=2, blank=True, null=True)
    nasiple = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ccodruc = models.CharField(max_length=11, blank=True, null=True)
    npigv = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cglosa2 = models.CharField(max_length=60, blank=True, null=True)
    cregpdb = models.CharField(max_length=2, blank=True, null=True)
    ctpcv = models.CharField(max_length=1, blank=True, null=True)
    ccoddes = models.CharField(max_length=1, blank=True, null=True)
    cnumdes = models.CharField(max_length=1, blank=True, null=True)
    cinddet = models.CharField(max_length=1, blank=True, null=True)
    ccoddet = models.CharField(max_length=5, blank=True, null=True)
    cindret = models.CharField(max_length=1, blank=True, null=True)
    cperind = models.CharField(max_length=1, blank=True, null=True)
    cpercod = models.CharField(max_length=2, blank=True, null=True)
    cref = models.CharField(max_length=1, blank=True, null=True)
    cmle = models.CharField(max_length=2, blank=True, null=True)
    cale = models.CharField(max_length=4, blank=True, null=True)
    ncorrelat = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    cnumero2 = models.CharField(max_length=13, blank=True, null=True)
    ncorrecb = models.CharField(max_length=1, blank=True, null=True)
    cmle2 = models.CharField(max_length=2, blank=True, null=True)
    cale2 = models.CharField(max_length=4, blank=True, null=True)
    lperden = models.BooleanField(blank=True, null=True)
    nmonperbas = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ccorre40 = models.CharField(max_length=6, blank=True, null=True)
    nrentanet = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nimpreten = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndeduc = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ntasreten = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    ccod_renta = models.CharField(max_length=2, blank=True, null=True)
    ccod_mone = models.CharField(max_length=3, blank=True, null=True)
    ntcamsnd = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_diario'

    def __str__(self):
        return '{} {}'.format(self.nasiento , self.cglosa)


class PgDiariolibro(models.Model):
    ccod_cue = models.CharField(max_length=50, blank=True, null=True)
    ndebe = models.IntegerField(blank=True, null=True)
    nhaber = models.IntegerField(blank=True, null=True)
    cglosa = models.CharField(max_length=250, blank=True, null=True)
    ccod_ori = models.CharField(max_length=250, blank=True, null=True)
    nasiento = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_diariolibro'

    def __str__(self):
        return '{} {}'.format(self.nasiento , self.cglosa)


class PgDifdbf(models.Model):
    cdsc = models.CharField(max_length=200, blank=True, null=True)
    mes = models.CharField(max_length=3, blank=True, null=True)
    asiento = models.CharField(max_length=8, blank=True, null=True)
    origen = models.CharField(max_length=2, blank=True, null=True)
    moneda = models.CharField(max_length=10, blank=True, null=True)
    asiento2 = models.CharField(max_length=8, blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    cuenta = models.CharField(max_length=10, blank=True, null=True)
    diferen = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tipocam = models.DecimalField(max_digits=15, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_difdbf'


class PgDoc(models.Model):
    ccod_doc = models.CharField(max_length=2, blank=True, null=True)
    cdsc = models.CharField(max_length=252, blank=True, null=True)
    ligvc = models.BooleanField(blank=True, null=True)
    ligvv = models.BooleanField(blank=True, null=True)
    lcv = models.BooleanField(blank=True, null=True)
    lexp = models.BooleanField(blank=True, null=True)
    ccom_habc = models.CharField(max_length=10, blank=True, null=True)
    ccom_habr = models.CharField(max_length=10, blank=True, null=True)
    cven_debc = models.CharField(max_length=10, blank=True, null=True)
    cven_debr = models.CharField(max_length=10, blank=True, null=True)
    cven_hab = models.CharField(max_length=10, blank=True, null=True)
    nie = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    lneg = models.BooleanField(blank=True, null=True)
    limp = models.BooleanField(blank=True, null=True)
    nser = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    nnum = models.DecimalField(max_digits=7, decimal_places=0, blank=True, null=True)
    mpath = models.CharField(max_length=500, blank=True, null=True)
    ndocint = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_doc'


class PgEnfinan(models.Model):
    ccod_enfin = models.CharField(max_length=2, blank=True, null=True)
    cdsc = models.CharField(max_length=80, blank=True, null=True)
    mcuenta = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_enfinan'


class PgFactor(models.Model):
    nfac0 = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    nfac1 = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    nfac2 = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    nfac3 = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    nfac4 = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    nfac5 = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    nfac6 = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    nfac7 = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    nfac8 = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    nfac9 = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    nfac10 = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    nfac11 = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    nfac12 = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    ccod_cue = models.CharField(max_length=10, blank=True, null=True)
    ccod_ori = models.CharField(max_length=2, blank=True, null=True)
    cori_dep = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_factor'


class PgFlujo(models.Model):
    ccod_flujo = models.CharField(max_length=4, blank=True, null=True)
    cdsc = models.CharField(max_length=100, blank=True, null=True)
    ndebe0 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber0 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebe1 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber1 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebe2 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber2 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebe3 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber3 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebe4 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber4 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebe5 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber5 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebe6 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber6 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebe7 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber7 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebe8 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber8 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebe9 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber9 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebe10 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber10 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebe11 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber11 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebe12 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber12 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebe13 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber13 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebe14 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber14 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebe15 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber15 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebed0 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd0 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebed1 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd1 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebed2 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd2 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebed3 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd3 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebed4 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd4 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebed5 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd5 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebed6 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd6 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebed7 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd7 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebed8 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd8 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebed9 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd9 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebed10 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd10 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebed11 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd11 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebed12 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd12 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebed13 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd13 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebed14 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd14 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebed15 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd15 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    cformula = models.CharField(max_length=100, blank=True, null=True)
    ccod_csev = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_flujo'


class PgFormato(models.Model):
    ccod_bal = models.CharField(max_length=4, blank=True, null=True)
    cdsc = models.CharField(max_length=55, blank=True, null=True)
    ntipo = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cformula = models.CharField(max_length=100, blank=True, null=True)
    nimporte = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nimported = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    notas = models.CharField(max_length=20, blank=True, null=True)
    cnotac1 = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    cnotac2 = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    ccod_csev = models.CharField(max_length=6, blank=True, null=True)
    lconfig = models.BooleanField(blank=True, null=True)
    ccodpdt = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_formato'


class PgFormato2(models.Model):
    ccod_bal = models.CharField(max_length=4, blank=True, null=True)
    cdsc = models.CharField(max_length=55, blank=True, null=True)
    ntipo = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    cformula = models.CharField(max_length=100, blank=True, null=True)
    nimporte = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nimported = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    notas = models.CharField(max_length=20, blank=True, null=True)
    cnotac1 = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    cnotac2 = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    ccod_csev = models.CharField(max_length=6, blank=True, null=True)
    lconfig = models.BooleanField(blank=True, null=True)
    ccodpdt = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_formato2'


class PgFormato34(models.Model):
    ffecha = models.DateField(blank=True, null=True)
    cdsc = models.CharField(max_length=50, blank=True, null=True)
    ctipo = models.CharField(max_length=30, blank=True, null=True)
    ncontable = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    namort = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nneto = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ntotal = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    cmes = models.CharField(max_length=2, blank=True, null=True)
    ccod_ori = models.CharField(max_length=2, blank=True, null=True)
    ncorrlela = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    ccod_cue = models.CharField(max_length=10, blank=True, null=True)
    nasiento = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_formato34'


class PgFormato37(models.Model):
    ccod_pro = models.CharField(max_length=12, blank=True, null=True)
    ccodt5 = models.CharField(max_length=2, blank=True, null=True)
    cdsc5 = models.CharField(max_length=50, blank=True, null=True)
    cdsc = models.CharField(max_length=80, blank=True, null=True)
    ccodt6 = models.CharField(max_length=3, blank=True, null=True)
    cdsc6 = models.CharField(max_length=50, blank=True, null=True)
    nuni = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    npu = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    ntotal = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ccod_proca = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_formato37'


class PgFormato38(models.Model):
    ccod_doc = models.CharField(max_length=2, blank=True, null=True)
    cnumero = models.CharField(max_length=12, blank=True, null=True)
    crazon = models.CharField(max_length=60, blank=True, null=True)
    cdenomi = models.CharField(max_length=30, blank=True, null=True)
    nnominal = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npu = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ncantidad = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nlibros = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nprovis = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nneto = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ntotal = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    cmes = models.CharField(max_length=2, blank=True, null=True)
    ccod_ori = models.CharField(max_length=2, blank=True, null=True)
    ncorrlela = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    nasiento = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_formato38'


class PgFormato50(models.Model):
    nubic = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    ncapsoc = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nvalnomi = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nacsus = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    nacpag = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    nsocios = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    ctipodoc = models.CharField(max_length=2, blank=True, null=True)
    cnumero = models.CharField(max_length=20, blank=True, null=True)
    crazon = models.CharField(max_length=60, blank=True, null=True)
    ctipo = models.CharField(max_length=40, blank=True, null=True)
    naccion = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    npor = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    ccod_cli = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_formato50'


class PgFunciones(models.Model):
    ncodfun = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    cdetfun = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_funciones'


class PgHisCal(models.Model):
    ctpo_cal = models.CharField(max_length=3, blank=True, null=True)
    cmes = models.CharField(max_length=2, blank=True, null=True)
    nvalini = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nvalfin = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    najssal = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npagcta = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ntotigv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ffecha = models.DateField(blank=True, null=True)
    ntpoopc = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    ntpopor = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_his_cal'


class PgHistorial(models.Model):
    cdeshist = models.CharField(max_length=50, blank=True, null=True)
    mdethist = models.CharField(max_length=500, blank=True, null=True)
    ncodhist = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    ccondi = models.CharField(max_length=500, blank=True, null=True)
    cselec = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_historial'


class PgHistvenc(models.Model):
    ccod_cue = models.CharField(max_length=10, blank=True, null=True)
    ccod_cli = models.CharField(max_length=11, blank=True, null=True)
    ccod_doc = models.CharField(max_length=2, blank=True, null=True)
    cnumero = models.CharField(max_length=20, blank=True, null=True)
    ffechareg = models.DateField(blank=True, null=True)
    ffecharep = models.DateField(blank=True, null=True)
    tipreg = models.CharField(max_length=1, blank=True, null=True)
    ccoment = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_histvenc'


class PgMoneda(models.Model):
    ccod_mone = models.CharField(max_length=3, blank=True, null=True)
    cdsc = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_moneda'


class PgNumtick(models.Model):
    cmes = models.CharField(max_length=2, blank=True, null=True)
    ccod_ori = models.CharField(max_length=2, blank=True, null=True)
    nasiento = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    cnumtick = models.CharField(max_length=41, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_numtick'


class PgOrigen(models.Model):
    ccod_ori = models.CharField(max_length=2, blank=True, null=True)
    cdsc = models.CharField(max_length=70, blank=True, null=True)
    nnum0 = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    nnum1 = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    nnum2 = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    nnum3 = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    nnum4 = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    nnum5 = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    nnum6 = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    nnum7 = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    nnum8 = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    nnum9 = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    nnum10 = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    nnum11 = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    nnum12 = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    nnum13 = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    nnum14 = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    nnum15 = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    lmodi = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_origen'


class PgOrigenbc(models.Model):
    ccod_ori = models.CharField(max_length=2, blank=True, null=True)
    cdsc = models.CharField(max_length=70, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_origenbc'


class PgOrigenfi(models.Model):
    ccod_ac = models.CharField(max_length=2, blank=True, null=True)
    cdsc = models.CharField(max_length=50, blank=True, null=True)
    ccuenta = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_origenfi'


class PgPagsunat(models.Model):
    ccod_pagsu = models.CharField(max_length=3, blank=True, null=True)
    cdsc = models.CharField(max_length=90, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_pagsunat'


class PgPais(models.Model):
    ccod_pais = models.CharField(max_length=4, blank=True, null=True)
    cdsc = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_pais'

    def __str__(self):
        return '{} {}'.format(self.ccod_pais , self.cdsc)


class PgPlan(models.Model):
    ccod_cue = models.CharField(max_length=10, blank=True, null=True)
    cdsc = models.CharField(max_length=100, blank=True, null=True)
    nnivel = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    ntipo = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    nanalisis = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    ccod_bal = models.CharField(max_length=4, blank=True, null=True)
    cdes_d = models.CharField(max_length=10, blank=True, null=True)
    cdes_h = models.CharField(max_length=10, blank=True, null=True)
    ndebe0 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber0 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebe1 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber1 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebe2 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber2 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebe3 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber3 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebe4 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber4 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebe5 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber5 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebe6 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber6 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebe7 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber7 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebe8 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber8 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebe9 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber9 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebe10 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber10 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebe11 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber11 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebe12 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber12 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebe13 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber13 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebe14 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber14 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebe15 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber15 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nganper = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    ccue_acm = models.CharField(max_length=10, blank=True, null=True)
    ndebed0 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd0 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebed1 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd1 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebed2 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd2 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebed3 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd3 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebed4 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd4 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebed5 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd5 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebed6 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd6 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebed7 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd7 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebed8 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd8 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebed9 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd9 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebed10 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd10 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebed11 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd11 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebed12 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd12 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebed13 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd13 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebed14 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd14 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ndebed15 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd15 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ccod_baln = models.CharField(max_length=4, blank=True, null=True)
    ccod_bal2 = models.CharField(max_length=4, blank=True, null=True)
    ccod_baln2 = models.CharField(max_length=4, blank=True, null=True)
    lajusneg = models.BooleanField(blank=True, null=True)
    lexpsunat = models.BooleanField(blank=True, null=True)
    neducat = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    mdinamica = models.CharField(max_length=500, blank=True, null=True)
    ccod_enfin = models.CharField(max_length=2, blank=True, null=True)
    cnumcta = models.CharField(max_length=40, blank=True, null=True)
    cmoneda = models.CharField(max_length=1, blank=True, null=True)
    npresup = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    ccod_balr = models.CharField(max_length=4, blank=True, null=True)
    ccod_cueci = models.CharField(max_length=10, blank=True, null=True)
    cnocorr1 = models.CharField(max_length=10, blank=True, null=True)
    cnocorr2 = models.CharField(max_length=10, blank=True, null=True)
    lccadest = models.BooleanField(blank=True, null=True)
    lsaldosme = models.BooleanField(blank=True, null=True)
    cref = models.CharField(max_length=1, blank=True, null=True)
    cale = models.CharField(max_length=4, blank=True, null=True)
    cmle = models.CharField(max_length=2, blank=True, null=True)
    mesmod = models.CharField(max_length=2, blank=True, null=True)
    anomod = models.CharField(max_length=4, blank=True, null=True)
    lafecret = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_plan'

    def __str__(self):
        return '{} {}'.format(self.ccod_cue , self.cdsc)


class PgPlanrela(models.Model):
    ccod_tpla = models.CharField(max_length=3, blank=True, null=True)
    ccuenta = models.CharField(max_length=20, blank=True, null=True)
    cdsc = models.CharField(max_length=100, blank=True, null=True)
    ccod_cue = models.CharField(max_length=20, blank=True, null=True)
    nnivel = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_planrela'


class PgPlantipo(models.Model):
    ccod_tpla = models.CharField(max_length=3, blank=True, null=True)
    cdsc = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_plantipo'


class PgPorcen(models.Model):
    ccod_por = models.CharField(max_length=4, blank=True, null=True)
    cdsc = models.CharField(max_length=30, blank=True, null=True)
    npor = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_porcen'


class PgPresup(models.Model):
    ccod_presu = models.CharField(max_length=10, blank=True, null=True)
    cdsc = models.CharField(max_length=80, blank=True, null=True)
    ntipo = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    ngrupo = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    npe1 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo1 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop1 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe2 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo2 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop2 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe3 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo3 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop3 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe4 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo4 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop4 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe5 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo5 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop5 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe6 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo6 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop6 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe7 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo7 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop7 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe8 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo8 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop8 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe9 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo9 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop9 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe10 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo10 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop10 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe11 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo11 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop11 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe12 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo12 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop12 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    cdes = models.CharField(max_length=80, blank=True, null=True)
    ncen_costo = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    npe1d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo1d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop1d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe2d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo2d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop2d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe3d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo3d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop3d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe4d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo4d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop4d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe5d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo5d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop5d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe6d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo6d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop6d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe7d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo7d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop7d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe8d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo8d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop8d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe9d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo9d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop9d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe10d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo10d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop10d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe11d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo11d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop11d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe12d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo12d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop12d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ntc1 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    ntc2 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    ntc3 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    ntc4 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    ntc5 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    ntc6 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    ntc7 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    ntc8 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    ntc9 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    ntc10 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    ntc11 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    ntc12 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_presup'


class PgPresupb(models.Model):
    ccod_presu = models.CharField(max_length=10, blank=True, null=True)
    ccod_costo = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_presupb'


class PgPresupc(models.Model):
    ccod_presu = models.CharField(max_length=10, blank=True, null=True)
    ccod_costo = models.CharField(max_length=9, blank=True, null=True)
    npe1 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo1 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop1 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe2 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo2 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop2 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe3 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo3 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop3 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe4 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo4 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop4 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe5 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo5 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop5 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe6 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo6 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop6 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe7 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo7 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop7 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe8 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo8 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop8 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe9 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo9 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop9 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe10 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo10 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop10 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe11 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo11 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop11 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe12 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo12 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop12 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe1d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo1d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop1d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe2d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo2d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop2d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe3d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo3d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop3d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe4d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo4d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop4d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe5d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo5d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop5d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe6d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo6d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop6d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe7d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo7d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop7d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe8d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo8d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop8d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe9d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo9d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop9d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe10d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo10d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop10d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe11d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo11d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop11d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    npe12d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nmo12d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nop12d = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ntc1 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    ntc2 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    ntc3 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    ntc4 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    ntc5 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    ntc6 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    ntc7 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    ntc8 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    ntc9 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    ntc10 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    ntc11 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    ntc12 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_presupc'


class PgProdcat(models.Model):
    ccod_proca = models.CharField(max_length=16, blank=True, null=True)
    cdsc = models.CharField(max_length=80, blank=True, null=True)
    ntipo = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_prodcat'


class PgRecladbf(models.Model):
    cdsc = models.CharField(max_length=200, blank=True, null=True)
    anno = models.CharField(max_length=4, blank=True, null=True)
    ccod_ori_1 = models.CharField(max_length=2, blank=True, null=True)
    ccod_ori_2 = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_recladbf'


class PgRepogen(models.Model):
    cgrupo = models.CharField(max_length=30, blank=True, null=True)
    mfiles = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_repogen'


class PgSeries(models.Model):
    ccod_doc = models.CharField(max_length=2, blank=True, null=True)
    cser = models.CharField(max_length=6, blank=True, null=True)
    nnum = models.DecimalField(max_digits=13, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_series'


class PgSunat05(models.Model):
    ccod_t05 = models.CharField(max_length=2, blank=True, null=True)
    cdsc = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_sunat05'


class PgSunat06(models.Model):
    ccod_t06 = models.CharField(max_length=3, blank=True, null=True)
    cdsc = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_sunat06'


class PgTabdetra(models.Model):
    ccod_detra = models.CharField(max_length=5, blank=True, null=True)
    nporcen = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    cdsc = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_tabdetra'


class PgTeleprov(models.Model):
    cmes = models.CharField(max_length=2, blank=True, null=True)
    ccod_cue = models.CharField(max_length=10, blank=True, null=True)
    ndebe = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaber = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    cglosa = models.CharField(max_length=60, blank=True, null=True)
    ffechadoc = models.DateField(blank=True, null=True)
    cnumero = models.CharField(max_length=20, blank=True, null=True)
    ffechaven = models.DateField(blank=True, null=True)
    ccod_doc = models.CharField(max_length=2, blank=True, null=True)
    ccod_cli = models.CharField(max_length=11, blank=True, null=True)
    cmesc = models.CharField(max_length=2, blank=True, null=True)
    ndebed = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    nhaberd = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    cmreg = models.CharField(max_length=1, blank=True, null=True)
    cid = models.CharField(max_length=10, blank=True, null=True)
    nsaldo = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    namor = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    cdscruc = models.CharField(max_length=80, blank=True, null=True)
    labono = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_teleprov'


class PgTipo(models.Model):
    ccod_tip = models.CharField(max_length=3, blank=True, null=True)
    cdsc = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_tipo'


class PgTipod(models.Model):
    ccod_tipd = models.CharField(max_length=1, blank=True, null=True)
    cdsc = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_tipod'


class PgTiprenta(models.Model):
    ccod_renta = models.CharField(max_length=2, blank=True, null=True)
    cdsc = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_tiprenta'


class PgUserkey(models.Model):
    campo01 = models.CharField(max_length=4, blank=True, null=True)
    campo02 = models.CharField(max_length=10, blank=True, null=True)
    campo03 = models.CharField(max_length=500, blank=True, null=True)
    campo04 = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_userkey'


class PgUseruser(models.Model):
    campo01 = models.CharField(max_length=4, blank=True, null=True)
    campo02 = models.CharField(max_length=4, blank=True, null=True)
    campo03 = models.CharField(max_length=500, blank=True, null=True)
    campo04 = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_useruser'


class PgVendedor(models.Model):
    ccod_vend = models.CharField(max_length=4, blank=True, null=True)
    cdsc = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_vendedor'
