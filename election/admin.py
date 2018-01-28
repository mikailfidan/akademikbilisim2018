from django.contrib import admin
from election.models import Survey, Category
#from election.models import Category
from import_export import resources
from import_export.admin import ImportExportMixin


class CategoryReSource(resources.ModelResource):
    class Meta:
        model = Category
        fields = ('title', 'desc', )
        export_order = ('title','desc',)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'created_at',)
    list_filter = ('title',)
    search_fields = ('title',)
    resource_class = CategoryReSource



class SurveyResource(resources.ModelResource):
    class Meta:
        model = Survey
        fields = ('id','name','active','created_at',)
        export_order = ('id','name','active','created_at', )



class SurveyAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'active', 'created_at','category',)
    list_filter = ('active',)
    search_fields = ('name',)
    resource_class = SurveyResource




admin.site.register(Survey, SurveyAdmin)
admin.site.register(Category, CategoryAdmin)
