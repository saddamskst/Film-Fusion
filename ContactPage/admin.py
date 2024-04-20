from django.contrib import admin
from ContactPage.models import Contact_List

class Contact_list(admin.ModelAdmin):
    list_display = ['Name', 'Email', 'Phone', 'Message'] #, 'edit_button', 'delete_button']
    search_fields = ['Name', 'Email', 'Phone', 'Message']
    
    #list_display_links = None

    def edit_button(self, obj):
        return f'<a href="/admin/Movies/add_movie/{obj.id}/change/">Edit</a>'
    edit_button.short_description = 'Edit'
    #edit_button.button='edit'

    def delete_button(self, obj):
        return f'<a href="/admin/Movies/add_movie/{obj.id}/delete/">Delete</a>'
    delete_button.short_description = 'Delete'

admin.site.register(Contact_List, Contact_list)