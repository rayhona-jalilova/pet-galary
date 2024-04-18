from rest_framework.serializers import ModelSerializer

from accounts.models import Address


class AddressModelSerializer(ModelSerializer):
    """Serializer for Address model"""

    class Meta:
        model = Address
        fields = ["street", "city", "province", "country"]
