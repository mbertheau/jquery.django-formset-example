from .forms import BlockForm
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
    form_class = BlockForm

    def get_success_url(self):
        return reverse('blocks-list')


class ListBlocksView(ListView):
    model = models.Block


class CreateBlockView(BlockView, CreateView):
    pass


NestedBlockForm = nestedformset_factory(
    models.Block,
    models.Building,
    nested_formset=inlineformset_factory(
        models.Building,
        models.Tenant,
        fields='__all__'
    )
)


BlockForm = inlineformset_factory(models.Block, models.Building, fields='__all__')


class EditBuildingsView(BlockView, UpdateView):
    template_name = 'blocks/building_form.html'
    form_class = NestedBlockForm


class EditBuildingsDynamicView(BlockView, UpdateView):
    template_name = 'blocks/building_form_dynamic.html'
    form_class = BlockForm


class EditBuildingsDynamicTabsView(BlockView, UpdateView):
    template_name = 'blocks/building_form_dynamic_tabs.html'
    form_class = BlockForm


class EditBuildingsDynamicTabsNestedView(BlockView, UpdateView):
    template_name = 'blocks/building_form_dynamic_tabs_nested.html'
    form_class = NestedBlockForm
