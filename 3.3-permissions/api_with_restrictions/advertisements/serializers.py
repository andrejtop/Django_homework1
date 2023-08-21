from django.contrib.auth.models import User
from rest_framework import serializers

from advertisements.models import Advertisement, AdvertisementStatusChoices


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        user = self.context["request"].user
        if Advertisement.objects.filter(
                creator=user, status=AdvertisementStatusChoices.OPEN
        ).count() >= 10 and data.get('status') != AdvertisementStatusChoices.CLOSED:
            raise serializers.ValidationError('Лимит объявлений превышен. Поменяйте статус объявления(ий) на Закрыто для создания новых объявлений')
        return data

