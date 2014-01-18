from django.contrib import admin
from workouts.models import Exercise, Session, ExerciseType, Set, Location, Weight, TargetWeight

class LocationAdmin(admin.ModelAdmin):
	fields = ['name', 'details']
	list_display = ('name', 'details')

class ExerciseAdmin(admin.ModelAdmin):
	list_display = ('name', 'description_short', 'exercise_type')

admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Session)
admin.site.register(ExerciseType)
admin.site.register(Set)
admin.site.register(Location, LocationAdmin)
admin.site.register(Weight)	
admin.site.register(TargetWeight)
