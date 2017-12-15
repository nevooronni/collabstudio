from django.contrib import admin
from .models import Comments,Profile,Project,Tags,Follow

class ProjectAdmin(admin.ModelAdmin):
	filter_horizontal = ('tags',)

admin.site.register(Comments)
admin.site.register(Profile)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Tags)
admin.site.register(Follow)


