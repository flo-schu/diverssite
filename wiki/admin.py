from django.contrib import admin
from django.http import HttpResponseRedirect
from simple_history.admin import SimpleHistoryAdmin

from .forms import ArticleAdminForm

# Register your models here.
from .models import Article, Category, Display, File, Image


class FileTabularInline(admin.TabularInline):
    extra = 1


class FileInline(FileTabularInline):
    model = Article.files.through


class ImageInline(FileTabularInline):
    model = Article.images.through


@admin.register(Article)
class ArticleAdmin(SimpleHistoryAdmin):
    form = ArticleAdminForm
    inlines = [ImageInline, FileInline]
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        "title",
        "visibility",
        "pub_date",
    )
    list_filter = ["pub_date", "visibility", "show_on_pages"]
    search_fields = ["title"]
    exclude = ["images", "files"]

    # def response_add(self, request, obj, post_url_continue=None):
    #     """
    #     This makes the response after adding go to another
    #     app's changelist for some model
    #     """
    #     app = obj.__module__.split(".")[0]
    #     path = f"{app}/{obj.slug}"
    #     return redirect(path)

    def response_change(self, request, obj, post_url_continue=None):
        """
        This makes the response go to the newly created
        model's change page without using reverse
        """
        full_path = request.get_full_path()
        if "?next=" in full_path:
            _, redirect_page = request.get_full_path().split("?next=")
            return HttpResponseRedirect(redirect_page)
        else:
            return super(ArticleAdmin, self).response_change(request, obj)


admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Display)
admin.site.register(File)
