import datetime
import logging
from django.utils import timezone
from django.urls import reverse
from django.test import TestCase

from .settings import DAYS_FROM_DANGER_TO_WARNING
from .models import Host

logging.disable(logging.CRITICAL)

class HostModelTest(TestCase):
    def test_online_host(self):
        """
        Test a "pingable" host
        """
        online_host = Host(name='online', ipv4='127.0.0.1')
        self.assertEqual(Host.DEFAULT, online_host.status)
        online_host.check_and_update()
        self.assertEqual(Host.SUCCESS, online_host.status)

    def test_offline_host(self):
        """
        Test a offline host
        """
        offline_host = Host(
            name='offline',
            ipv4='7.7.7.7',
            status=Host.SUCCESS,
            )
        offline_host.check_and_update()
        self.assertEqual(Host.DANGER, offline_host.status)

    def test_danger_to_warning_status_host(self):
        """
        Change host status after DAYS_FROM_DANGER_TO_WARNING
        """
        now = timezone.now()
        offline_host = Host(
            name='offline',
            ipv4='7.7.7.7', 
            status=Host.DANGER,
            last_status_change = now - datetime.timedelta(days=DAYS_FROM_DANGER_TO_WARNING),
            status_info = 'Connection Lost',
            )
        offline_host.check_and_update()
        self.assertEqual(Host.WARNING, offline_host.status)
        

class HostListViewTests(TestCase):
    def test_empty_list(self):
        """
        If no hosts exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('monitor:host_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No hosts are available.")
        self.assertQuerysetEqual(response.context['host_list'], [])
