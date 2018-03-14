# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
import os

# Register your models here.
class MachineDetailAdmin(admin.ModelAdmin):
    list_display = ('v4_ip','status','machine_type','operating_system','hostName','ram',
                    'symantic','domain','location','cabinet_esxi','esxi_server_id',
                    'owner_team','owner_person','isactive')
    #list_editable = ('owner_team','owner_person')
    exclude = ('created_by','updated_by',)
    list_per_page=5

    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user
        if not obj.created_by:
            obj.created_by = request.user
        super(MachineDetailAdmin, self).save_model(request, obj, form, change)
    def status(self,obj):
        data = os.system("ping -c 4 " + obj.v4_ip)
        if data == 0:
            return '<img src="/static/admin/img/icon-yes.svg" alt="True">'
        return '<img src="/static/admin/img/icon-no.svg" alt="True">'

    status.allow_tags = True
# Register your models here.
class ServerDetailAdmin(admin.ModelAdmin):
    list_display = ('v4_ip','status','machine_type','operating_system','fqdn','ram',
                    'location','owner_team','owner_person','isactive')
    #list_editable = ('owner_team','owner_person')
    exclude = ('created_by','updated_by',)
    list_per_page=5

    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user
        if not obj.created_by:
            obj.created_by = request.user
        super(ServerDetailAdmin, self).save_model(request, obj, form, change)
    def status(self,obj):
        data = os.system("ping -c 4 " + obj.v4_ip)
        if data == 0:
            return '<img src="/static/admin/img/icon-yes.svg" alt="True">'
        return '<img src="/static/admin/img/icon-no.svg" alt="True">'

    status.allow_tags = True
class SanityMasterAdmin(admin.ModelAdmin):
    list_display = ('Serialnumber','Platform','BuildID','BuildName','StatusType','IsActive')
class AgentsDetailAdmin(admin.ModelAdmin):
    list_display = ('AgentID','AgentIP','SetupPlatform','AgentState','DownloadPercentage')

admin.site.register(MachineDetail,MachineDetailAdmin)
admin.site.register(ServerDetail,ServerDetailAdmin)
admin.site.register(SanityMaster,SanityMasterAdmin)
admin.site.register(AgentsDetail,AgentsDetailAdmin)