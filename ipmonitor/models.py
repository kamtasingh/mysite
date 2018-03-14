# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User,Group
from django.db import models


# Create your models here.
MACHINE_TYPE=((1,"Windows PC"),(2,"Ubuntu"))
OPERATING_SYSTEM=((1,"Windows 10 Aniversary"),(2,"Windows 10 Pro"),(3,"Windows 10"),(4,"Windows 8"),(5,"Windows 7"),(6,"Ubuntu"))
SERVER_TYPE=((1,"ESXI"),(2,"AWV Server"))
SERVER_OPERATING_SYSTEM=((1,"ESXI"),(2,"MSL"))
class MachineDetail(models.Model):
    machine_type = models.IntegerField(choices=MACHINE_TYPE, default=1)
    operating_system=models.IntegerField(choices=OPERATING_SYSTEM, default=1)
    v4_ip=models.GenericIPAddressField(protocol="ipv4")
    hostName=models.CharField(max_length=100,unique=True)
    ram = models.IntegerField(null=True,blank=True)
    symantic=models.BooleanField(default=False)
    domain=models.CharField(max_length=100,null=True,blank=True)
    location=models.CharField(max_length=100,null=True,blank=True)
    cabinet_esxi=models.CharField(max_length=100,null=True,blank=True)
    esxi_server_id=models.CharField(max_length=100,null=True,blank=True)
    softwares=models.TextField(null=True,blank=True)
    owner_team= models.ForeignKey(Group,null=True,blank=True)
    owner_person=models.ForeignKey(User,null=True,blank=True,related_name='owner')
    created_by=models.ForeignKey(User,null=True,blank=True,related_name='creator')
    updated_by=models.ForeignKey(User,null=True,blank=True,related_name='updator')
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    isactive=models.BooleanField(default=True)
    def __unicode__(self):
        return str(self.v4_ip)


class ServerDetail(models.Model):
    machine_type = models.IntegerField(choices=SERVER_TYPE, default=1)
    operating_system=models.IntegerField(choices=SERVER_OPERATING_SYSTEM, default=1)
    v4_ip=models.GenericIPAddressField(protocol="ipv4")
    fqdn=models.CharField(max_length=100,null=True,blank=True)
    ram = models.IntegerField(null=True,blank=True,default=0)
    location=models.CharField(max_length=100,null=True,blank=True)
    owner_team= models.ForeignKey(Group,null=True,blank=True)
    owner_person=models.ForeignKey(User,null=True,blank=True,related_name='server_owner')
    created_by=models.ForeignKey(User,null=True,blank=True,related_name='server_creator')
    updated_by=models.ForeignKey(User,null=True,blank=True,related_name='server_updator')
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    isactive=models.BooleanField(default=True)
    def __unicode__(self):
        return str(self.v4_ip)

class SanityMaster(models.Model):
    Serialnumber = models.IntegerField(null=True,blank=True)
    Platform=models.CharField(max_length=100,null=True,blank=True)
    BuildID=models.IntegerField(null=True,blank=True)
    BuildName=models.CharField(max_length=100,null=True,blank=True)
    StatusType = models.CharField(max_length=100,null=True,blank=True)
    IsActive=models.BooleanField(default=True)
    def __unicode__(self):
        return str(self.Serialnumber)

    class Meta:
        managed = False
        db_table = 'ipmonitor_sanitymaster'

class AgentsDetail(models.Model):
    AgentID = models.IntegerField(null=True,blank=True)
    AgentIP=models.GenericIPAddressField(protocol="ipv4")
    SetupPlatform = models.CharField(max_length=100, null=True, blank=True)
    AgentState=models.CharField(max_length=100,null=True,blank=True)
    DownloadPercentage = models.IntegerField(null=True,blank=True,default=0)
    def __unicode__(self):
        return str(self.AgentID)
    class Meta:
        managed = False
        db_table = 'ipmonitor_agentdetail'

