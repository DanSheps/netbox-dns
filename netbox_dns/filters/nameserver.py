import django_filters
from django.db.models import Q

from netbox.filtersets import NetBoxModelFilterSet

from netbox_dns.models import NameServer


class NameServerFilter(NetBoxModelFilterSet):
    """Filter capabilities for NameServer instances."""

    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )
    name = django_filters.CharFilter(
        lookup_expr="icontains",
    )

    class Meta:
        model = NameServer
        fields = ("name",)

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = Q(name__icontains=value)
        return queryset.filter(qs_filter)
