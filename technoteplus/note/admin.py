from django.contrib import admin
from .models import Note,Tag,SharedNote

@admin.register(Note)
class Admin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title','unique_id','created_by')
    #autocomplete_fields = ["userid"] search field needs to be active in the foreign key
    #exclude = ('pcname',)
    #list of fields displayable
    #fields =  ('uid','userid','devicename','simno','activatedate','expiredate','monthfee','bkash','address')
    readonly_fields = ('created_by', 'updated_by','unique_id')

    def save_model(self, request, obj, form, change):
        #changed data are stored in form.changed_data
        if change:
            obj.updated_by = request.user
        else:
            obj.created_by = request.user
            obj.updated_by = request.user

        super().save_model(request, obj, form, change)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name','created_by','updated_by')
    readonly_fields = ('created_by', 'updated_by')

    def save_model(self, request, obj, form, change):
        #changed data are stored in form.changed_data
        if change:
            obj.updated_by = request.user
        else:
            obj.created_by = request.user
            obj.updated_by = request.user

        super().save_model(request, obj, form, change)

@admin.register(SharedNote)
class SharedNoteAdmin(admin.ModelAdmin):
    search_fields = ['shared_with',]
    list_display = ('shared_with','created_by','updated_by')

    readonly_fields = ('created_by', 'updated_by')

    def save_model(self, request, obj, form, change):
        #changed data are stored in form.changed_data
        if change:
            obj.updated_by = request.user
        else:
            obj.created_by = request.user
            obj.updated_by = request.user

        super().save_model(request, obj, form, change)

