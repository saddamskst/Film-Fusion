from django.contrib import admin
from Movies.models import Add_Movie

class Mov_list(admin.ModelAdmin):
    list_display = ['Movie_Name', 'Year', 'Genre', 'Directed_By', 'rating'] #, 'edit_button', 'delete_button']
    search_fields = ['Movie_Name', 'Year', 'Genre', 'rating', 'Directed_By', 'Description']
    list_display_links = None

    def edit_button(self, obj):
        return f'<a href="/admin/Movies/add_movie/{obj.id}/change/">Edit</a>'
    edit_button.short_description = 'Edit'

    def delete_button(self, obj):
        return f'<a href="/admin/Movies/add_movie/{obj.id}/delete/">Delete</a>'
    delete_button.short_description = 'Delete'

admin.site.register(Add_Movie, Mov_list)
