from django.views import generic
from monitor.models import Host


class IndexView(generic.ListView):

    template_name = 'monitor/index.html'
    context_object_name = 'host_list'

    def get_queryset(self):
        return Host.objects.all().order_by('-status', '-last_status_change')


class DetailView(generic.DetailView):

    template_name = 'monitor/detail.html'
    model = Host

