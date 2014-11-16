from django.core.urlresolvers import reverse
from django.forms.models import inlineformset_factory
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
)

from nested_formset import nestedformset_factory

from blocks import models


class BlockView(object):
    model = models.Block
    # don't conflict with django's block template context variable
    context_object_name = "Block"


class ListBlocksView(ListView):
    model = models.Block


class CreateBlockView(BlockView, CreateView):
    def get_success_url(self):

        return reverse('blocks-list')


class EditBuildingsView(BlockView, UpdateView):
    def get_template_names(self):

        return ['blocks/building_form.html']

    def get_form_class(self):

        return nestedformset_factory(
            models.Block,
            models.Building,
            nested_formset=inlineformset_factory(
                models.Building,
                models.Tenant
            )
        )

    def get_success_url(self):

        return reverse('blocks-list')
