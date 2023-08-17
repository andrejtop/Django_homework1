from django_filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerPermission
from advertisements.serializers import AdvertisementSerializer



class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    ordering_fields = ['id', 'creator', 'created_at']
    # filterset_class = []


    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create"]:
            return [IsAuthenticated()]
        elif self.action in ["update", "destroy", "partial_update"]:
            return [IsOwnerPermission()]
        return []
