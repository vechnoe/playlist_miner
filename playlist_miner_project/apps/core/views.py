# coding: utf-8

from django.views.generic import ListView, DetailView

from core.models import Radiostation

class RadiostationListView(ListView):
    model = Radiostation
    template_name = 'core/radiostation_list.html'

class RadiostationDetailView(DetailView):
    model = Radiostation
    template_name = 'core/radiostation_detail.html'

    def get_context_data(self, **kwargs):
        context = super(
            RadiostationDetailView, self).get_context_data(**kwargs)
        context['airplay_list'] = self.object.airplay_set.all()
        return context
