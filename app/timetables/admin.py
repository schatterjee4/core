from django.contrib import admin

from .models import (
    Event, Weekday, MealOption, Course, Meal, Timetable, Dish, Admin, MenuItem
)


@admin.register(Weekday, MealOption, Course)
class DefaultAdmin(admin.ModelAdmin):
    """Default admin for models with just name and slug fields."""
    readonly_fields = ('slug',)


@admin.register(Meal)
class MealAdmin(DefaultAdmin):
    fields = ('name', 'slug', 'start_time', 'end_time')


class AdminsInline(admin.TabularInline):
    model = Timetable.admins.through


@admin.register(Timetable)
class TimetableAdmin(DefaultAdmin):
    fields = ('name', 'slug', 'code', 'api_key', 'cycle_length',
              'current_cycle_day', 'description')
    inlines = (AdminsInline,)


@admin.register(Dish)
class DishAdmin(DefaultAdmin):
    fields = ('name', 'slug', 'description')


admin.site.empty_value_display = ''

other_models = [Event, Admin, MenuItem]
admin.site.register(other_models)
