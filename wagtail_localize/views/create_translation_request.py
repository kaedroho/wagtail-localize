from django import forms

from django.contrib import messages
from django.db import transaction
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from wagtail.core.models import Page, Locale, get_translatable_models

from wagtail_localize.fields import WAIT
from wagtail_localize.models import Translation, TranslationSource


class CreateTranslationRequestForm(forms.Form):
    locales = forms.ModelMultipleChoiceField(
        queryset=Locale.objects.none(), widget=forms.CheckboxSelectMultiple
    )
    include_subtree = forms.BooleanField(required=False)

    def __init__(self, page, *args, **kwargs):
        super().__init__(*args, **kwargs)

        page_descendant_count = (
            page.get_descendants().type(tuple(get_translatable_models())).count()
        )
        if page_descendant_count > 0:
            self.fields[
                "include_subtree"
            ].help_text = "This will add {} additional pages to the request".format(
                page_descendant_count
            )
        else:
            self.fields["include_subtree"].widget = forms.HiddenInput()

        self.fields["locales"].queryset = Locale.objects.filter(is_active=True).exclude(
            id=page.locale_id
        )


def create_translation_request(request, page_id):
    page = get_object_or_404(Page, id=page_id).specific

    if request.method == "POST":
        form = CreateTranslationRequestForm(page, request.POST)

        if form.is_valid():
            with transaction.atomic():
                seen_objects = set()

                def _create_translation_requests(instance, target_locales, include_related_objects=True):
                    if isinstance(instance, Page):
                        # TODO: Find a way to handle non-page models with MTI
                        instance = instance.specific

                    if instance.translation_key in seen_objects:
                        return
                    seen_objects.add(instance.translation_key)

                    source, created = TranslationSource.from_instance(instance)

                    if created:
                        source.extract_segments()

                    for target_locale in target_locales:
                        # Create/update translation
                        t, created = Translation.objects.update_or_create(
                            object=source.object,
                            target_locale=target_locale,
                            defaults={
                                'source': source,
                            }
                        )
                        t.update(user=request.user)

                    # Add related objects
                    if include_related_objects:
                        for related_object_segment in source.relatedobjectsegment_set.filter(if_untranslated=WAIT):
                            related_instance = related_object_segment.object.get_instance(instance.locale)

                            # Limit to one level of related objects, since this could potentially pull in a lot of stuff
                            _create_translation_requests(related_instance, target_locales, include_related_objects=False)

                _create_translation_requests(page, form.cleaned_data["locales"])

                # Now add the sub tree
                if form.cleaned_data["include_subtree"]:
                    translatable_models = tuple(get_translatable_models())

                    def _walk(current_page):
                        for child_page in current_page.get_children():
                            if not issubclass(
                                child_page.specific_class, translatable_models
                            ):
                                continue

                            _create_translation_requests(child_page, form.cleaned_data["locales"])

                            if child_page.numchild:
                                _walk(child_page)

                    _walk(page)

                messages.success(
                    request, "The translation request was submitted successfully"
                )
                return redirect("wagtailadmin_explore", page.get_parent().id)
    else:
        form = CreateTranslationRequestForm(page)

    return render(
        request,
        "wagtail_localize/admin/create_translation_request.html",
        {"page": page, "form": form},
    )
