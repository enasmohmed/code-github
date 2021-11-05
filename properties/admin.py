from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from properties.models import Category, SubCategory, CardsFeatures, CardsProgramUnits, CardDoxHome, \
    CardEliteHome, DetailSubCategory, DetailSection


class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(Category)
admin.site.register(SubCategory)

admin.site.register(DetailSubCategory, SomeModelAdmin)

admin.site.register(DetailSection, SomeModelAdmin)


admin.site.register(CardsFeatures, SomeModelAdmin)

admin.site.register(CardsProgramUnits, SomeModelAdmin)
admin.site.register(CardDoxHome, SomeModelAdmin)
admin.site.register(CardEliteHome, SomeModelAdmin)

