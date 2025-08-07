# Настраивает админку под работу с моделями
from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    # Настройка админ-панелли для модели Note
    list_display = ['title', 'created_at', 'updated_at']
    list_filter = ['created_at']
    search_fields = ['title', 'content']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = [
        ('Основная информация', {
            'fields': ('title', 'content')
        }),
        ('Временные метки', {
            'fields': ('created_at', 'updated_at')
        })
    ]



