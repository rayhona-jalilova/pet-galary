from rest_framework.serializers import ModelSerializer

from accounts.models.abstract.contact_model import Contact


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ["phone_number", "email"]
