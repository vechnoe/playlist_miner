# coding: utf-8

from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import ListView, FormView
from django.views.generic.detail import SingleObjectMixin

from core.models import Radiostation
from core.forms import DateFilterForm

class RadiostationListView(ListView):
    model = Radiostation
    template_name = 'core/radiostation_list.html'

class RadiostationDetailView(SingleObjectMixin, FormView):
    template_name = 'core/radiostation_detail.html'
    form_class = DateFilterForm
    model = Radiostation

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(RadiostationDetailView, self).post(
            request, *args, **kwargs)

    def get_success_url(self):
        return reverse('core:radiostation_detail', kwargs={'pk': self.object.pk})

    def get_initial(self):
        initial = super(RadiostationDetailView, self).get_initial()
        initial['begin_date'] = self.object.begin_date
        initial['end_date'] = self.object.end_date
        return initial

    def get_context_data(self, **kwargs):
        context = super(
           RadiostationDetailView, self).get_context_data(**kwargs)
        context['airplay_list'] = self.object.get_airplay_filtered_set()
        context['form'] = self.get_form()
        return context

    def form_valid(self, form):
        begin = form.cleaned_data.get('begin_date')
        end = form.cleaned_data.get('end_date')
        if begin and end is not None:
            self.object.begin_date = begin
            self.object.end_date = end
            self.object.save()
        return redirect(self.get_success_url())


