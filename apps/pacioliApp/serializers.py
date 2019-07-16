from django.contrib.auth.models import User
from rest_framework import serializers
from .models import PgPlan, PgDiariolibro

# ccod_cue	cdsc	nnivel	ntipo	nanalisis	ccod_bal
# cdes_d	cdes_h	ndebe0	nhaber0	ndebe1	nhaber1	ndebe2	
# nhaber2	ndebe3	nhaber3	ndebe4	nhaber4	ndebe5	nhaber5	
# ndebe6	nhaber6	ndebe7	nhaber7	ndebe8	nhaber8	ndebe9	
# nhaber9	ndebe10	nhaber10	ndebe11	nhaber11	
# ndebe12	nhaber12	ndebe13	nhaber13	ndebe14	nhaber14	
# ndebe15	nhaber15	nganper	ccue_acm	ndebed0	nhaberd0	
# ndebed1	nhaberd1	ndebed2	nhaberd2	ndebed3	nhaberd3	
# ndebed4	nhaberd4	ndebed5	nhaberd5	ndebed6	nhaberd6	
# ndebed7	nhaberd7	ndebed8	nhaberd8	ndebed9	nhaberd9	
# ndebed10	nhaberd10	ndebed11	nhaberd11	ndebed12	
# nhaberd12	ndebed13	nhaberd13	ndebed14	nhaberd14	
# ndebed15	nhaberd15	ccod_baln	ccod_bal2	ccod_baln2	lajusneg	
# lexpsunat	neducat	ccod_enfin	cnumcta	cmoneda	npresup	ccod_balr	
# ccod_cueci	cnocorr1	cnocorr2	lccadest	lsaldosme	cref	
# cale	cmle	mesmod	anomod




class planSerializer(serializers.ModelSerializer):
    class Meta:
        model = PgPlan
        fields = ('ccod_cue','cdsc' ,'nnivel', 'neducat')

class PlanshortSerializer(serializers.ModelSerializer):
    class Meta:
        model = PgPlan
        fields = ('ccod_cue','cdsc')


#nasiento ccod_cue ndebe nhaber cglosa ccod_ori ffecha

#ccod_cue = models.CharField(max_length=50, blank=True, null=True)
#    ndebe = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
#    nhaber = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
#    cglosa = models.CharField(max_length=250, blank=True, null=True)
#    ccod_ori = models.CharField(max_length=250, blank=True, null=True)
#    nasiento = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

class libroDiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PgDiariolibro
        fields = ('ccod_cue', 'ndebe', 'nhaber', 'cglosa', 'ccod_ori', 'nasiento')

class libroDiarioShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = PgDiariolibro
        fields = ( 'ccod_cue', 'cglosa')