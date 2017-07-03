from django.views import generic
from monitor.models import Host, Log, Port
from django.core import serializers
from django.http import JsonResponse
from nltk.stem.lancaster import LancasterStemmer
from django.apps import apps

class IndexView(generic.ListView):

    template_name = 'monitor/index.html'
    context_object_name = 'host_list'

    def get_queryset(self):
        return Host.objects.all().order_by('-status', '-last_status_change')


class DetailView(generic.DetailView):

    template_name = 'monitor/detail.html'
    model = Host

def jsonView(request, model):
    data = []
    #Remove plural and capitalize
    st = LancasterStemmer()
    model_name = st.stem(model).capitalize()

    if model_name in ('Host', 'Log', 'Port'):
        query_model = apps.get_model('monitor', model_name)
        data = serializers.serialize('json', query_model.objects.all())
    return JsonResponse(data, safe=False)
