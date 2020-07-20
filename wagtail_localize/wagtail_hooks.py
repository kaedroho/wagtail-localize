from django.conf.urls import url, include
from django.templatetags.static import static
from django.urls import reverse
from django.utils.html import format_html_join
from django.utils.translation import ugettext_lazy as _

from wagtail.admin import widgets as wagtailadmin_widgets
from wagtail.admin.menu import MenuItem
from wagtail.core import hooks

from . import admin_views
from .views.create_translation_request import create_translation_request
from .views.management import TranslationViewSet
from .views.translate import export_file, import_file, machine_translate, translation_form


@hooks.register("insert_editor_js")
def insert_editor_js():
    js_files = ["wagtail_localize/js/page-editor.js"]
    return format_html_join(
        "\n",
        '<script src="{0}"></script>',
        ((static(filename),) for filename in js_files),
    )


@hooks.register("register_admin_urls")
def register_admin_urls():
    urls = [
        url(r"^translations_list/(\d+)/$", admin_views.translations_list_modal, name="translations_list_modal"),
        url(
            r"^create_translation_request/(\d+)/$",
            create_translation_request,
            name="create_translation_request",
        ),
        url(r"^machine_translate/(\d+)/$", machine_translate, name="machine_translate"),
        url(r"^export_file/(\d+)/$", export_file, name="export_file"),
        url(r"^import_file/(\d+)/$", import_file, name="import_file"),
        url(r"^translation_form/(\d+)/$", translation_form, name="translation_form"),
    ]

    return [
        url(
            r"^localize/",
            include(
                (urls, "wagtail_localize"),
                namespace="wagtail_localize",
            ),
        )
    ]


@hooks.register("register_page_listing_more_buttons")
def page_listing_more_buttons(page, page_perms, is_parent=False, next_url=None):
    yield wagtailadmin_widgets.Button(
        "Create translation request",
        reverse(
            "wagtail_localize:create_translation_request", args=[page.id]
        ),
        priority=60,
    )


@hooks.register("register_admin_viewset")
def register_viewset():
    return TranslationViewSet(
        "wagtail_localize_management",
        url_prefix="localize/translations",
    )


class TranslationsMenuItem(MenuItem):
    def is_shown(self, request):
        return True


@hooks.register("register_admin_menu_item")
def register_menu_item():
    return TranslationsMenuItem(
        _("Translations"),
        reverse("wagtail_localize_management:list"),
        classnames="icon icon-site",
        order=500,
    )
