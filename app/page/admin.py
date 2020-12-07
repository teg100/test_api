from django.contrib import admin
from .models import *
from adminsortable.admin import NonSortableParentAdmin, SortableTabularInline


class ABCContentAdmin(SortableTabularInline):
    model = Page.contents.through
    extra = 0


class PageAdmin(NonSortableParentAdmin):
    list_display = ['id', "title"]
    inlines = [ABCContentAdmin]
    fields = ['title']
    search_fields = ('^title',)


def get_list_display(self, request):
        return self.get_fields(request)


def register_all_content_models_in_admin():
    global_vars = globals()
    models = [model for model in global_vars if model.startswith('Content')]
    for model in models:
        cls = type(f'{model}Admin', (admin.ModelAdmin,), {
            'search_fields': ('^title',),
            'get_list_display': get_list_display,
            'readonly_fields': ['counter']
        })
        admin.site.register(global_vars[model], cls)


register_all_content_models_in_admin()
admin.site.register(Page, PageAdmin)