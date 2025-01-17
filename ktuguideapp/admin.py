from django.contrib import admin
from .models import Scheme, Branch, Semester, Subject, Notes, YTLink, KTUUpdates, Newsletter

admin.site.register(Scheme)
admin.site.register(Branch)
admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(Notes)
admin.site.register(YTLink)
admin.site.register(Newsletter)

@admin.register(KTUUpdates)
class KTUUpdatesAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')